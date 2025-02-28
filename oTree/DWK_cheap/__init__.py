from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'Dana_cheap_fairness'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Payoffs
    dictator_A = 70
    dictator_B = 60
    receiver_scenario1A = 10
    receiver_scenario2A = 60
    receiver_scenario1B = 60
    receiver_scenario2B = 10
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
    honeypot = models.StringField(blank=True)  # Hidden input field


    #Final Questions
    q_dictator = models.LongStringField(label="Did you reveal the payoffs of Player Y?")
    q_dictator_why = models.LongStringField(label="could you explain to us why?")
    q_receiver_perception = models.LongStringField(label="Do you think all Player Xs wanted to know PlayerY's payoff?")
    q_receiver_reasoning = models.LongStringField(label="If Player X did not want to know Player Y's payoff, what do you think was the reason?")
    motivation = models.StringField(
        choices=[
            "I was mainly concerned about how I would feel about myself and my decision",
            "I was mainly concerned about the actual outcomes and payoffs",
            "I was curious",
            "None of the above"
        ] ,  widget=widgets.RadioSelect,
    )
    motivation_receiver = models.StringField(
        choices=[
            "Player X was mainly concerned about how he/she would feel about him/herself and his/her decision",
            "Player X  was mainly concerned about the actual outcomes and payoffs",
            "Player X was mainly curious",
            "None of the above"
        ] ,  widget=widgets.RadioSelect,
    )


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
                                         ('0', '10 points'),
                                         ('1', ' 60 or 10 points, depending on the game selected by the computer')],
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

    #PlayerYTask
    treatgendermentor = models.BooleanField(blank=True)  # whether male gender or female gender of professors in PlayerTaskY.
    treatlocation = models.BooleanField(blank=True)  # whether pub or cafe is displayed first in PlayerTaskY.
    treatgendermentee = models.BooleanField(blank=True)  # whether male or female question is displayed always first or second in PlayerTaskY.

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
            blank=True
        )

    appropriateness_pub_MM = appropriateness_field(label="...a male student")
    appropriateness_pub_MF = appropriateness_field(label="...a female student")
    appropriateness_cafe_MM = appropriateness_field(label="...a male student")
    appropriateness_cafe_MF = appropriateness_field(label="...a female student")
    appropriateness_pub_FM = appropriateness_field(label="...a male student")
    appropriateness_pub_FF = appropriateness_field(label="...a female student")
    appropriateness_cafe_FM = appropriateness_field(label="...a male student")
    appropriateness_cafe_FF = appropriateness_field(label="...a female student")

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

    def set_payoffs(player):
        if player.task1 == "A" and player.participant.vars["role_"] == "dictator":
            player.bonus_payoff = f"{0.02 * C.dictator_A:.2f}"
            #if player.scenario1 == 1:
             #   p2.bonus_payoff = f"{0.02 * C.receiver_scenario1A:.2f}"
            #else:
             #   p2.bonus_payoff = f"{0.02 * C.receiver_scenario2A:.2f}"
        elif player.task1 == "B" and player.participant.vars["role_"] == "dictator":
            player.bonus_payoff = f"{0.02 * C.dictator_B:.2f}"
            #if p1.scenario1:
               # p2.bonus_payoff = f"{0.02 * C.receiver_scenario1B:.2f}"
            #else:
                #p2.bonus_payoff = f"{0.02 * C.receiver_scenario2B:.2f}"




class Consent(Page):
    form_model = 'player'
    form_fields = ['prolific_id','honeypot']
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
    def vars_for_template(player):
        return {
            "role_": player.participant.vars['role_']
        }

class Task1(Page):
    form_model = 'player'
    form_fields = ['reveal']

    def is_displayed(player):
        return player.participant.vars['role_'] == "dictator"
    def before_next_page(player, timeout_happened):
        player.treatgendermentor = random.choice([True, False])
        player.treatgendermentee = random.choice([True, False])
        player.treatlocation = random.choice([True, False])




