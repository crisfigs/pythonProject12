from otree.api import *

import random
class C(BaseConstants):
    NAME_IN_URL = 'website'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass



class Player(BasePlayer):
  pass
class website(Page):
    pass
page_sequence = [website]
