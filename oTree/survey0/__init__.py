from otree.api import *

import random
class C(BaseConstants):
    NAME_IN_URL = 'video'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass



class Player(BasePlayer):
    prolific_id = models.StringField()
    treatnumber = models.IntegerField()


    #How appropriate each situation is
    #1 – Absolutely inappropriate 2 – Inappropriate 3 – Slightly inappropriate 4 – Neutral
    # 5 – Slightly appropriate 6 – Appropriate 7 – Absolutely appropriate
    approp_female = models.IntegerField(label="9. How appropriate do you think it is for a male professor to mentor a female student over a drink in a pub?",
                                        choices=[
                                            ("1", "Absolutely inappropriate"),
                                            ("2", "Inappropriate"),
                                            ("3", "Slightly inappropriate"),
                                            ("4", "Neutral"),
                                            ("5", "Slightly appropriate"),
                                            ("6", "Appropriate"),
                                            ("7", "Absolutely appropriate")
                                        ], widget=widgets.RadioSelect)

    approp_male = models.IntegerField(label="9. How appropriate do you think it is for a male professor to mentor a male student over a drink in a pub?",
                                      choices=[
                                          ("1", "Absolutely inappropriate"),
                                          ("2", "Inappropriate"),
                                          ("3", "Slightly inappropriate"),
                                          ("4", "Neutral"),
                                          ("5", "Slightly appropriate"),
                                          ("6", "Appropriate"),
                                          ("7", "Absolutely appropriate")
                                      ], widget=widgets.RadioSelect)

    #Opinion of other people when sees it
    opinion_female_others = models.LongStringField(label="What do you think other people think if they see an older male in a pub having a drink with a younger female?")
    opinion_male_others = models.LongStringField(label="What do you think other people think if they see an older male in a pub having a drink with a younger male?")

    #Opinion of the self  when sees it
    # opinion_female_self = models.LongStringField(label="What do you think if you see an older male in a pub having a drink with a younger female?")
    #opinion_male_self = models.LongStringField(label="What do you think if you see an older male in a pub having a drink with a younger male?")

    # Preferences for mentoring. Why are senior males more or less willing to mentor women
    #  opinion1 = models.LongStringField(label="There is evidence showing that senior males are less willing to mentor junior females than to mentor junior males. Why do you think this is so?")
    opinion2 = models.IntegerField(label="Who would you prefer mentoring?",
                                   choices=[[0, 'No one'],[1,'Female'], [2,'Indifferrent'],[3, 'Male'], ])
    opinion3 = models.LongStringField(label="Could you elaborate on your previous answer and explain why?")

    #Scenario questions
    #Distribution of good and bad types signing up to each scenario.
    mentor_q1_male =  models.IntegerField(label="2. How many professors out of 100 do you think will sign up with the intention to mentor male students? (Enter a number between 0 and 100)",
        min=0,
        max=100)
    mentor_q2 = models.IntegerField(label="3. How many professors out of 100 do you think will sign up with other intentions? (Enter a number between 0 and 100)",
        min=0,
        max=100)
    mentor_q3 = models.LongStringField(label="Could you provide three or more examples of those other intentions?")
    mentor_q1_female1 =  models.IntegerField(label="2. How many professors out of 100 do you think will sign up with the intention to mentor female students? (Enter a number between 0 and 100)",
        min=0,
        max=100)


    mentor_q1_female2 = models.IntegerField(label="2. How many professors out of 100 do you think will sign up with the intention to mentor female students? (Enter a number between 0 and 100)",
        min=0,
        max=100)


    #Opinion of the act of signing up and of the amount of people who think badly for each scenario
    opinion_malementor = models.LongStringField(label="4. What do you think other people will think if a professor signs up for this program?")
    #6: Definitely 5 Very Probably  4Probably •3Possibly 2Probably Not 1Definitely Not
    opinion_bad = models.IntegerField(label="5. Do you think other people might think that a professor signs up for this program with other intentions ?",
                                                 choices=[
                                                     ("1", "Definitely Not"),
                                                     ("2", "Probably Not"),
                                                     ("3", "Possibly"),
                                                     ("4", "Probably"),
                                                     ("5", "Very Probably"),
                                                     ("6", "Definitely")
                                                 ], widget=widgets.RadioSelect)
    opinion_femalementor1 = models.LongStringField(label="4. What do you think other people will think if a professor signs up for this program?")

    opinion_femalementor2 = models.LongStringField(label="4. What do you think other people will think if a professor signs up for this program?")


    #Intensity of concern of being identified as a bad type
    #1 – not at all concerned , 2 – Slightly concerned, 3 – Somewhat concerned, 4 – Moderately concerned, 5 – Extremely concerned
    identification_concern_male = models.IntegerField(label="6. Imagine you are a professor, to what degree would you be concerned about being perceived as someone who signs up to the mentoring meeting under 'other' intentions?",
                                                      choices=[
                                                          ("1", "Not at all concerned"),
                                                          ("2", "Slightly concerned"),
                                                          ("3", "Somewhat concerned"),
                                                          ("4", " Moderately concerned"),
                                                          ("5", "Extremely concerned")
                                                      ], widget=widgets.RadioSelect)
    identification_concern_female1 = models.IntegerField(label="6. Imagine you are a professor, to what degree would you be concerned about being perceived as someone who signs up to the mentoring meeting under 'other' intentions?",
                                                         choices=[
                                                             ("1", "Not at all concerned"),
                                                             ("2", "Slightly concerned"),
                                                             ("3", "Somewhat concerned"),
                                                             ("4", " Moderately concerned"),
                                                             ("5", "Extremely concerned")
                                                         ], widget=widgets.RadioSelect)
    identification_concern_female2 = models.IntegerField(label="6. Imagine you are a professor, to what degree would you be concerned about being perceived as someone who signs up to the mentoring meeting under 'other' intentions?",
                                                         choices=[
                                                             ("1", "Not at all concerned"),
                                                             ("2", "Slightly concerned"),
                                                             ("3", "Somewhat concerned"),
                                                             ("4", " Moderately concerned"),
                                                             ("5", "Extremely concerned")
                                                         ], widget=widgets.RadioSelect)

    #False accusations estimate
    accusations_freq = models.IntegerField(label="7. Think about false accusations: a student falsely accusing the professor of things like harrasment or inappropriate behaviour, for example. How frequent do you think false accusations are in the situation described?",
                                           choices=[
                                               ("1", "Never"),
                                               ("2", "Very Rarely"),
                                               ("3", "Rarely"),
                                               ("4", " Ocassionally"),
                                               ("5", "Frequently"),
                                               ("6", "Very Frequently"),
                                           ], widget=widgets.RadioSelect)
    accusations_concern = models.IntegerField(label="8. How concerned would you be regarding false accusations in the situation described?",
                                              choices=[
                                                  ("1", "Not at all concerned"),
                                                  ("2", "Slightly concerned"),
                                                  ("3", "Somewhat concerned"),
                                                  ("4", " Moderately concerned"),
                                                  ("5", "Extremely concerned")
                                              ], widget=widgets.RadioSelect)




    #signups
    signups_male = models.IntegerField(label="1. How many male professors out of 100 do you think would sign up for this program?", min=0,
        max=100)
    signups_female1 = models.IntegerField(label="1. How many male professors out of 100 do you think would sign up for this program?", min=0,
        max=100)
    signups_female2 = models.IntegerField(label="1. How many male professors out of 100 do you think would sign up for this program?", min=0,
        max=100)
    #Feedback questions
    q_feedback = models.LongStringField(label="This is the end of the survey. "
                                            "In case you have comments, please leave them here.",
                                      blank=True)
    q_feedback_pilot = models.LongStringField(label="If you found any instructions unclear or confusing, please let us know here.",
                                            blank=True)

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