class Task1Reveal(Page):
    form_model = 'player'
    form_fields = ['task1']

    def is_displayed(player):
        return player.participant.vars['role_'] == "dictator" and player.reveal == 1
    def before_next_page(player, timeout_happened):
        return player.set_payoffs()



class Task1NoReveal(Page):
    form_model = 'player'
    form_fields = ['task1']
    def is_displayed(player):
      return player.participant.vars['role_'] == "dictator" and player.reveal == 0

    def before_next_page(player, timeout_happened):
        return player.set_payoffs()



class Questions(Page):
    form_model = 'player'
    form_fields = ['q_receiver_scenario1', 'q_receiver_scenario2']
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.vars['role_'] == "receiver"
    def before_next_page(player, timeout_happened):
        player.treatgendermentor = random.choice([True, False])
        player.treatgendermentee = random.choice([True, False])
        player.treatlocation = random.choice([True, False])


class PlayerYTask(Page):
    form_model = 'player'
    form_fields = ['appropriateness_pub_MM','appropriateness_pub_MF','appropriateness_cafe_MM','appropriateness_cafe_MF',
                   'appropriateness_pub_FM','appropriateness_pub_FF','appropriateness_cafe_FM','appropriateness_cafe_FF']
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.vars['role_'] == "receiver"

    def error_message(player, values):
        if player.treatgendermentor:
            required_fields = [
                'appropriateness_pub_MM', 'appropriateness_pub_MF',
                'appropriateness_cafe_MM', 'appropriateness_cafe_MF'
            ]
        else:
            required_fields = [
                'appropriateness_pub_FM', 'appropriateness_pub_FF',
                'appropriateness_cafe_FM', 'appropriateness_cafe_FF'
            ]

        if any(values[field] is None or values[field] == '' for field in required_fields):
            return "All required fields must be filled."

class FinalQuestions(Page):
        form_model = 'player'

        def get_form_fields(player):
            if player.participant.vars['role_'] == "dictator":
                return ['q_dictator_why', 'motivation']  #
            else:
                return ['q_receiver_perception', 'q_receiver_reasoning', 'motivation_receiver']

        def vars_for_template(player):
            is_dictator = player.participant.vars["role_"] == "dictator"

            return {
                "role_": player.participant.vars['role_'],
                "reveal": player.reveal if is_dictator else None
            }


class PlayerXTask(Page):
    form_model = 'player'
    form_fields = ['appropriateness_pub_MM', 'appropriateness_pub_MF', 'appropriateness_cafe_MM',
                   'appropriateness_cafe_MF',
                   'appropriateness_pub_FM', 'appropriateness_pub_FF', 'appropriateness_cafe_FM',
                   'appropriateness_cafe_FF']

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.vars['role_'] == "dictator"

    def error_message(player, values):
        if player.treatgendermentor:
            required_fields = [
                'appropriateness_pub_MM', 'appropriateness_pub_MF',
                'appropriateness_cafe_MM', 'appropriateness_cafe_MF'
            ]
        else:
            required_fields = [
                'appropriateness_pub_FM', 'appropriateness_pub_FF',
                'appropriateness_cafe_FM', 'appropriateness_cafe_FF'
            ]

        if any(values[field] is None or values[field] == '' for field in required_fields):
            return "All required fields must be filled."


class SummaryTask1(Page):
    form_model = 'player'

    def vars_for_template(player):
        is_dictator = player.participant.vars["role_"] == "dictator"

        return {
            "p1_task1": player.task1 if is_dictator else None,
            "p1_bonus": f"{float(player.bonus_payoff)} pounds" if is_dictator else None,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.vars['role_'] == "dictator"


class SummaryTask2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.vars['role_'] == "receiver"



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
    FinalQuestions,
    PlayerXTask,
    SummaryTask1,
    SummaryTask2
]