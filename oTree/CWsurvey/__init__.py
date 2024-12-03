from otree.api import *

import random
class C(BaseConstants):
    NAME_IN_URL = 'CWsurvey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    participation_fee = 2 # in pounds


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass



class Player(BasePlayer):
    prolific_id = models.StringField()
    treatnumber = models.IntegerField()
    sum_correct = models.IntegerField()
    number = models.IntegerField()

    # Allocations
    allocation_left = models.IntegerField(
        label="¿Cuánto desea asignar a la Fundación FAES?",
        min=0,
        max=100)
    allocation_right = models.IntegerField(
        label="¿Cuánto desea asignar a la Fundación AVANZA?",
        min=0,
        max=100)
    allocation_neutral = models.IntegerField(
        label="¿Cuánto desea asignar a la Fundación Española del Corazón?",
        min=0,
        max=100)
    #question on political spectrum perception

    agreement = models.IntegerField(label="1. ¿Qué tan de acuerdo está usted con la descripción de los eventos que aparece en el texto?",
                                       choices=[[1, 'Completamente en desacuerdo'],
                                          [2, 'En desacuerdo'],
                                          [3, 'Ni de acuerdo ni en desacuerdo'],
                                          [4, 'De acuerdo' ],
                                          [5, 'Completamente de acuerdo']], widget=widgets.RadioSelectHorizontal)

    ##Political preferences
    political_spectrum = models.IntegerField(label = '2. En política se habla normalmente de “izquierda” y “derecha”. En una escala donde “0” es izquierda y “10” la derecha, ¿dónde se ubicaría usted?',
                                             choices=[ [0, '0 \n Izquierda'],
                                                       [1, '1'],
                                                       [2, '2'],[3, '3'],[4, '4'], [5, '5'],[6, '6'],
                                                       [7, '7'], [8, '8'],[9, '9'],[10, '10 \n Derecha']], widget=widgets.RadioSelectHorizontal
                                             )
    vote2023 = models.StringField(
        label= "3. ¿Por cuál partido o coalición votó usted en las elecciones generales del 23 de julio de 2023?",
        choices=[
            "Partido Popular (PP)",
            "Partido Socialista Obrero Español (PSOE)",
            "Vox",
            "Sumar",
            "Otro",
            "Prefiero no responder",
            "No votó",
            "Voto en blanco"
        ])
    vote2023_otro = models.StringField(label = "4. Si seleccionó 'Otro', por favor especifique:", blank=True )


   ##Personal Experience
    familyside = models.IntegerField(label="2. Por lo que usted sabe o puede recordar, ¿con cuál de los dos bandos de la Guerra Civil simpatizaba más su familia?",
                                      choices = [
                                          [1, 'Con los nacionales'],
                                          [2, 'Con los republicanos'],
                                          [3, 'Unos con los nacionales y otros con los republicanos'],
                                          [4, 'Con ninguno de los dos' ],
                                          [5, 'No sabe']], widget=widgets.RadioSelect)

    transmission_school = models.IntegerField(label = "escuela")
    transmission_family = models.IntegerField(label = 'familia')
    transmission_media = models.IntegerField(label = 'medios de comunicación (libros, películas, prensa, etc.)' )
    transmission_other1 = models.IntegerField(label = 'otras fuentes')
    transmission_other2 = models.StringField(label = '', blank=True)

    memory = models.LongStringField(label="3. Por favor, recuerde cualquier historia(s) sobre la Guerra Civil o el Franquismo que haya sido compartida en su familia. Resúmala brevemente en unas pocas frases.")

    #Trust

    trust_army = models.IntegerField(label="Ejército",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_civilguard = models.IntegerField(label="Guardia Civil",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_church = models.IntegerField(label="Iglesia",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_constitutionalcourt= models.IntegerField(label="Tribunal Constitucional",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_ombudsman= models.IntegerField(label="Defensor del Pueblo",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_parliament= models.IntegerField(label="Parlamento",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)

    #Demographics
    province = models.StringField(
        label="6. ¿En qué provincia de España creció (dónde residía antes de los 16 años)? Seleccione su provincia de residencia o, si vivió la mayor parte de su vida antes de los 16 años fuera de España, elija la opción 'Fuera de España':",
        choices=[
            "Álava",
            "Albacete",
            "Alicante",
            "Almería",
            "Asturias",
            "Ávila",
            "Badajoz",
            "Barcelona",
            "Burgos",
            "Cáceres",
            "Cádiz",
            "Cantabria",
            "Castellón",
            "Ceuta",
            "Ciudad Real",
            "Córdoba",
            "Cuenca",
            "Girona",
            "Granada",
            "Guadalajara",
            "Guipúzcoa",
            "Huelva",
            "Huesca",
            "Islas Baleares",
            "Jaén",
            "La Coruña",
            "La Rioja",
            "Las Palmas",
            "León",
            "Lleida",
            "Lugo",
            "Madrid",
            "Málaga",
            "Melilla",
            "Murcia",
            "Navarra",
            "Ourense",
            "Palencia",
            "Pontevedra",
            "Salamanca",
            "Santa Cruz de Tenerife",
            "Segovia",
            "Sevilla",
            "Soria",
            "Tarragona",
            "Teruel",
            "Toledo",
            "Valencia",
            "Valladolid",
            "Vizcaya",
            "Zamora",
            "Zaragoza",
            "Fuera de España"
        ])
    income_level = models.StringField(
        label="5. Aproximadamente, ¿cuál es su nivel de ingresos mensuales (antes de impuestos)?",
        choices=[
            "Menos de 1.000 €",
            "Entre 1.000 € y 1.499 €",
            "Entre 1.500 € y 1.999 €",
            "Entre 2.000 € y 2.999 €",
            "Entre 3.000 € y 3.999 €",
            "Entre 4.000 € y 4.999 €",
            "Más de 5.000 €",
            "Prefiero no responder"
        ]
    )










    def make_field(label):
        return models.IntegerField(
            choices=[1, 2, 3, 4, 5],
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
    #Emotions
    ##Questions on emotions associated to the narrative (or should we ask about the CW and Francoism?)
    happy = make_field(label="Felicidad")
    sad = make_field(label="Tristeza")
    fear = make_field(label="Miedo")
    anger = make_field(label="Rabia")
    patriotism = make_field(label="Compasión")
    guilt = make_field(label="Culpa")
    uncomfortable = make_field(label="Incomodidad")
    indifference = make_field(label="Indiferencia")
    boredom = make_field(label="Aburrimiento")
    misunderstanding = make_field(label="Incomprensión")
    nostalgia = make_field(label="Nostalgia")
    pride = make_field(label="Orgullo")
    shame = make_field(label="Verguenza")
    surprise = make_field(label="Sorpresa")


    #Feedback questions
    q_feedback = models.LongStringField(label="Este es el final de la encuesta."
                                              "Si tiene comentarios, por favor déjelos aquí.",
                                        blank=True)
    q_feedback_pilot = models.LongStringField(
        label="Si encontró alguna instrucción poco clara o confusa, por favor háganoslo saber aquí.",
        blank=True)

    ##Attention questions
    controlq1_1 = models.IntegerField(
        label="¿Qué característica fue común en ambos bandos durante la Guerra Civil?",
        choices=[
            [1, 'Ambos participaron en actos de violencia y cometieron atrocidades'],
            [2, 'Un bando fue claramente más violento que el otro'],
            [3, 'Ninguno de los bandos tuvo responsabilidad en las atrocidades']
        ]
    )
    controlq1_2 = models.IntegerField(
        label="¿Qué enfoque adoptaron ambos bandos hacia sus oponentes durante la Guerra Civil?",
        choices=[

            [2, 'Solo uno de los bandos reprimió y purgó a sus oponentes'],
            [1, 'Ambos llevaron a cabo acciones represivas y purgas contra sus opositores'],
            [3, 'Ambos intentaron reconciliarse con sus opositores sin represalias']
        ]
    )

    controlq1_3 = models.IntegerField(label = "¿Qué tensiones políticas existían en España antes de la Guerra Civil?",
                                      choices=[
                                          [2, 'Falta de interés en la política'],
                                          [3, 'Concordia entre los distintos grupos políticos'],
                                          [1, 'División entre posiciones políticas, sociales y económicas opuestas']])

    controlq2_1 = make_field3(label="... ")
    controlq2_2 = make_field3(label="...")
    controlq2_3 = models.IntegerField(
        choices=[
            [1, 'False'],
            [0, 'True']],
        label="....",
        widget=widgets.RadioSelect)
    controlq3_1 = make_field3(label="... ")
    controlq3_2 = make_field3(label="...")
    controlq3_3 = models.IntegerField(
        choices=[
            [1, 'False'],
            [0, 'True']],
        label="....",
        widget=widgets.RadioSelect)


class Bienvenida(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        player.treatnumber = random.choices([1,2,3], weights=(1,0,0), k=1)[0]
        return {
            'treatnumber': player.treatnumber
        }


class Texto(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(player: Player):
      return player.treatnumber == 1

class Choice(Page):
    form_model = 'player'

    def vars_for_template(player: Player):
        descriptions = [
            {'name': 'Fundación FAES',
            'description': 'La Fundación FAES es un think tank liberal-conservador que promueve valores como la libertad, la economía de mercado y la unidad nacional. Defiende políticas públicas que refuercen la competitividad, el emprendimiento y el fortalecimiento de las instituciones en España.'},
            {'name': 'Fundación AVANZA',
            'description': 'Laboratorio de Ideas Avanza es un think tank progresista que fomenta el debate sobre los grandes retos sociales. Promueve valores como la democracia social, la igualdad y los derechos humanos, trabajando por una sociedad más inclusiva y justa.'},
            {'name': 'Fundación Española del Corazón',
            'description': 'La Fundación Española del Corazón es una organización apolítica dedicada a la salud cardiovascular. Busca mejorar la calidad de vida a través de la prevención de enfermedades, educación y campañas de concienciación.'},]
        random.shuffle(descriptions)
        return {'descriptions': descriptions}
    def get_form_fields(player):
        e = ['allocation_left', 'allocation_right', 'allocation_neutral']
        random.shuffle(e)
        return e

    def error_message(self, values):
        total = values['allocation_left'] + values['allocation_right'] + values['allocation_neutral']
        if total != 100:
            return "La suma de las asignaciones debe ser exactamente 100 euros."

class Atencion1(Page):
    form_model = 'player'
    form_fields = ["controlq1_1", "controlq1_2", "controlq1_3"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.sum_correct = player.controlq1_1 + player.controlq1_2 + player.controlq1_3
        player.number = random.choices([1,0], weights=(1, 99), k=1)[0]
    @staticmethod
    def is_displayed(player: Player):
      return player.treatnumber == 1

class Atencion2(Page):
    form_model = 'player'
    form_fields = ["controlq2_1", "controlq2_2","controlq2_3"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.sum_correct = player.controlq2_1 + player.controlq2_2 + player.controlq2_3
        player.number = random.choices([1,0], weights=(1, 99), k=1)[0]
    @staticmethod
    def is_displayed(player: Player):
      return player.treatnumber == 2


class Atencion3(Page):
    form_model = 'player'
    form_fields = ["controlq3_1", "controlq3_2", "controlq3_3"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.sum_correct = player.controlq3_1 + player.controlq3_2 + player.controlq3_3
        player.number = random.choices([1, 0], weights=(1, 99), k=1)[0]

    @staticmethod
    def is_displayed(player: Player):
        return player.treatnumber == 3

class FailedAttention(Page):
        form_model = 'player'
        form_fields = []

        @staticmethod
        def is_displayed(player: Player):
            return player.sum_correct > 3 and player.number == 1

        def js_vars(player):
            error_code = player.session.config["error_code"]
            link = "https://app.prolific.co/submissions/complete?cc=" + str(error_code)
            return dict(
                errorlink=link
            )

        pass
class Emociones(Page):
    form_model = 'player'
    def get_form_fields(player):
        e = ["happy", "sad", "fear", "anger", "patriotism", "guilt", "uncomfortable", "indifference",
             "boredom", "misunderstanding", "nostalgia", "pride", "shame", "surprise"]
        random.shuffle(e)
        return e

class Quest1(Page):
    form_model = 'player'
    form_fields = ['agreement', 'political_spectrum', 'vote2023', 'vote2023_otro', 'province', 'income_level']

class Quest2(Page):
    form_model = 'player'
    form_fields = ['familyside', 'memory','transmission_school', 'transmission_family',  'transmission_media']

class Quest3(Page):
    form_model = 'player'
    def get_form_fields(player):
        e = ['trust_army', 'trust_civilguard','trust_church', 'trust_constitutionalcourt',  'trust_ombudsman', 'trust_parliament']
        random.shuffle(e)
        return e


class Fin(Page):
    form_model = 'player'
    form_fields = ['q_feedback', 'q_feedback_pilot']

    def js_vars(player):
        cc_code = player.session.config["cc_code"]
        link = "https://app.prolific.co/submissions/complete?cc=" + str(cc_code)
        return dict(
            completionlink=link
        )


page_sequence = [Bienvenida,
                 Texto,

                 Atencion1,
                 Atencion2,
                 Atencion3,
                 Choice,
                 FailedAttention,
                 Emociones,
                 Quest1,
                 Quest2,
                 Quest3,
                 Fin]