class Welcome(Page):
    form_model = 'player'
    form_fields = ['prolific_id']
    #Randomize people into each survey.
    #@staticmethod
    #def app_after_this_page(player, upcoming_apps):
    #    print('upcoming_apps is', upcoming_apps[0],upcoming_apps[1],upcoming_apps[2],upcoming_apps[3])
    #    player.treatnumber = random.choices([1,2,3], weights=(0, 0, 1,), k=1)[0]
    #    if player.treatnumber == 1:
    #        return 'Scenario_'
    #    elif player.treatnumber == 2:
    #        return 'Scenario__'
    #    elif player.treatnumber == 3:
    #        return 'Scenario___'


    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.treatnumber = random.choices([1, 2, 3], weights=(1/3,1/3,1/3), k=1)[0]

#class Questions1_(Page):
    # form_model = 'player'
        # form_fields = ['approp_female','approp_male',
#    'opinion_female_others', 'opinion_male_others']

    #def get_form_fields(player):
     #   e = ["happy2","sad2", "fear2", "disgust2","anger2", "compassion2", "guilt2", "boredom2"]
      #  random.shuffle(e)
       # return e

class Questions2_(Page):
        form_model = 'player'
        form_fields = []
        def get_form_fields(player):
            if player.treatnumber == 1:
                return ['signups_male','mentor_q1_male','mentor_q2','mentor_q3','opinion_malementor', 'opinion_bad','identification_concern_male','accusations_freq', 'accusations_concern', 'approp_male']
            elif player.treatnumber == 2:
                return ['signups_female1','mentor_q1_female1','mentor_q2', 'mentor_q3','opinion_femalementor1', 'opinion_bad','identification_concern_female1','accusations_freq', 'accusations_concern','approp_female']
            elif player.treatnumber == 3:
                return ['signups_female2','mentor_q1_female2','mentor_q2','mentor_q3','opinion_femalementor2', 'opinion_bad', 'identification_concern_female2', 'accusations_freq', 'accusations_concern','approp_female']


class Emotions(Page):
    form_model = 'player'
    def get_form_fields(player):
        e = ["happy","sad", "fear", "disgust","anger", "compassion", "guilt", "boredom", "hope"]
        random.shuffle(e)
        return e

class Questions3_(Page):
    form_model = 'player'
    form_fields = ['opinion2','opinion3']

class Feedback(Page):
    form_model = 'player'
    form_fields = ['q_feedback', 'q_feedback_pilot']



page_sequence = [Welcome,  Questions2_, Emotions, Questions3_, Feedback]
