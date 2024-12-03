from otree.api import *

import random
class C(BaseConstants):
    NAME_IN_URL = 'signup_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass



class Player(BasePlayer):
    email = models.StringField()

    def make_field(label):
        return models.IntegerField(
            choices=[1, 2, 3, 4, 5],
            label=label,
            widget=widgets.RadioSelect,
        )
    ##Questions on emotions and feelings
    happy = make_field(label="Happiness")
    sad = make_field(label="Sadness")
    fear = make_field(label="Fear")
    disgust = make_field(label="Disgust")
    anger = make_field(label="Anger")
    compassion = make_field(label="Compassion")
    guilt = make_field(label="Guilt")
    boredom = make_field(label="Boredom")
    anger = make_field(label="Anger")
    hope = make_field(label="Hope")
    ##
    first_q = models.IntegerField()
    angry = models.IntegerField()

    identification_concern = models.IntegerField(label="To what degree would you be concerned about being perceived as someone who signs up to the mentoring meeting under 'bad' intentions (to take advantage of the student, for example)?")
    distribution_good = models.IntegerField(label="Overall, how common do you think it is that people choose to participate in this mentoring program under good intentions?")

class Questions_(Page):
    form_model = 'player'
    form_fields = ['angry']







page_sequence = [Questions_]
