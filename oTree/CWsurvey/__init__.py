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
    control_number = models.IntegerField()
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

    agreement = models.IntegerField(label="1. ¿En qué medida considera que el texto representa fielmente los acontecimientos históricos reales?",
                                       choices=[[1, 'En ninguna medida'],
                                          [2, 'En poca medida'],
                                          [3, 'En medida neutral '],
                                          [4, 'En buena medida' ],
                                          [5, 'En gran medida']], widget=widgets.RadioSelectHorizontal)

    ##Political preferences
    political_spectrum = models.IntegerField(label = '3. En política se habla normalmente de “izquierda” y “derecha”. En una escala donde “0” es la izquierda y “10” la derecha, ¿dónde se ubicaría usted?',
                                             choices=[ [0, '0 \n Izquierda'],
                                                       [1, '1'],
                                                       [2, '2'],[3, '3'],[4, '4'], [5, '5'],[6, '6'],
                                                       [7, '7'], [8, '8'],[9, '9'],[10, '10 \n Derecha']], widget=widgets.RadioSelectHorizontal
                                             )
    #25 most voted
    vote2023 = models.StringField(
        label= "2. ¿Por cuál partido o coalición votó usted en las elecciones generales del 23 de julio de 2023?",
        choices=[
            "Partido Popular (PP)",
            "Partido Socialista Obrero Español (PSOE)",
            "VOX (VOX)",
            "SUMAR (SUMAR)",
            "Esquerra Republicana de Catalunya (ERC)",
            "Junts Per Catalunya - Junts (JxCAT - JUNTS)",
            "Euskal Herria Bildu (EH Bildu)",
            "Partido Nacionalista Vasco (EAJ-PNV)",
            "Bloque Nacionalista Galego (BNG)",
            "Coalición Canaria (CCa)",
            "Unión del Pueblo Navarro (UPN)",
            "Partido Animalista con el Medio Ambiente (PACMA)",
            "Candidatura D’Uunitat Popular-Per La Ruptura (CUP-PR)",
            "Frente Obrero (FO)",
            "Nueva Canarias - Bloque Canarista (NC-bc)",
            "Partit Demòcrata Europeu Català (PDeCAT-E-CiU)",
            "Recortes Cero (RECORTES CERO)",
            "Unión del Pueblo Leonés (UPL)",
            "Por Un Mundo Más Justo (PUM+J)",
            "EXISTE",
            "Partido Comunista de los Trabajadores de España (PCTE)",
            "Otro",
            "Prefiero no responder",
            "No votó",
            "Voto en blanco"
        ])
    vote2023_otro = models.StringField(label = "3. Si seleccionó 'Otro', por favor especifique:", blank=True )


   ##Personal Experience
    familyside = models.IntegerField(label="2. Por lo que usted sabe o puede recordar, ¿con cuál de los dos bandos de la Guerra Civil simpatizaba más su familia?",
                                      choices = [
                                          [1, 'Con los nacionales'],
                                          [2, 'Con los republicanos'],
                                          [3, 'Unos con los nacionales y otros con los republicanos'],
                                          [4, 'Con ninguno de los dos' ],
                                          [5, 'No sabe']], widget=widgets.RadioSelect)

    transmission_school = models.IntegerField(label = "En la escuela: ",
                                              choices=[[0, 'Nada'],
                                                       [1,'Poco'],
                                                       [2,'Algo'],
                                                       [3,'Bastante'],
                                                       [4, 'Mucho']],widget=widgets.RadioSelectHorizontal)
    transmission_family = models.IntegerField(label = 'En la familia: ',
                                              choices=[[0, 'Nada'],
                                                       [1, 'Poco'],
                                                       [2, 'Algo'],
                                                       [3, 'Bastante'],
                                                       [4, 'Mucho']], widget = widgets.RadioSelectHorizontal)

    transmission_media = models.IntegerField(label = 'En los medios de comunicación (libros, películas, prensa, etc.): ',
                                             choices=[[0, 'Nada'],
                                                      [1, 'Poco'],
                                                      [2, 'Algo'],
                                                      [3, 'Bastante'],
                                                      [4, 'Mucho']], widget = widgets.RadioSelectHorizontal)



    memory = models.LongStringField(label="3. Por favor, recuerde cualquier historia(s) sobre la Guerra Civil o el Franquismo que haya sido compartida en su familia. Resúmala brevemente en unas pocas frases.")
    transmission_binary = models.IntegerField(label="4.Si tuviera hijos (o si los tiene), les transmitiría (o les ha transmitido) lo anterior?", choices= [[0,"No"],
    [1, "Sí"]])
    transmission_no = models.LongStringField(
        label="5. Si su respuesta a la anterior pregunta es no, ¿nos podría explicar brevemente qué les transmitiría?", blank=True)



    #Trust

    trust_army = models.IntegerField(label="Ejército",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_civilguard = models.IntegerField(label="Guardia Civil",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_church = models.IntegerField(label="Iglesia",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_constitutionalcourt= models.IntegerField(label="Tribunal Constitucional",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_ombudsman= models.IntegerField(label="Defensor del Pueblo",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_parliament= models.IntegerField(label="Parlamento",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)

    #Demographics
    #'
    age = models.IntegerField(
        label="1. ¿Cuál es su edad?",
        min = 0,  # You can adjust the minimum and maximum age limits as needed
        max = 100,
    )
    gender = models.StringField(
        label="2. ¿Cuál es su sexo?",
        choices=[
            ("male", "Hombre"),
            ("female", "Mujer"),
            ("other", "Otro"),
            ("prefer_not_to_say", "Prefiero no decirlo"),
        ],
    )
    level_studies = models.StringField(
        label="7. ¿Cuál es su nivel más alto de estudios completados?",
        choices=[
            ("none", "Ninguno"),
            ("primary", "Educación primaria"),
            ("secondary", "Educación secundaria"),
            ("higher", "Educación superior (universidad o equivalente)"),
            ("postgraduate", "Postgrado o superior"),
        ],
    )
    employment_situation = models.StringField(
        label="8. ¿Cuál es su situación laboral actual?",
        choices=[
            ("employed", "Empleado/a"),
            ("unemployed", "Desempleado/a"),
            ("student", "Estudiante"),
            ("retired", "Jubilado/a"),
            ("other", "Otro"),
        ],
    )
    religiosity = models.StringField(
        label="6. ¿Cómo se define usted en materia religiosa?",
        choices=[
            ("catholic", "Católico"),
            ("other religion", "Creyente de otra religión"),
            ("non believer", "No Creyente"),
            ("atheist", "Ateo"),
            ("agnostic", "Agnóstico"),
        ],
    )
    province = models.StringField(
        label="5. ¿En qué provincia de España creció (dónde residía antes de los 16 años)? Seleccione su provincia de residencia o, si vivió la mayor parte de su vida antes de los 16 años fuera de España, elija la opción 'Fuera de España':",
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
        label="4. Aproximadamente, ¿cuál es su nivel de ingresos mensuales (antes de impuestos)?",
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
    q_feedback = models.LongStringField(label="Este es el final de la encuesta. Si tiene comentarios, por favor déjelos aquí.",
                                        blank=True)
    q_feedback_pilot = models.LongStringField(
        label="Si encontró alguna instrucción poco clara o confusa, por favor háganoslo saber aquí.",
        blank=True)

    ##Attention questions
    pregunta_1 = models.IntegerField(
        label="1. ¿Cuál fue la causa principal de la Guerra Civil Española?",
        choices=[
            [1, 'El fracaso de la Segunda República para gobernar responsablemente y mantener el orden.'],
            [2, 'La rebelión nacionalista contra un gobierno legítimo y democrático.'],
            [3, 'Las divisiones políticas, sociales y económicas arraigadas, exacerbadas por visiones irreconciliables para España.'],
            [4, 'La intervención de potencias extranjeras que avivaron las tensiones.']],  widget=widgets.RadioSelect)

    pregunta_2 = models.IntegerField(
        label="2. ¿Qué bando fue el responsable de causar la mayoría de las muertes durante la guerra?",
        choices=[
            [1, 'Los Republicanos, a través de ejecuciones masivas y violencia radical.'],
            [2, 'Los Nacionales, a través de su represión sistemática y campañas de bombardeo.'],
            [3, 'Ambos bandos, ya que se cometieron atrocidades por ambas facciones.'],
            [4, 'La intervención extranjera, que exacerbó las bajas.']],  widget=widgets.RadioSelect)

    pregunta_3 = models.IntegerField(
        label="3. En términos de gobernanza, el régimen de Franco fue...",
        choices=[
            [1, 'una fuerza estabilizadora y unificadora que corrigió el caos de la era republicana.' ],
            [2, 'una dictadura represiva que sofocó las libertades individuales y la expresión cultural.'],
            [3, 'un régimen autoritario que impuso orden pero sacrificó las libertades democráticas. '],
            [4, 'un gobierno de transición en el camino de España hacia la democracia moderna.']],  widget=widgets.RadioSelect)
    pregunta_4 = models.IntegerField(
        label="4. ¿Cómo se caracteriza a la España de hoy en día en comparación con la epoca de Franco?",
        choices=[
            [1, 'La España moderna sufre tensiones separatistas, en contraste con la era de estabilidad y orgullo nacional de Franco.' ],
            [2, 'La España moderna prospera como una sociedad democrática centrada en la libertad, a diferencia del régimen represivo de Franco. '],
            [3, 'La España moderna es un país que todavía lucha con las tensiones regionales y el legado del autoritarismo de Franco.'],
            [4, 'La España moderna ha alcanzado plena unidad y prosperidad, dejando atrás las divisiones de la Guerra Civil.']],  widget=widgets.RadioSelect)


    def set_error_message1(player, value):
        correct_answers = {
            'pregunta_1': 3,
            'pregunta_2': 3,
            'pregunta_3': 3,
            'pregunta_4':3,
        }

        incorrect_questions = []

        for question, correct_answer in correct_answers.items():
            if value.get(question) != correct_answer:
                incorrect_questions.append(question)

        if incorrect_questions:
            incorrect_list = ", ".join(incorrect_questions)
            return (
                f"No respondió a las siguientes preguntas correctamente: {incorrect_list}. "
                "Por favor, vuelva a las instrucciones y revise sus respuestas."
            )
        return None  # Return None if all answers are correct
    def set_error_message2(player, value):
        correct_answers = {
            'pregunta_1': 1,
            'pregunta_2': 1,
            'pregunta_3': 1,
            'pregunta_4': 1,
        }

        incorrect_questions = []

        for question, correct_answer in correct_answers.items():
            if value.get(question) != correct_answer:
                incorrect_questions.append(question)

        if incorrect_questions:
            incorrect_list = ", ".join(incorrect_questions)
            return (
                f"No respondió a las siguientes preguntas correctamente: {incorrect_list}. "
                "Por favor, vuelva a las instrucciones y revise sus respuestas."
            )
        return None  # Return None if all answers are correct
    def set_error_message3(player, value):
        correct_answers = {
            'pregunta_1': 2,
            'pregunta_2': 2,
            'pregunta_3': 2,
            'pregunta_4': 2,
        }

        incorrect_questions = []

        for question, correct_answer in correct_answers.items():
            if value.get(question) != correct_answer:
                incorrect_questions.append(question)

        if incorrect_questions:
            incorrect_list = ", ".join(incorrect_questions)
            return (
                f"No respondió a las siguientes preguntas correctamente: {incorrect_list}. "
                "Por favor, vuelva a las instrucciones y revise sus respuestas."
            )
        return None  # Return None if all answers are correct

class Bienvenida(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        player.treatnumber = random.choices([1,2,3], weights=(1,0,0), k=1)[0]
        player.control_number = random.choices([1,2,3,4], weights=(1/4,1/4,1/4,1/4), k=1)[0]

        return {
            'treatnumber': player.treatnumber
        }
class Sociodemograficas(Page):
    form_model = 'player'
    form_fields = ['age', 'gender','political_spectrum',   'income_level', 'province', 'religiosity','level_studies', 'employment_situation']
class Text1(Page):
    form_model = 'player'
    form_fields = ["pregunta_1",'pregunta_2', 'pregunta_3' , 'pregunta_4']
    def error_message(player,value):
        return player.set_error_message1(value)
    def is_displayed(player: Player):
        return player.treatnumber == 1

class Text2(Page):
    form_model = 'player'
    form_fields = ["pregunta_1",'pregunta_2', 'pregunta_3' , 'pregunta_4']
    def error_message(player,value):
        return player.set_error_message2(value)
    def is_displayed(player: Player):
        return player.treatnumber == 2

class Text3(Page):
    form_model = 'player'
    form_fields = ["pregunta_1",'pregunta_2', 'pregunta_3' , 'pregunta_4']
    def error_message(player,value):
        return player.set_error_message3(value)
    def is_displayed(player: Player):
        return player.treatnumber == 3

class IntroChoice(Page):
    pass

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


class Emociones(Page):
    form_model = 'player'
    def get_form_fields(player):
        e = ["happy", "sad", "fear", "anger", "patriotism", "guilt", "uncomfortable", "indifference",
             "boredom", "misunderstanding", "nostalgia", "pride", "shame", "surprise"]
        random.shuffle(e)
        return e

class Quest1(Page):
    form_model = 'player'
    form_fields = ['agreement', 'vote2023', 'vote2023_otro']

class Quest2(Page):
    form_model = 'player'
    form_fields = ['transmission_school', 'transmission_family',  'transmission_media','familyside', 'memory', 'transmission_binary','transmission_no']

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
                 Sociodemograficas,
                 Text1,
                 Text2,
                 Text3,
                 IntroChoice,
                 Choice,
                 Quest1,
                 Quest2,
                 Quest3,
                 Emociones,
                 Fin]
