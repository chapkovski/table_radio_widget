from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from .widgets import TableRadio

author = 'Philip Chapkovski, chapkovski@gmail.com'

doc = """
Example of 'Other' field 
"""


class Constants(BaseConstants):
    name_in_url = 'other_field_app'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    s1 = models.IntegerField(
        label='What do you think about Moscow if you compare it to Boston?',
        choices=[1, 2, 3, 4, 5, ],
        widget=TableRadio(bottom_row=['Worse place to live', 'Better place to live '], )
    )
