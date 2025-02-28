from otree.api import *
import random
# RECAPTCHA
import requests
from otree.settings import RECAPTCHA_SECRET_KEY, RECAPTCHA_SITE_KEY

class C(BaseConstants):
    NAME_IN_URL = 'Dana'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TREATMENTS = ['DWK_baseline', 'DWK_cheap', 'DWK_increasedloss', 'DWK_likelyloss']

    participation_fee = 2 # in pounds



class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
        pass

class Player(BasePlayer):
    prolific_id = models.StringField()
    is_human = models.BooleanField(initial=False)
    assigned_treatment = models.StringField()
    role_ = models.StringField()

# Function to balance role assignment across treatments
def creating_session(subsession: Subsession):
    players = subsession.get_players()

    # Track role counts within each treatment
    treatment_counts = {t: {'dictators': 0, 'receivers': 0} for t in C.TREATMENTS}

    for p in players:
        if p.field_maybe_none('assigned_treatment') is None:
            p.assigned_treatment = random.choices(C.TREATMENTS, weights=(1,0,0,0), k=1)[0]

        # Get current counts for this player's treatment
        counts = treatment_counts[p.assigned_treatment]

        if p.field_maybe_none('role_') is None:
            # Assign role to balance within the treatment
            if counts['dictators'] < counts['receivers']:
                p.role_ = 'dictator'
                counts['dictators'] += 1
            else:
                p.role_ = 'receiver'
                counts['receivers'] += 1
            # Store the role in participant.vars for access across apps
            p.participant.vars['role_'] = p.role_
def recaptcha_valid(response_token):
    res = requests.post("https://www.google.com/recaptcha/api/siteverify", data={
        'secret': RECAPTCHA_SECRET_KEY,
        'response': response_token
    })
    return res.json()["success"]

# Creating session without `self`
#def creating_session(subsession: Subsession):
 #   players = subsession.get_players()
  #  random.shuffle(players)

   # group_matrix = [players[i:i + 2] for i in range(0, len(players), 2)]
    #subsession.set_group_matrix(group_matrix)

    #for group in subsession.get_groups():
     #   treatment = random.choice(C.TREATMENTS)
      #  for p in group.get_players():
       #     p.assigned_treatment = treatment  # Only store the string treatment


class Welcome(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        return {
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
    def app_after_this_page(player: Player, upcoming_apps):
        return player.assigned_treatment  # Redirect to assigned treatment app

    #@staticmethod
    #def app_after_this_page(player, upcoming_apps):
     #   print('upcoming_apps is', upcoming_apps[0],upcoming_apps[1],upcoming_apps[2],upcoming_apps[3])
      #  if player.treatnumber == 1:
       #     return 'DWK_baseline'
       # elif player.treatnumber == 2:
        #    return 'DWK_cheap'
        #elif player.treatnumber == 3:
         #   return 'DWK_increasedloss'
        #elif player.treatnumber == 4:
         #   return 'DWK_likelyloss'





page_sequence = [
    Welcome
]
