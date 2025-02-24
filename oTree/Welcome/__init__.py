from otree.api import *
import random
# RECAPTCHA
import requests
from otree.settings import RECAPTCHA_SECRET_KEY, RECAPTCHA_SITE_KEY

class C(BaseConstants):
    NAME_IN_URL = 'Dana'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    participation_fee = 2 # in pounds



class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
        pass

class Player(BasePlayer):
    prolific_id = models.StringField()
    treatnumber = models.IntegerField()
    is_human = models.BooleanField(initial=False)

def recaptcha_valid(response_token):
    res = requests.post("https://www.google.com/recaptcha/api/siteverify", data={
        'secret': RECAPTCHA_SECRET_KEY,
        'response': response_token
    })
    return res.json()["success"]

class Welcome(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        player.treatnumber = random.choices([1,2,3,4], weights=(1/4,1/4,1/4,1/4), k=1)[0]
        return {
            'treatnumber': player.treatnumber,
            "RECAPTCHA_SITE_KEY": RECAPTCHA_SITE_KEY
        }
    def live_method(player: Player, data):
        if recaptcha_valid(data["response_token"]):
            player.is_human = True

    @staticmethod
    def error_message(player, values):
        if not player.is_human:
            return 'You did not solve the captcha.'

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        print('upcoming_apps is', upcoming_apps[0],upcoming_apps[1],upcoming_apps[2],upcoming_apps[3])
        if player.treatnumber == 1:
            return 'DWK_baseline'
        elif player.treatnumber == 2:
            return 'DWK_cheap'
        elif player.treatnumber == 3:
            return 'DWK_increasedloss'
        elif player.treatnumber == 4:
            return 'DWK_likelyloss'





page_sequence = [
    Welcome
]
