from otree.api import *

import random
class C(BaseConstants):
    NAME_IN_URL = 'Survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass



class Player(BasePlayer):
    prolific_id = models.StringField()
    treatnumber = models.IntegerField()

    #Survey for Vignettes 1-5:
    #Supply of mentoring and pool of suppliers composition
    signups = models.IntegerField(label="1. How many professors out of 100 do you think would sign up for this program? (Please enter a number between 0 and 100)", min=0, max=100)
    #signups and intentions for vignettes 1-7
    signups_good = models.IntegerField(label="2. How many professors out of 100 do you think will sign up with the sole intention to mentor students? (Please enter a number between 0 and 100)", min=0, max=100)
    signups_bad = models.IntegerField(label="3. How many professors out of 100 do you think will sign up with other intentions? (Please enter a number between 0 and 100)", min=0, max=100)
    other_intentions = models.LongStringField(label="4. Could you provide two or more examples of those other intentions?")

    # Appropriateness
    #How appropriate do you think it is for a professor to sign up to this program?
    appropriateness1 = models.IntegerField(label="5. How appropriate do you think it is for a professor to sign up to this program?",
                                        choices=[
                                            ("1", "Absolutely inappropriate"),
                                            ("2", "Inappropriate"),
                                            ("3", "Slightly inappropriate"),
                                            ("4", "Neutral"),
                                            ("5", "Slightly appropriate"),
                                            ("6", "Appropriate"),
                                            ("7", "Absolutely appropriate")
                                        ], widget=widgets.RadioSelect)
    appropriateness2 = models.IntegerField(label="2. Do you think the professor's choice of mentee was appropriate?",
                                        choices=[
                                            ("1", "Absolutely inappropriate"),
                                            ("2", "Inappropriate"),
                                            ("3", "Slightly inappropriate"),
                                            ("4", "Neutral"),
                                            ("5", "Slightly appropriate"),
                                            ("6", "Appropriate"),
                                            ("7", "Absolutely appropriate")
                                        ], widget=widgets.RadioSelect)
    # What other people think about sign up, intentions and appropriateness,


    signups_bad_others = models.IntegerField(label="6. Which do you think was the most common answer given by other respondents to the question: “How many professors out of 100 do you think will sign up with other intentions? (Please enter a number between 0 and 100)”?  You will get an extra 15 cents if your answer is +/- 10 of the average number given by the respondents of this survey.", min=0, max=100)
    other_intentions_others = models.LongStringField(label = "7. Which do you think were the two most common answers given by other participants in this survey to the question: “Could you provide two or more examples of those other intentions?” You will get an extra 10 cents per answer that matches the one of most common answers given by other participants (thus you can earn a maximum of 20 cents).")
    appropriateness1_others = models.IntegerField(label = "8. How many participants in this survey, out of 100, do you believe consider the professor's decision to sign up to be appropriate? (Please provide a number between 0 and 100) You will get an extra 15 cents if your answer is +/- 10 of the actual number of participants in 100 that consider the professor's decision to be appropriate.", min=0, max=100)
    appropriateness2_others = models.IntegerField(label = "4. How many people, out of 100, do you believe consider the professor's choice of mentee to be appropriate? (Please provide a number between 0 and 100) You will get an extra 20 cents if your answer is +/- 10 of the actual number of respondents in 100 that consider the professor's decision to be appropriate.")

    #Vignettes 1- 5 and 9 - 10
    #To check for imbalance in beliefs about likelihood of false accusations, I assume these are correlated with the professors beliefs.
    accusations_freq = models.IntegerField(label="9. Think about false accusations: a student falsely accusing the professor of things like harassment or inappropriate behaviour, for example. How frequently do you think false accusations happen in the situation described?",
                                           choices=[
                                               ("1", "Never"),
                                               ("2", "Very Rarely"),
                                               ("3", "Rarely"),
                                               ("4", "Occasionally"),
                                               ("5", "Frequently"),
                                               ("6", "Very Frequently"),
                                           ], widget=widgets.RadioSelect)
    accusations_consequences = models.IntegerField(label="10. For someone who is accused, how severe do you believe the consequences will be?",
                                                   choices = [
                                                       ("1", "Not severe at all"),
                                                       ("2", "Slightly severe"),
                                                       ("3", "Moderately severe"),
                                                       ("4", "Very severe"),
                                                       ("5", "Extremely severe")
                                                   ], widget = widgets.RadioSelect)


    #Vignette5: For the Zero Tolerance Policy to see what it signals (high past incidence and thus bad pool, high/low risk…
    ZTP_justification = models.LongStringField(label = "11. Why do you think the Zero Tolerance Policy is at place?")


    # Survey for Vignette 6-10:
    #What you think about motivations and appropriateness
    reasons_choice = models.LongStringField(label="1. Could you state three reasons why you think the professor chose that student?")
    #Same var as before Appropriateness Do you think the professor's choice was appropriate?

    #What other people think about intentions and appropriateness, Krupka Weber incentivized
    reasons_choice_others = models.LongStringField(label="3. Which do you think were the three most common answers from other respondents to the question: “Could you state three reasons why you think the professor chose that student?” You will get an extra 10 cents per answer that matches each of the most common answers given by other participants (thus you can earn a maximum of 30 cents). ")
  	#Same var as before Appropriateness_others "How many people, out of 100, do you believe consider the professor's decision to be appropriate? (Please provide a number between 0 and 100)"

    #Page Emotions
    #Please rate how intense you feel the following emotions
    # when considering the mentorship program
    def make_field(label):
        return models.IntegerField(
            choices=[1, 2, 3, 4, 5],
            label=label,
            widget=widgets.RadioSelect,
        )
    happy = make_field(label="Happiness")
    sad = make_field(label="Sadness")
    fear = make_field(label="Fear")
    disgust = make_field(label="Disgust")
    anger = make_field(label="Anger")
    compassion = make_field(label="Compassion")
    guilt = make_field(label="Guilt")
    boredom = make_field(label="Boredom")
    hope = make_field(label="Hope")

    #Feedback Page
    q_feedback = models.LongStringField(label="This is the end of the survey. "
                                            "In case you have comments, please leave them here.",
                                      blank=True)
    q_feedback_pilot = models.LongStringField(label="If you found any instructions unclear or confusing, please let us know here.",
                                            blank=True)


