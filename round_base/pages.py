from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class RoundBeginWait(WaitPage):
    after_all_players_arrive = 'begin'


class Round(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.id_in_group == self.group.A_id:
            return []
        else:
            return ['is_selfish']


class RoundWait(WaitPage):
    # 正常等待--所有人结束
    after_all_players_arrive = 'set_deposit'

class AChoice(Page):
    form_model = 'group'
    form_fields = ['A_continue']
    def is_displayed(self):
        return self.player.id_in_group == self.group.A_id

class AChoiceWait(WaitPage):
    # 所以角色B等待
    after_all_players_arrive = 'set_A_choice'

class BVote(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.id_in_round == self.group.A_continue:
            return []
        else:
            return ['B_vote']
    def is_displayed(self):
        return self.group.A_continue != 0 and self.player.id_in_group != self.group.A_id

class BVoteWait(WaitPage):
    # A等待
    after_all_players_arrive = 'set_B_vote'
class Show(Page):
    pass

page_sequence = [
    RoundBeginWait,
    Round,
    RoundWait,
    AChoice,
    AChoiceWait,
    BVote,
    BVoteWait,
    Show,
]
