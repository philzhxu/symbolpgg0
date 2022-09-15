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
    name_in_url = 'survey'
    players_per_group = 5
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def begin(self):
        from random import shuffle
        order_number_list = list(range(1, Constants.players_per_group + 1))
        shuffle(order_number_list)
        for player in self.get_players():
            player.order_number = order_number_list.pop()


class Player(BasePlayer):
    order_number = models.IntegerField()
    # Part1
    process_understand_level = models.IntegerField(choices=[(0,'完全不理解'),(1,''),(2,''),(3,''),(4,'完全理解')],widget=widgets.RadioSelectHorizontal,label='')
    income_satisfaction_level = models.IntegerField(choices=[(0,'非常不满意'),(1,''),(2,''),(3,''),(4,'完全满意')],widget=widgets.RadioSelectHorizontal,label='')
    manager_decision_satisfaction_level = models.IntegerField(choices=[(-1,'我不是管理者'),(0,'非常不满意'),(1,''),(2,''),(3,''),(4,'完全满意')],widget=widgets.RadioSelectHorizontal,label='')
    second_stage_rule_satisfaction_level = models.IntegerField(choices=[(0,'非常不满意'),(1,''),(2,''),(3,''),(4,'完全满意')],widget=widgets.RadioSelectHorizontal,label='')
    willing_participate_level = models.IntegerField(choices=[(0, '愿意'), (1, '不愿意'), (2, '不确定')], widget=widgets.RadioSelectHorizontal,label='')


    # Part2
    is_male = models.BooleanField(choices=[(True,'男性'),(False,'女性')], widget=widgets.RadioSelectHorizontal, label='')
    is_economics_or_management = models.BooleanField(choices=[(True, '是'), (False, '不是')], widget=widgets.RadioSelectHorizontal, label='')
    grade_level = models.IntegerField(choices=[(1,'大一'),(2,'大二'),(3,'大三'),(4,'大四'),(5,'研究生')], widget=widgets.RadioSelectHorizontal,label='')


    # Part3
    is_party_member = models.BooleanField(choices=[(True,'是'),(False,'不是')],widget=widgets.RadioSelectHorizontal,label='')
    is_student_union_member = models.BooleanField(choices=[(True,'有'),(False,'没有')],widget=widgets.RadioSelectHorizontal,label='')
    is_cadre = models.BooleanField(choices=[(True,'是'),(False,'不是')],widget=widgets.RadioSelectHorizontal,label='')
    is_hourly_workers = models.BooleanField(choices=[(True,'有'),(False,'没有')],widget=widgets.RadioSelectHorizontal,label='')
    is_scholarship_member = models.BooleanField(choices=[(True,'有'),(False,'没有')],widget=widgets.RadioSelectHorizontal,label='')
    own_expenses_level = models.IntegerField(choices=[(0,'1000元一下'),(1,'1001元-2000元'),(2,'2001元-4000元'),(3,'4000元以上')],widget=widgets.RadioSelectHorizontal,label='')
    is_from_village = models.BooleanField(choices=[(True,'农村'),(False,'城市')],widget=widgets.RadioSelectHorizontal,label='')
    is_minority_nationalities = models.BooleanField(choices=[(True,'少数民族'),(False,'汉族')],widget=widgets.RadioSelectHorizontal,label='')
    family_annual_income_level = models.IntegerField(choices=[(0,'5万元一下'),(1,'5万元-10万元'),(2,'10万元-20万元'),(3,'20万元以上')],widget=widgets.RadioSelectHorizontal,label='')