class Welcome(Page):
    form_model = 'player'
    form_fields = ['prolific_id']


    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.treatnumber = random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11], weights=(1/11,1/11,1/11,1/11,1/11,1/11,1/11,1/11,1/11,1/11,1/11), k=1)[0]

class Questions_(Page):
    form_model = 'player'
    form_fields = []
    def get_form_fields(player):
            if player.treatnumber in [1, 2, 3, 4]:#No choice vignettes
                return ["signups", "signups_good", "signups_bad", "other_intentions", "appropriateness1",
                        "signups_bad_others", "other_intentions_others", "appropriateness1_others",
                        "accusations_freq", "accusations_consequences"]
            elif player.treatnumber == 5 : #No choice ZTP vignette
                return ["signups", "signups_good", "signups_bad", "other_intentions", "appropriateness1",
                        "signups_bad_others", "other_intentions_others", "appropriateness1_others",
                        "accusations_freq", "accusations_consequences", "ZTP_justification"]
            elif player.treatnumber in [6,7,8]: #Choice attractiveness vignette
                return ["reasons_choice" , "appropriateness2", "reasons_choice_others" , "appropriateness2_others" ]
            elif player.treatnumber in [9,10,11]: #Simple Choice vignettes
                return ["reasons_choice" , "appropriateness2", "reasons_choice_others" , "appropriateness2_others",
                        "accusations_freq", "accusations_consequences"]



class Emotions(Page):
    form_model = 'player'
    def get_form_fields(player):
        e = ["happy","sad", "fear", "disgust","anger", "compassion", "guilt", "hope", "boredom"]
        random.shuffle(e)
        return e


class Feedback(Page):
    form_model = 'player'
    form_fields = ['q_feedback', 'q_feedback_pilot']

class Back(Page):
    form_model = 'player'
    form_fields = []

    def js_vars(player):
        cc_code = player.session.config["cc_code"]
        link = "https://app.prolific.co/submissions/complete?cc=" + str(cc_code)
        return dict(
            completionlink=link
        )

page_sequence = [Welcome,  Questions_, Emotions, Feedback, Back]
