from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'Dana_increased_loss'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    # Payoffs
    dictator_A = 100
    dictator_B = 60
    receiver_scenario1A = -20
    receiver_scenario2A = 60
    receiver_scenario1B = 60
    receiver_scenario2B = -20
    participation_fee = 2  # in pounds


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
        pass

class Player(BasePlayer):
    prolific_id = models.StringField()
    reveal = models.IntegerField(blank=True)  # whether participant decides to reveal information in Dana task
    task1 = models.StringField(blank=True)  # whether participant takes selfish choice in Dana task
    scenario1 = models.BooleanField(blank=True)  # whether scenario 1 or 2 will be displayed
    bonus_payoff = models.StringField(blank=True)
    treatgender = models.BooleanField(blank=True)  # whether male gender or female gender of professors in PlayerTaskY.
    treatlocation = models.BooleanField(blank=True)  # whether pub or cafe is displayed first in PlayerTaskY.

    # Comprehension questions
    qXB = models.IntegerField(label="Player X receives:")
    qYB = models.IntegerField(label="Player Y receives:")
    qXA = models.IntegerField(label="Player X receives:")
    qYA = models.IntegerField(label="Player Y receives:")
    q_control1 = models.IntegerField(widget=widgets.RadioSelect,
                                     choices=[
                                         ('1', 'A'),
                                         ('0', 'B')],
                                     label="Which option gives Player X his or her highest payment in both games?")

    q_control2 = models.IntegerField(widget=widgets.RadioSelect,
                                     choices=[
                                         ('0', '60 points'),
                                         ('0', '-20 points'),
                                         ('1', ' 60 or -20 points')],
                                     label="If Player X chooses B, then Player Y receives")
    q_receiver_scenario1 = models.IntegerField(widget=widgets.RadioSelect,
                                     choices=[
                                         ('1', 'A'),
                                         ('0', 'B')],
                                     label="In the game on the left, I would choose:")

    q_receiver_scenario2 = models.IntegerField(widget=widgets.RadioSelect,
                                     choices=[
                                         ('1', 'A'),
                                         ('0', 'B')],
                                     label="In the game on the right, I would choose:")

    ####PlayerYTask
    def appropriateness_field(label):
        return models.IntegerField(
            choices=[
                (1, 'Highly inappropriate'),
                (2, 'Somewhat inappropriate'),
                (3, 'Neutral'),
                (4, 'Somewhat appropriate'),
                (5, 'Highly appropriate'),
            ],
            label=label,
            widget=widgets.RadioSelectHorizontal,
            blank=True
        )

    appropriateness_pub_MM = appropriateness_field(label="The professor chooses to mentor a male student")
    appropriateness_pub_MF = appropriateness_field(label="The professor chooses to mentor a female student")
    appropriateness_cafe_MM = appropriateness_field(label="The professor chooses to mentor a male student")
    appropriateness_cafe_MF = appropriateness_field(label="The professor chooses to mentor a female student")
    appropriateness_pub_FM = appropriateness_field(label="The professor chooses to mentor a male student")
    appropriateness_pub_FF = appropriateness_field(label="The professor chooses to mentor a female student")
    appropriateness_cafe_FM = appropriateness_field(label="The professor chooses to mentor a male student")
    appropriateness_cafe_FF = appropriateness_field(label="The professor chooses to mentor a female student")


  ###FUNCTIONS
    def set_error_message(player, value):
        correct_answers = {
                        'qXB': 3,
                        'qYB': 4,
                        'qXA': 1,
                        'qYA': 2}
        list_answers = list(value.items())[0:]
        list_correct_answers = list(correct_answers.items())
        if list_answers != list_correct_answers:
            Text = 'You did not answer all questions correctly. Please go back to the instructions and revise your answers.'
            return Text

    def set_error_message2(player, value):
        correct_answers = {
                        'q_control1': 1,
                        'q_control2': 1}
        list_answers = list(value.items())[0:]
        list_correct_answers = list(correct_answers.items())
        if list_answers != list_correct_answers:
            Text = 'You did not answer all questions correctly. Please go back to the instructions and revise your answers.'
            return Text


