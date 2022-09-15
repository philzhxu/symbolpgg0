from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'round_base_limited'
    players_per_group = 5
    num_rounds = 20
    multiplication_factor = 2

    num_A = 1
    num_B = players_per_group - num_A

    base_punish = 30
    base_deposit = 20
    base_wave = 1 / 6
    cost_select_A = 2
    cost_select_B = 1
    entrance_fee = 5
    Rule_base = 'rule_base_limited/Rule_base.html'


class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    def begin(self):
        if self.round_number == 1:
            from random import randint
            A_id = randint(1, 5)
            self.A_id = A_id
        else:
            self.A_id = self.in_round(self.round_number-1).A_id
        players = self.get_players()
        from random import shuffle
        self.session.vars['id_pool'] = list(range(1, Constants.num_B + 1))
        shuffle(self.session.vars['id_pool'])
        for other in players[:self.A_id-1]+players[self.A_id:]:
            other.id_in_round = self.session.vars['id_pool'].pop()
        return ''
    A_id = models.IntegerField()
    game = models.StringField(initial="Dickson salary limited")
    deposit_sum = models.IntegerField(initial=0)
    public2deposit = models.FloatField()
    A_continue = models.IntegerField(
        choices=[(0, '不选择任何人'), *[(i, 'ID为%d的参与者' % i) for i in range(1, Constants.num_B + 1)]], label='',
        widget=widgets.RadioSelectHorizontal)
    is_punish = models.BooleanField()
    favor_num = models.IntegerField(initial=0)
    opposition = models.IntegerField(initial=0)

    def set_deposit(self):
        players = [i for i in self.get_players() if i.id_in_group != self.A_id]
        for player in players:
            if not player.in_round(self.round_number).is_selfish:
                self.deposit_sum += Constants.base_deposit

        self.public2deposit = self.deposit_sum * Constants.multiplication_factor / Constants.players_per_group
        for player in self.get_players():
            player.round_deposit = self.public2deposit + (
                        player.in_round(self.round_number).is_selfish in (None, True)) * 20

    def set_A_choice(self):
        pass

    def set_B_vote(self):
        from random import random
        players = [i for i in self.get_players() if i.id_in_group != self.A_id]
        all_players = self.get_players()
        for i in players:
            if i.B_vote == 1:
                self.favor_num += 1
            elif i.B_vote == -1:
                self.opposition += 1
        self.is_punish = random() < (0.5 + (self.favor_num - self.opposition) / (Constants.players_per_group + 1))

        if self.A_continue == 0:
            for player in all_players:
                player.real_round_deposit = player.round_deposit
        else:
            for player in players:
                player.real_round_deposit = player.round_deposit - bool(player.B_vote) * 1 - (
                            player.id_in_round == self.A_continue and self.is_punish) * 30
            A = self.get_player_by_id(self.A_id)
            A.real_round_deposit = A.round_deposit - bool(self.A_continue) * 2

        if self.round_number == Constants.num_rounds:
            print('*' * 10)
            for player in all_players:
                player.participant.vars['all'] = 0
                rounds = player.in_all_rounds()
                for round in rounds:
                    player.participant.vars['all'] += round.real_round_deposit
                player.participant.vars['all_in_all']  = Constants.entrance_fee + float(format(player.participant.vars['all'] / 20, '.2f'))
                player.all_profit = player.participant.vars['all_in_all']
    def get_deduction_result(self):
        return "" if self.is_punish else "未"

    def get_sorted_id_in_round(self):
        players = [i for i in self.get_players() if i.id_in_group != self.A_id]
        players.sort(key=lambda x: x.id_in_round)
        return [(i.id_in_round, '都留在私人账户' if i.is_selfish else '都存入本组公共账户') for i in players]

    def get_sorted_id_in_round_contain_A(self):
        players = [i for i in self.get_players() if i.id_in_group != self.A_id]
        players.sort(key=lambda x: x.id_in_round)
        return [("角色A", "未参与", self.get_player_by_id(self.A_id).real_round_deposit)] + [
            (i.id_in_round, '都留在私人账户' if i.is_selfish else '都存入本组公共账户', i.real_round_deposit) for i in players]

    def get_favor_tuple(self):
        return (self.favor_num, self.opposition, Constants.num_B - 1 - self.opposition - self.favor_num)


class Player(BasePlayer):
    id_in_round = models.IntegerField()
    is_selfish = models.BooleanField(label='', choices=[(True, '都留在私人账户'), (False, '都存入本组公共账户')],
                                     widget=widgets.RadioSelectHorizontal)
    round_deposit = models.FloatField()
    B_vote = models.IntegerField(choices=[(0, '什么也不做'), (1, '同意A的决策'), (-1, '反对A的决策')],
                                 widget=widgets.RadioSelectHorizontal, label='')
    real_round_deposit = models.FloatField()

    all_profit = models.FloatField()
