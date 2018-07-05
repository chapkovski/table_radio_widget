from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class MyPage(Page):
    form_model = 'player'
    form_fields = ['s1']

# second page just to test that fields correctly rendered with values
class MyPage2(Page):
    form_model = 'player'
    form_fields = ['s1']


page_sequence = [
    MyPage,
    MyPage2,
]


