from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class RoundBeginWait(WaitPage):
    after_all_players_arrive = 'begin'

class Part1(Page):
    form_model = 'player'
    form_fields = ['process_understand_level','income_satisfaction_level','manager_decision_satisfaction_level','second_stage_rule_satisfaction_level','willing_participate_level']


class Part2(Page):
    form_model = 'player'
    form_fields = ['is_male', 'is_economics_or_management', 'grade_level']

class Part3(Page):
    form_model = 'player'
    form_fields = ['is_party_member','is_student_union_member','is_cadre','is_hourly_workers','is_scholarship_member','own_expenses_level','is_from_village','is_minority_nationalities','family_annual_income_level']

class Over(Page):
    pass

page_sequence = [
    RoundBeginWait,
    Part1,
    Part2,
    Part3,
    Over,
]
