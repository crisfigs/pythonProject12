from otree.api import *

import random
class C(BaseConstants):
    NAME_IN_URL = 'video'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    link1 = "https://www.dropbox.com/scl/fi/frjwsn6jex5jmkmy20sga/gemma.MOV?rlkey=1epeintyq89v47zx7qm90v3qp&raw=1"


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass



class Player(BasePlayer):
    prolific_id = models.StringField()
    sum_correct = models.IntegerField()
    number = models.IntegerField()
    task1 = models.StringField(blank=True)
    treatment = models.CharField(initial='video1')
    openq = models.LongStringField(label="Explain in the space below other thoughts and feelings associated to watching the video ")
    def make_field(label):
        return models.IntegerField(
            choices=[1, 2, 3, 4, 5],
            label=label,
            widget=widgets.RadioSelect,
        )
    def make_field2agree(label):
        return models.IntegerField(
            choices=[0, 0, 1, 2],
            label=label,
            widget=widgets.RadioSelect,
        )
    def make_field2disagree(label):
        return models.IntegerField(
            choices=[2, 1, 0, 0],
            label=label,
            widget=widgets.RadioSelect,
        )
    def make_field3(label):
        return models.IntegerField(
            choices=[
                [0, 'False'],
                [1, 'True']],
            label=label,
            widget=widgets.RadioSelect,
        )
    happy1 = make_field(label="Happy")
    sad1 = make_field(label="Sad")
    fear1 = make_field(label="Fear")
    disgust1 = make_field(label="Disgust")
    anger1 = make_field(label="Anger")
    compassion1 = make_field(label="Compassion")
    guilt1 = make_field(label="Guilt")
    boredom1 = make_field(label="Boredom")
    happy2 = make_field(label="Happy")
    sad2 = make_field(label="Sad")
    fear2 = make_field(label="Fear")
    disgust2 = make_field(label="Disgust")
    anger2 = make_field(label="Anger")
    compassion2 = make_field(label="Compassion")
    guilt2 = make_field(label="Guilt")
    boredom2 = make_field(label="Boredom")

    ##Attention questions video
    controlq1 = make_field3(label="... a woman called Gemma who introduced herself as the Head of Fundraising at Save the Children.")
    controlq2 = make_field3(label="...the staff member stating that children 'should never die from preventable causes.'")
    controlq3 = models.IntegerField(
            choices=[
                [1, 'False'],
                [0, 'True']],
            label="...children playing and smiling.",
            widget=widgets.RadioSelect)


    qemp1 = make_field2agree(label="I can easily tell if someone else wants to enter a conversation.")
    qemp3 = make_field2agree(label="I really enjoy caring for other people.")
    qemp4 = make_field2disagree(label="I find it hard to know what to do in a social situation.")
    qemp8 = make_field2disagree(label="I often find it difficult to judge if something is rude or polite.")
    qemp9 = make_field2disagree(
        label="In a conversation, I tend to focus on my own thoughts rather than on what my listener might be thinking.")
    qemp11 = make_field2agree(label="I can pick up quickly if someone says one thing but means another.")
    qemp12 = make_field2disagree(label="It is hard for me to see why some things upset people so much.")
    qemp13 = make_field2agree(label="I find it easy to put myself in somebody else’s shoes.")
    qemp14 = make_field2agree(label="I am good at predicting how someone will feel.")
    qemp15 = make_field2agree(label="I am quick to spot when someone in a group is feeling awkward or uncomfortable.")
    qemp18 = make_field2disagree(label="I can’t always see why someone should have felt offended by a remark.")
    qemp21 = make_field2agree(label="I don’t tend to find social situations confusing.")
    qemp22 = make_field2agree(
        label="Other people tell me I am good at understanding how they are feeling and what they are thinking.")
    qemp26 = make_field2agree(label="I can easily tell if someone else is interested or bored with what I am saying.")
    qemp28 = make_field2agree(
        label="Friends usually talk to me about their problems as they say that I am very understanding.")
    qemp29 = make_field2agree(label="I can sense if I am intruding, even if the other person doesn’t tell me.")
    qemp31 = make_field2disagree(label="Other people often say that I am insensitive, though I don’t always see why.")
    qemp34 = make_field2agree(label="I can tune into how someone else feels rapidly and intuitively.")
    qemp35 = make_field2agree(label="I can easily work out what another person might want to talk about.")
    qemp36 = make_field2agree(label="I can tell if someone is masking their true emotion.")
    qemp38 = make_field2agree(label="I am good at predicting what someone will do.")
    qemp39 = make_field2agree(label="I tend to get emotionally involved with a friend’s problems.")


    q_feedback = models.LongStringField(label="This is the end of the survey. "
                                            "In case you have comments, please leave them here.",
                                      blank=True)
    q_feedback_pilot = models.LongStringField(label="If you found any instructions unclear or confusing, please let us know here.",
                                            blank=True)
    donationq = models.IntegerField(label="Are you already a donor for Save the Children?", choices = [[1,"Yes"],[0,"No"]])
    donationqother = models.IntegerField(label="Are you already a donor for any other charity?", choices=[[1, "Yes"], [0, "No"]])
    charityq = models.IntegerField(label="Do you think Save the Children is a charity worth donating?", choices=[1, 2, 3, 4,5],widget=widgets.RadioSelectHorizontal)






