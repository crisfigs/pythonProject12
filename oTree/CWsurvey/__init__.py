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
        label="¿Cuánto desea asignar a la <b>Fundación AVANZA</b>?",
        min=0,
        max=100)
    allocation_right = models.IntegerField(
        label="¿Cuánto desea asignar a la <b>Fundación FAES</b>?",
        min=0,
        max=100)
    allocation_neutral = models.IntegerField(
        label="¿Cuánto desea asignar a la <b>Fundación Española del Corazón</b>?",
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
    familyside = models.IntegerField(label="5. Por lo que usted sabe o puede recordar, ¿con cuál de los dos bandos de la Guerra Civil simpatizaba más su familia?",
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



    memory = models.LongStringField(label="6. Por favor, recuerde cualquier historia(s) sobre la Guerra Civil o el Franquismo que haya sido compartida en su familia. Resúmala brevemente en unas pocas frases.")
    transmission_binary = models.IntegerField(label="7. Si tiene hijos, o si los tuviera en el futuro, ¿les transmitiría (o les ha transmitido) las historias sobre la Guerra Civil y la época de Franco que su familia le contó?",
                                              choices= [[1,'Sí'], [0, 'No']])

    transmission_no = models.LongStringField(
        label="8. Si su respuesta a la anterior pregunta es no, ¿nos podría explicar brevemente qué les transmitiría?", blank=True)



    #Trust

    trust_army = models.IntegerField(label="Ejército",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_civilguard = models.IntegerField(label="Guardia Civil",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_church = models.IntegerField(label="Iglesia",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_constitutionalcourt= models.IntegerField(label="Tribunal Constitucional",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_ombudsman= models.IntegerField(label="Defensor del Pueblo",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_parliament= models.IntegerField(label="Parlamento",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)

    #History
    talk_past = models.IntegerField(label="9. Es mejor olvidarse del pasado porque, si se remueve, podría volver a repetirse la Guerra Civil.",
                                    choices=[[1, 'Completamente en desacuerdo'],
                                             [2, 'Más bien en desacuerdo'],
                                             [3, 'Ni de acuerdo ni en desacuerdo'],
                                             [4, 'Más bien de acuerdo'],
                                             [5, 'Completamente de acuerdo']], widget=widgets.RadioSelectHorizontal)

    partiality_education = models.IntegerField(label="10. La enseñanza de la historia de la Guerra Civil Española y la época de Franco en la actualidad carece de objetividad.",
                                                choices=[[1, 'Completamente en desacuerdo'],
                                                         [2, 'Más bien en desacuerdo'],
                                                         [3, 'Ni de acuerdo ni en desacuerdo'],
                                                         [4, 'Más bien de acuerdo'],
                                                         [5, 'Completamente de acuerdo']],
                                                widget=widgets.RadioSelectHorizontal)

    regionalism_education = models.IntegerField(label="11. Existe una excesiva variabilidad entre regiones en la manera en que se imparte la historia de España.",
                                                choices=[[1, 'Completamente en desacuerdo'],
                                                         [2, 'Más bien en desacuerdo'],
                                                         [3, 'Ni de acuerdo ni en desacuerdo'],
                                                         [4, 'Más bien de acuerdo'],
                                                         [5, 'Completamente de acuerdo']],
                                                widget=widgets.RadioSelectHorizontal)


    #Demographics

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
            ("non believer/atheist", "No Creyente/Ateo"),
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


 #Factual questions
    franco_years_in_power = models.IntegerField(label="¿Cuántos años gobernó Francisco Franco en España?")
    civil_war_duration = models.IntegerField(label="¿Cuánto tiempo duró la Guerra Civil Española?")
    white_terror_executions = models.IntegerField(label="¿Cuántos civiles fueron ejecutados durante el Terror Blanco de Franco (1939–1945)?")
    red_terror_executions = models.IntegerField(label="¿Cuántos civiles fueron ejecutados durante el Terror Rojo de los republicanos (1936–1939)?")

    industrial_decline_percentage = models.IntegerField(label="¿Cuál fue el porcentaje estimado de disminución en la producción industrial en España al final de la Guerra Civil (1939 comparado con 1936)?", min=0,max=100)
    gdp_growth_rate = models.FloatField(label="En promedio, ¿cuánto creció anualmente el PIB per cápita de España durante el régimen de Franco (1939-1975)? Responda con un porcentaje.",min=0,max=100)
    emigrated_due_to_repression = models.IntegerField(label="¿Cuántos españoles emigraron debido a la represión política durante el régimen de Franco?")
    orphaned_children = models.IntegerField(label="¿Cuántos niños fueron enviados a los orfanatos del Auxilio Social durante la dictadura franquista?")
    churches_destroyed = models.IntegerField(label="Aproximadamente, ¿cuántas iglesias católicas fueron destruidas durante la Guerra Civil Española?")
    gender_wage_gap_percentage = models.FloatField(label="¿Qué porcentaje más ganan los hombres que las mujeres en España por realizar el mismo trabajo?",min=0,max=100)
    temporary_contracts_percentage = models.FloatField(label="En España, ¿qué porcentaje de los contratos laborales firmados en 2023 fueron temporales?",min=0,max=100)
    unsafe_abortion_deaths = models.IntegerField(label="Según la OMS, ¿cuántas mujeres mueren cada año como consecuencia de abortos inseguros en países donde el aborto es ilegal o tiene restricciones severas?")
    immigrant_welfare_percentage = models.FloatField(label="¿Cuál es el porcentaje de los beneficiarios de prestaciones sociales en España que son inmigrantes?",min=0,max=100)
    gdp_gap_richest_poor = models.FloatField(label="En términos de PIB per cápita, ¿cuál es la diferencia aproximada entre las comunidades más ricas y más pobres de España? Responda con un porcentaje.",min=0,max=100)
    marijuana_health_issues_percentage = models.FloatField(label="¿Qué porcentaje de personas que consumen marihuana desarrolla problemas graves de salud mental, como ansiedad o depresión? ",min=0,max=100)
    richest_tax_revenue_percentage = models.FloatField(label="En España, ¿qué porcentaje del gasto público total se financia con los impuestos recaudados de los ciudadanos y empresas más ricas (el 10% con mayores ingresos)?",min=0,max=100)
    co2_reduction_percentage = models.FloatField(label="En términos de emisiones de CO₂, ¿cuánto más bajas son las emisiones de un coche eléctrico en comparación con un coche de gasolina, considerando todo su ciclo de vida? Responda con un porcentaje.",min=0,max=100)
    public_funding_tauromaquia = models.IntegerField(label="En España, ¿qué cantidad de dinero público se destina anualmente al apoyo de la tauromaquia (subvenciones, ayudas locales, etc.)?")







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
        label="1. ¿Cuál fue la causa principal de la Guerra Civil Española?")

    pregunta_2 = models.IntegerField(
        label="2. ¿Qué bando fue el responsable de causar la mayoría de las muertes durante la guerra?")

    pregunta_3 = models.IntegerField(
        label="3. En términos de gobernanza, el régimen de Franco fue...")
    pregunta_4 = models.IntegerField(
        label="4. ¿Cómo se caracteriza a la España de hoy en día en comparación con la época de Franco?")

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


def pregunta_1_choices(player):
    import random
    choices = [[1, 'El fracaso de la Segunda República para gobernar responsablemente y mantener el orden.'],
               [2, 'La rebelión nacionalista contra un gobierno legítimo y democrático.'],
               [3,'Las divisiones políticas, sociales y económicas arraigadas, exacerbadas por visiones irreconciliables para España.'],
               [4, 'La intervención de potencias extranjeras que avivaron las tensiones.']]
    random.shuffle(choices)
    return choices

def pregunta_2_choices(player):
    import random
    choices=[
            [1, 'Los Republicanos, a través de ejecuciones masivas y violencia radical.'],
            [2, 'Los Nacionales, a través de su represión sistemática y campañas de bombardeo.'],
            [3, 'Ambos bandos, ya que se cometieron atrocidades por ambas facciones.'],
            [4, 'La intervención extranjera, que exacerbó las bajas.']]
    random.shuffle(choices)
    return choices

def pregunta_3_choices(player):
    import random
    choices = [
        [1, 'una fuerza estabilizadora y unificadora que corrigió el caos de la era republicana.'],
        [2, 'una dictadura represiva que sofocó las libertades individuales y la expresión cultural.'],
        [3, 'un régimen autoritario que consiguió orden pero sacrificó las libertades democráticas. '],
        [4,'un gobierno de transición en el camino de España hacia la democracia moderna.']]
    random.shuffle(choices)
    return choices

def pregunta_4_choices(player):
    import random
    choices = [
        [1, 'La España moderna sufre tensiones separatistas, en contraste con la época de estabilidad y orgullo nacional de Franco.'],
        [2, 'La España moderna prospera como una sociedad democrática centrada en la libertad, a diferencia del régimen represivo de Franco. '],
        [3, 'La España moderna es un país que todavía lucha con las tensiones regionales y el legado de la Guerra Civil y el Franquismo.'],
        [4, 'La España moderna ha alcanzado plena unidad y prosperidad, dejando atrás las divisiones de la Guerra Civil.']]
    random.shuffle(choices)
    return choices


class Bienvenida(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        player.treatnumber = random.choices([1,2,3], weights=(1/3,1/3,1/3), k=1)[0]
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
    def error_message(player, values):
        if values['transmission_binary'] == 0 and not values['transmission_no']:
            return "Por favor, responda brevemente a la pregunta 8."


class Quest2_(Page):
    form_model = 'player'
    form_fields = ['talk_past','partiality_education', 'regionalism_education']

class Quest3(Page):
    form_model = 'player'
    def get_form_fields(player):
        e = ['trust_army', 'trust_civilguard','trust_church', 'trust_constitutionalcourt',  'trust_ombudsman', 'trust_parliament']
        random.shuffle(e)
        return e

class FactualQs(Page):
    form_model = 'player'
    timeout_seconds = 360 # 5 minutes (300 seconds)

    def get_form_fields(player):
        b =  [
        'franco_years_in_power','civil_war_duration','white_terror_executions','red_terror_executions','industrial_decline_percentage',
        'gdp_growth_rate','emigrated_due_to_repression','orphaned_children','churches_destroyed','gender_wage_gap_percentage',
        'temporary_contracts_percentage','unsafe_abortion_deaths','immigrant_welfare_percentage','gdp_gap_richest_poor',
        'marijuana_health_issues_percentage','richest_tax_revenue_percentage','co2_reduction_percentage','public_funding_tauromaquia']
        random.shuffle(b)
        return b

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
                Quest2_,
                 Quest3,
                 Emociones,
                 FactualQs,
                 Fin]