def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    if p1.task1 == "A":
        p1.payoff = str(C.participation_fee + 0.1 * C.dictator_A) + "0"
        p1.bonus_payoff = str(0.1 * C.dictator_A) + "0"
        if p1.scenario1 == 1:
            p2.payoff = str(C.participation_fee + 0.1 * C.receiver_scenario1A) + "0"
            p2.bonus_payoff = str(0.1 * C.receiver_scenario1A) + "0"
        else:
            p2.payoff = str(C.participation_fee + 0.1 * C.receiver_scenario2A) + "0"
            p2.bonus_payoff = str(0.1 * C.receiver_scenario2A) + "0"

    elif p1.task1 == "B":
        p1.payoff = str(C.participation_fee + 0.1 * C.dictator_B) + "0"
        p1.bonus_payoff = str(0.1 * C.dictator_B) + "0"

        if p1.scenario1:
            p2.payoff = str(C.participation_fee + 0.1 * C.receiver_scenario1B) + "0"
            p2.bonus_payoff = str(0.1 * C.receiver_scenario1B) + "0"
        else:
            p2.payoff =  str(C.participation_fee  + 0.1 * C.receiver_scenario2B) + "0"
            p2.bonus_payoff = str(0.1 * C.receiver_scenario2B) + "0"

class Consent(Page):
    form_model = 'player'
    form_fields = ['prolific_id']
    def before_next_page(player, timeout_happened):
        player.scenario1 = random.choice([True, False])


class InstructionsTask1(Page):
    form_model = 'player'
    form_fields = ['qXA', 'qYA', 'qXB', 'qYB' ]

    def error_message(player, value):
        return player.set_error_message(value)

class Instructions2Task1(Page):
    form_model = 'player'
    form_fields = ['q_control1', 'q_control2']
    def error_message(player, value):
        return player.set_error_message2(value)

class SummaryInstructionsTask1(Page):
    form_model = 'player'

class Role(Page):
    form_model = 'player'

class Task1(Page):
    form_model = 'player'
    form_fields = ['reveal']

    def is_displayed(player):
        return player.id_in_group == 1



class Task1Reveal(Page):
    form_model = 'player'
    form_fields = ['task1']

    def is_displayed(player):
        return player.id_in_group == 1 and player.reveal == 1



class Task1NoReveal(Page):
    form_model = 'player'
    form_fields = ['task1']
    def is_displayed(player):
      return player.id_in_group == 1 and player.reveal == 0


class Questions(Page):
    form_model = 'player'
    form_fields = ['q_receiver_scenario1', 'q_receiver_scenario2']
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2
    def before_next_page(player, timeout_happened):
        player.treatgender = random.choice([True, False])
        player.treatlocation = random.choice([True, False])


class PlayerYTask(Page):
    form_model = 'player'
    form_fields = ['appropriateness_pub_MM','appropriateness_pub_MF','appropriateness_cafe_MM','appropriateness_cafe_MF',
                   'appropriateness_pub_FM','appropriateness_pub_FF','appropriateness_cafe_FM','appropriateness_cafe_FF']
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

class SummaryTask1(Page):
    form_model = 'player'

    def vars_for_template(player):
        return {"p1_payoff":  f"{float(player.group.get_player_by_id(1).payoff)} euros",
                "p2_payoff": f"{float(player.group.get_player_by_id(2).payoff)} euros",
                "p1_task1": player.group.get_player_by_id(1).task1,
                "p1_bonus": f"{float(player.group.get_player_by_id(1).bonus_payoff)} euros",
                "p2_bonus": f"{float(player.group.get_player_by_id(2).bonus_payoff)} euros"
               }



page_sequence = [

    Consent,
    InstructionsTask1,
    Instructions2Task1,
    SummaryInstructionsTask1,
    Role,
    Task1,
    Task1Reveal,
    Task1NoReveal,
    Questions,
    PlayerYTask,
    ResultsWaitPage,
    SummaryTask1
]