class Welcome(Page):
    form_model = 'player'
    form_fields = ['prolific_id']

    @staticmethod
    def before_next_page(player, timeout_happened):
        import random
        player.number = random.choices([1,0], weights=(1, 100), k=1)[0]



class Desc(Page):
    form_model = 'player'

class Attention1(Page):
    form_model = 'player'
    form_fields = ["controlq1", "controlq2","controlq3"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.sum_correct = player.controlq1 + player.controlq2 + player.controlq3

class FailedAttention(Page):
        form_model = 'player'
        form_fields = ["controlq_cake", "controlq_flute","controlq_airplane"]

        @staticmethod
        def is_displayed(player: Player):
            return player.sum_correct <= 2 and player.number==1


        def js_vars(player):
            error_code = player.session.config["error_code"]
            link = "https://app.prolific.co/submissions/complete?cc=" + str(error_code)
            return dict(
                errorlink=link
                 )
        pass

class survey1(Page):
    form_model = 'player'

    def get_form_fields(player):
        e = ["happy1","sad1", "fear1", "disgust1","anger1", "compassion1", "guilt1", "boredom1"]
        random.shuffle(e)
        return e

class Video_alert(Page):
    pass

class Video(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        link = C.link1
        return dict(
            link = link
         )



class Video2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment == 0

class survey2(Page):
    form_model = 'player'

    def get_form_fields(player):
        e = ["happy2","sad2", "fear2", "disgust2","anger2", "compassion2", "guilt2", "boredom2"]
        random.shuffle(e)
        return e

class Openq(Page):
    form_model = 'player'
    form_fields = ['openq']

class Hypo_choice(Page):
    form_model = 'player'
    form_fields = ['task1']

class Hypo_choiceq(Page):
    form_model = 'player'
    form_fields = ['donationq','donationqother','charityq']

class EQ(Page):
    form_model='player'
    form_fields = ["qemp1", "qemp3", "qemp4","qemp8",
                   "qemp9" , "qemp11", "qemp12","qemp13",
                   "qemp14","qemp15","qemp18","qemp21", "qemp22",
                   "qemp26", "qemp28", "qemp29", "qemp31", "qemp34",
                    "qemp35", "qemp36", "qemp38", "qemp39"]

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

    pass


page_sequence = [Welcome, Desc, survey1, Video_alert, Video, survey2, Openq, Attention1, FailedAttention, Hypo_choice, Hypo_choiceq, EQ, Feedback, Back]
