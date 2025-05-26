from otree.api import *

import random
class C(BaseConstants):
    NAME_IN_URL = 'CWsurvey_netquest'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    participation_fee = 2 # in pounds



class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass



class Player(BasePlayer):
    pid = models.StringField()
    organization_order = models.StringField()


    # Allocations
    donation_faes = models.IntegerField()
    donation_avanza= models.IntegerField()




   ##Personal Experience/Memory

    family_shared_stories = models.StringField(
        label="1. ¿Ha compartido su familia historias sobre la Guerra Civil Española y/o la dictadura de Franco?",
        choices=[
            "Sí, mi familia ha compartido historias",
            "No, nadie en mi familia ha compartido historias",
            "No estoy seguro/a"
        ],
        widget=widgets.RadioSelect
    )


    who_shared_stories_grandpa = models.BooleanField(label="Abuelos", blank=True, initial=False)
    who_shared_stories_parents = models.BooleanField(label="Padres", blank=True, initial=False)
    who_shared_stories_other = models.BooleanField(label="Otros parientes", blank=True, initial=False)
    who_shared_stories_noone = models.BooleanField(label="Nadie", blank=True, initial=False)
    story_detail_level = models.StringField(
        label="3.¿Qué nivel de detalle tenían esas historias familiares?",
        choices=[
            "Muy detalladas, con nombres y eventos específicos",
            "Algo detalladas, experiencias generales de la familia",
            "Poco detalladas, solo menciones breves",
            "No he escuchado ninguna historia familiar"
        ],
        widget=widgets.RadioSelect
    )
    familyside = models.IntegerField(label="4. Por lo que usted sabe o puede recordar, ¿con cuál de los dos bandos de la Guerra Civil simpatizaba más su familia?",
                                      choices = [
                                          [1, 'Con los nacionales'],
                                          [2, 'Con los republicanos'],
                                          [3, 'Unos con los nacionales y otros con los republicanos'],
                                          [4, 'Con ninguno de los dos' ],
                                          [5, 'No sabe']], widget=widgets.RadioSelect)
    memory = models.LongStringField(label="5. Por favor, recuerde cualquier historia sobre la Guerra Civil Española o el Franquismo que haya vivido o haya sido compartida en su familia. Resúmala brevemente en unas frases. Si las memorias incluyen acciones, indique, en la medida de lo posible, qué bando fue responsable (Republicanos/Nacionales).")

    # Persona 1 – Consecuencias múltiples (cada una como BooleanField)
    p1_died_in_combat = models.BooleanField(label="Falleció en combate", blank=True, initial=False)
    p1_died_in_bombing = models.BooleanField(label="Murió en un bombardeo", blank=True, initial=False)
    p1_assesinated = models.BooleanField(label="Fue asesinado", blank=True, initial=False)
    p1_dissapeared = models.BooleanField(label="Desapareció", blank=True, initial=False)
    p1_jail = models.BooleanField(label="Ingresó en prisión", blank=True, initial=False)
    p1_leftspain = models.BooleanField(label="Tuvo que salir de Espana", blank=True, initial=False)
    p1_hiding = models.BooleanField(label="Tuvo que esconderse", blank=True, initial=False)
    p1_lostjob = models.BooleanField(label="Le echaron de su trabajo", blank=True, initial=False)
    p1_another = models.BooleanField(label="Otra situación", blank=True, initial=False)
    p1_nothing = models.BooleanField(label="No aplica", blank=True, initial=False)

    # Persona 2 – Consecuencias múltiples (cada una como BooleanField)
    p2_died_in_combat = models.BooleanField(label="Falleció en combate", blank=True,initial=False)
    p2_died_in_bombing = models.BooleanField(label="Murió en un bombardeo", blank=True,initial=False)
    p2_assesinated = models.BooleanField(label="Fue asesinado", blank=True,initial=False)
    p2_dissapeared = models.BooleanField(label="Desapareció", blank=True,initial=False)
    p2_jail = models.BooleanField(label="Ingresó en prisión", blank=True,initial=False)
    p2_leftspain = models.BooleanField(label="Tuvo que salir de Espana", blank=True,initial=False)
    p2_hiding = models.BooleanField(label="Tuvo que esconderse", blank=True,initial=False)
    p2_lostjob = models.BooleanField(label="Le echaron de su trabajo", blank=True,initial=False)
    p2_another = models.BooleanField(label="Otra situación", blank=True,initial=False)
    p2_nothing = models.BooleanField(label="No aplica", blank=True,initial=False)
    # Persona 3
    p3_died_in_combat = models.BooleanField(label="Falleció en combate", blank=True,initial=False)
    p3_died_in_bombing = models.BooleanField(label="Murió en un bombardeo", blank=True,initial=False)
    p3_assesinated = models.BooleanField(label="Fue asesinado", blank=True,initial=False)
    p3_dissapeared = models.BooleanField(label="Desapareció", blank=True,initial=False)
    p3_jail = models.BooleanField(label="Ingresó en prisión", blank=True,initial=False)
    p3_leftspain = models.BooleanField(label="Tuvo que salir de Espana", blank=True,initial=False)
    p3_hiding = models.BooleanField(label="Tuvo que esconderse", blank=True,initial=False)
    p3_lostjob = models.BooleanField(label="Le echaron de su trabajo", blank=True,initial=False)
    p3_another = models.BooleanField(label="Otra situación", blank=True,initial=False)
    p3_nothing = models.BooleanField(label="No aplica", blank=True,initial=False)

    p1_responsible= models.BooleanField(label="",
                                        choices=[
                                            "El bando Nacional",
                                            "El bando Republicano",
                                            "No sé",
                                            "No aplica"
                                        ],
                                        widget=widgets.RadioSelect)
    p2_responsible= models.BooleanField(label="",
                                        choices=[
                                            "El bando Nacional",
                                            "El bando Republicano",
                                            "No sé",
                                            "No aplica"
                                        ],
                                        widget=widgets.RadioSelect)
    p3_responsible= models.BooleanField(label="",
                                        choices=[
                                            "El bando Nacional",
                                            "El bando Republicano",
                                            "No sé",
                                            "No aplica"
                                        ],
                                        widget=widgets.RadioSelect)



    #Family Memory Alignment
    family_memory_alignment = models.IntegerField(
        label="8. En general, ¿diría usted que las conversaciones dentro de su familia (como recuerdos compartidos, historias contadas, anécdotas, etc.) fueron más favorables hacia uno de los bandos de la Guerra Civil Española?",
        choices=[
            [0, '0 Completamente favorable al bando Republicano'],
            [1, '1'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5 Igualmente favorable/desfavorable a ambos'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, '9'],
            [10, '10 Completamente favorable al bando Nacional'],
            [99, 'No aplica (No tengo memorias familiares).']
        ], widget=widgets.RadioSelectHorizontal)


    # Current alignment with side
    current_alignment = models.StringField(
        choices=[
            "El bando republicano",
            "El bando nacional",
            "En los dos",
            "Ninguno de los dos",
            "No lo sé / Prefiero no responder"
        ],
        label="9. ¿En cuál de los dos bandos que participaron en la Guerra Civil se encuentran mejor reflejadas sus ideas politicas actuales?",
        widget=widgets.RadioSelect)



    #Trust
    trust_army = models.IntegerField(label="Ejército",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_civilguard = models.IntegerField(label="Guardia Civil",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_church = models.IntegerField(label="Iglesia Católica",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_constitutionalcourt= models.IntegerField(label="Tribunal Constitucional",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_ombudsman= models.IntegerField(label="Defensor del Pueblo",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)
    trust_parliament= models.IntegerField(label="Parlamento",choices=[0, 1, 2, 3, 4],widget=widgets.RadioSelect)



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
            ("prefer_not_to_say", "Prefiero no responder"),
        ],
    )
    level_studies = models.StringField(
        label="3. ¿Cuál es su nivel más alto de estudios completados?",
        choices=[
            ("none", "Ninguno"),
            ("primary", "Educación primaria"),
            ("secondary", "Educación secundaria"),
            ("higher1", "Educación superior (Formación Profesional o equivalente)"),
            ("higher2", "Educación superior (Universidad o equivalente)"),
            ("postgraduate", "Postgrado o superior (Maestría, Doctorado o equivalente)"),
        ],
    )
    employment_situation = models.StringField(
        label="4. ¿Cuál es su situación laboral actual?",
        choices=[
            ("employed", "Empleado/a"),
            ("unemployed", "Desempleado/a"),
            ("student", "Estudiante"),
            ("retired", "Jubilado/a"),
            ("other", "Otro"),
        ],
    )
    religiosity = models.StringField(
        label="9. ¿Cómo se define usted en materia religiosa?",
        choices=[
            ("catholic", "Cristiano Católico"),
            ("protestant","Cristiano Protestante"),
            ("Muslim","Musulmán"),
            ("other religion", "Creyente de otra religión"),
            ("agnostic", "Agnóstico"),
            ("non believer/atheist", "No Creyente/Ateo"),
        ])


    province = models.StringField(
        label="10. ¿En qué provincia de España creció (dónde residía antes de los 16 años)? Seleccione su provincia de residencia o, si vivió la mayor parte de su vida antes de los 16 años fuera de España, elija la opción 'Fuera de España':",
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

    ##Immigration background
    immigration_background = models.StringField(
        label="11. ¿Nació usted o alguno de sus padres fuera de España?",
        choices=["Sí", "No"],
        widget=widgets.RadioSelect
    )

    birth_self = models.StringField(
        label="11a. ¿Dónde nacio usted?",
        blank=True,
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


    birth_parents = models.StringField(
        label="11b. ¿Dónde nacieron sus padres?",
        choices=[
            "Ambos nacieron en España",
            "Uno nació en España y otro en el extranjero",
            "Ambos nacieron en el extranjero"
        ],
        widget=widgets.RadioSelect,
        blank=True
    )

    spanish_ascendance = models.StringField(
        label="11c. Si sus padres nacieron en el extranjero, ¿sabes si son hijos de emigrantes españoles?",
        choices=[
            "Sí, al menos uno de mis padres es hijo de emigrantes españoles",
            "No, ninguno de mis padres es hijo de emigrantes españoles",
            "No lo sé"
        ],
        widget=widgets.RadioSelect,
        blank=True
    )
    income_level = models.StringField(
        label="12. Aproximadamente, ¿cuál es su nivel de ingresos mensuales (antes de impuestos)?",
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


    ##Political preferences
    political_spectrum = models.IntegerField(label = '5. ...¿dónde se ubicaría usted?',
                                             choices=[ [0, '0 \n Izquierda'],
                                                       [1, '1'],
                                                       [2, '2'],[3, '3'],[4, '4'], [5, '5'],[6, '6'],
                                                       [7, '7'], [8, '8'],[9, '9'],[10, '10 \n Derecha'],
                                                       [ 99, 'Prefiero no responder']

                                                       ], widget=widgets.RadioSelectHorizontal)
    political_spectrum_mother = models.IntegerField(
        label='6. ...¿Y dónde colocaría a su madre?',
        choices=[[0, '0 \n Izquierda'],
                 [1, '1'],
                 [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                 [7, '7'], [8, '8'], [9, '9'], [10, '10 \n Derecha'],[ 99, 'Prefiero no responder']], widget=widgets.RadioSelectHorizontal
        )

    political_spectrum_father = models.IntegerField(
        label='7. ...¿Y a su padre?',
        choices=[[0, '0 \n Izquierda'],
                 [1, '1'],
                 [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                 [7, '7'], [8, '8'], [9, '9'], [10, '10 \n Derecha'],[ 99, 'Prefiero no responder']], widget=widgets.RadioSelectHorizontal
        )

    political_spectrum_faes = models.IntegerField(
        label='Organización FAES',
        choices=[[0, '0 \n Izquierda'],
                 [1, '1'],
                 [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                 [7, '7'], [8, '8'], [9, '9'], [10, '10 \n Derecha']], widget=widgets.RadioSelectHorizontal
    )
    political_spectrum_avanza = models.IntegerField(
        label='Organización AVANZA',
        choices=[[0, '0 \n Izquierda'],
                 [1, '1'],
                 [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                 [7, '7'], [8, '8'], [9, '9'], [10, '10 \n Derecha']], widget=widgets.RadioSelectHorizontal
    )


    #25 most voted
    vote2023 = models.StringField(
        label= "8. ¿Por cuál partido o coalición votó usted en las elecciones generales del 23 de julio de 2023?",
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
    vote2023_otro = models.StringField(label = "8a. Si seleccionó 'Otro', por favor especifique:", blank=True )





    #Incentivized questions

    belief_immigration_crime = models.IntegerField(label="Según el Instituto Nacional de Estadística (INE), la mayoría de los delitos en España son cometidos por personas inmigrantes.",
                                                   min=0, max=100)
    belief_religious_abuse = models.IntegerField(label="Un estudio de 2014 de la Universidad de Ulm concluyó que el abuso es más probable en instituciones religiosas que en no religiosas.",
                                                 min=0, max=100)
    belief_abortion_deaths = models.IntegerField(label="Según la Organización Mundial de la Salud (OMS), la legalización del aborto aumenta muertes maternas y complicaciones graves de salud para las mujeres.",
                                                 min=0, max=100)
    belief_gender_trends = models.IntegerField(label="Scientific American afirma que el aumento de menores que buscan atención de afirmación de género se debe más a tendencias sociales que a necesidad médica.",
                                               min=0, max=100)
    belief_white_red_terror = models.IntegerField(label="Un estudio de investigadores de la Universidad de California estima que unas 150.000 personas fueron asesinadas por nacionalistas durante el Terror Blanco, y hasta 50.000 por republicanos durante el Terror Rojo.",
                                                  min=0, max=100)
    belief_franco_growth = models.IntegerField(label="Según la revista académica Quarterly Journal of Economics, una revista especializada en economía, el régimen de Franco tuvo el mayor crecimiento económico en la historia reciente de España.",
                                               min=0, max=100)
    belief_franco_kidnapping = models.IntegerField(label="La revista New York Times Magazine afirma que el franquismo secuestró niños para dárselos a sus simpatizantes.",
                                                   min=0, max=100)

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
    patriotism = make_field(label="Patriotismo")
    compassion= make_field(label="Compasión")
    guilt = make_field(label="Culpa")
    uncomfortable = make_field(label="Incomodidad")
    indifference = make_field(label="Indiferencia")
    boredom = make_field(label="Aburrimiento")
    misunderstanding = make_field(label="Incomprensión")
    nostalgia = make_field(label="Nostalgia")
    pride = make_field(label="Orgullo")
    shame = make_field(label="Verguenza")
    surprise = make_field(label="Sorpresa")
    envy = make_field(label="Envidia")
    irritation = make_field(label="Irritación")
    contempt = make_field(label="Desprecio")

    #Perceptions about text
    political_spectrum_narrative =models.IntegerField(label="1. ¿En el contexto de la política española actual, dónde situaría usted la postura política expresada en el texto dentro del espectro izquierda–derecha?",
                                                      choices=[[0, '0 \n Izquierda'],
                                                               [1, '1'],
                                                               [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                                                               [7, '7'], [8, '8'], [9, '9'], [10, '10 \n Derecha']],
                                                      widget=widgets.RadioSelectHorizontal
                                                      )

    agreement = models.IntegerField(label="2. ¿Considera que el texto representa fielmente los acontecimientos históricos reales?",
                                    choices=[[0, '0: En ninguna medida'],
                                             [1, '1'],
                                             [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                                             [7, '7'], [8, '8'], [9, '9'], [10, '10: En gran medida']],
                                    widget=widgets.RadioSelectHorizontal
                                    )

    agreement_others = models.IntegerField(
        label="3. ¿Qué proporción de los participantes en este estudio cree usted que estará mayormente de acuerdo con que el texto representa fielmente hechos históricos reales?",
        min=0,
        max=100
    )
    stigma_nationalists = models.IntegerField(
        label="4. ¿Cree usted que expresar apoyo al bando nacionalista está socialmente estigmatizado (es decir, no es políticamente correcto) en la España actual?",
        choices=[[0, '0'],
                 [1, '1'],
                 [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                 [7, '7'], [8, '8'], [9, '9'], [10, '10']],
        widget=widgets.RadioSelectHorizontal
    )
    stigma_republicans = models.IntegerField(
        label="5. ¿Cree usted que expresar apoyo al bando republicano está socialmente estigmatizado (es decir, no es políticamente correcto) en la España actual?",
        choices=[[0, '0'],
                 [1, '1'],
                 [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                 [7, '7'], [8, '8'], [9, '9'], [10, '10']],
        widget=widgets.RadioSelectHorizontal
    )
    learned_something = models.IntegerField(
        label='6. Indique hasta qué punto está usted de acuerdo o en desacuerdo con la siguiente afirmación: "He aprendido algo nuevo gracias al texto que acabo de leer."',
        choices=[[0, '0'],
                 [1, '1'],
                 [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                 [7, '7'], [8, '8'], [9, '9'], [10, '10']],
        widget=widgets.RadioSelectHorizontal
    )
    #Affectivepolarizationv
    def make_field4(label):
        return models.IntegerField(
            choices=[0,1, 2, 3, 4, 5,6,7,8,9,10],
            label=label,
            widget=widgets.RadioSelect,
        )
    vox = make_field4(label="VOX")
    pp = make_field4(label="PP")
    psoe = make_field4(label="PSOE")
    podemos = make_field4(label="Podemos")



    ##Attention questions
    pregunta_1 = models.IntegerField(
        label="1. ¿Cuál fue la causa principal de la Guerra Civil Española?", widget = widgets.RadioSelect)

    pregunta_2 = models.IntegerField(
        label="2. ¿Qué bando fue el responsable de causar la mayoría de las muertes durante la guerra?", widget = widgets.RadioSelect)

    pregunta_3 = models.IntegerField(
        label="3. En términos de gobernanza, el régimen de Franco fue...", widget = widgets.RadioSelect)
    pregunta_4 = models.IntegerField(
        label="4. ¿Cómo se caracteriza a la España de hoy en día en comparación con la época de Franco?", widget = widgets.RadioSelect)

    ###Sources
    transmission_school = models.IntegerField(label="La educacion formal (escuela, colegio, universidad, etc.)",
                                              choices=[[0, 'Nada'],
                                                       [1, 'Poco'],
                                                       [2, 'Algo'],
                                                       [3, 'Bastante'],
                                                       [4, 'Muy']], widget=widgets.RadioSelectHorizontal)
    transmission_family = models.IntegerField(label='La familia o parientes',
                                              choices=[[0, 'Nada'],
                                                       [1, 'Poco'],
                                                       [2, 'Algo'],
                                                       [3, 'Bastante'],
                                                       [4, 'Muy']], widget=widgets.RadioSelectHorizontal)
    transmission_media = models.IntegerField(label='Los medios de comunicación tradicionales (TV,radio, prensa, etc.) ',
                                             choices=[[0, 'Nada'],
                                                      [1, 'Poco'],
                                                      [2, 'Algo'],
                                                      [3, 'Bastante'],
                                                      [4, 'Muy']], widget=widgets.RadioSelectHorizontal)

    transmission_socialmedia = models.IntegerField(label='Las redes sociales (YouTube, TikTok, Instagram, Facebook, X, etc.)',
                                             choices=[[0, 'Nada'],
                                                      [1, 'Poco'],
                                                      [2, 'Algo'],
                                                      [3, 'Bastante'],
                                                      [4, 'Muy']], widget=widgets.RadioSelectHorizontal)
    transmission_friends = models.IntegerField(label='Los amigos o colegas',
                                             choices=[[0, 'Nada'],
                                                      [1, 'Poco'],
                                                      [2, 'Algo'],
                                                      [3, 'Bastante'],
                                                      [4, 'Muy']], widget=widgets.RadioSelectHorizontal)
    transmission_books = models.IntegerField(label='Entretenimiento (libros, películas etc.)',
                                             choices=[[0, 'Nada'],
                                                      [1, 'Poco'],
                                                      [2, 'Algo'],
                                                      [3, 'Bastante'],
                                                      [4, 'Muy']], widget=widgets.RadioSelectHorizontal)

    emotional_connection_family = models.IntegerField(
        label="2. ¿En qué medida han influido las historias familiares en su conexión emocional con eventos históricos como la Guerra Civil Española?",

        choices=[[0, '0'],
                 [1, '1'],
                 [2, '2'],
                 [3, '3'],
                 [4, '4']], widget=widgets.RadioSelectHorizontal)

    credibility_family_vs_school = models.IntegerField(
        label="3. Cuando las historias familiares y la educación escolar ofrecen versiones distintas de un hecho histórico, ¿a cuál tiende usted a dar más credibilidad?",
        choices=[
            [0, 'Solo a la familia'],
            [1, 'Más a la familia'],
            [2, 'A ambos por igual'],
            [3, 'Más a la escuela'],
            [4, 'Solo a la escuela'],
        ])

    follow_political_news = models.IntegerField(
        label="¿Sigue usted las noticias políticas o los acontecimientos actuales?",
        choices=[[0, '0'],
                 [1, '1'],
                 [2, '2'],
                 [3, '3'],
                 [4, '4']], widget=widgets.RadioSelectHorizontal)

    political_participation_current = models.IntegerField(
        label="¿Participa usted en acciones políticas (por ejemplo, protestas, firmas de peticiones o campañas)?",
        choices=[[0, '0'],
                 [1, '1'],
                 [2, '2'],
                 [3, '3'],
                 [4, '4']], widget=widgets.RadioSelectHorizontal)

    political_participation_future = models.IntegerField(
        label="6. En el futuro, ¿qué tan dispuesto/a estaría a participar en actividades políticas (como firmar una petición, asistir a una protesta o colaborar en una campaña)?",
        choices=[[0, '0'],
                 [1, '1'],
                 [2, '2'],
                 [3, '3'],
                 [4, '4']], widget=widgets.RadioSelectHorizontal)

    family_closeness = models.StringField(label="4. ¿Qué tan cercano/a se siente a su familia?",
                                          choices=[[0, '0'],
                                                   [1, '1'],
                                                   [2, '2'],
                                                   [3, '3'],
                                                   [4, '4']], widget=widgets.RadioSelectHorizontal)

    family_alignment = models.StringField(
        label="5. ¿En qué medida siente que está ideológica o políticamente alineado/a con su familia?",

            choices = [[0, '0'],
                       [1, '1'],
                       [2, '2'],
                       [3, '3'],
                       [4, '4']], widget = widgets.RadioSelectHorizontal)


    #Feedback questions
    q_feedback = models.LongStringField(label="Este es el final de la encuesta. Si tiene comentarios, por favor déjelos aquí.",
                                        blank=True)
    q_feedback_pilot = models.LongStringField(
        label="Si encontró alguna instrucción poco clara o confusa, por favor háganoslo saber aquí.",
        blank=True)

    q_feedback_why= models.LongStringField(
        label="")

    #Opinions

    immigration_crime = models.IntegerField(
        label='La inmigración es una de las principales causas del aumento de la criminalidad y la inestabilidad social en nuestro país.',
        choices=[[0, '0'],
                 [1, '1'],
                 [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                 [7, '7'], [8, '8'], [9, '9'], [10,'10']],
        widget=widgets.RadioSelectHorizontal
    )
    welfare_dependency = models.IntegerField(
        label='Los programas de asistencia social del gobierno crean dependencia y desalientan el trabajo duro.',
        choices=[[0, '0'],
                 [1, '1'],
                 [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                 [7, '7'], [8, '8'], [9, '9'], [10, '10']],
        widget=widgets.RadioSelectHorizontal
    )

    traditional_values = models.IntegerField(
        label='Los valores familiares tradicionales están en peligro y necesitan una mayor protección.',
        choices=[[0, '0'],
                 [1, '1'],
                 [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                 [7, '7'], [8, '8'], [9, '9'], [10, '10']],
        widget=widgets.RadioSelectHorizontal
    )

    gender_diversity = models.IntegerField(
        label='El énfasis en cuestiones de género y diversidad ha ido demasiado lejos y está dañando a la sociedad.',
        choices=[[0, '0'],
                 [1, '1'],
                 [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                 [7, '7'], [8, '8'], [9, '9'], [10, '10']],
        widget=widgets.RadioSelectHorizontal
    )

    justice1 = models.IntegerField(
        label='La transición a la democracia en España fue demasiado suave con los responsables de la represión durante la dictadura de Franco.',
        choices=[[0, '0'],
                 [1, '1'],
                 [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                 [7, '7'], [8, '8'], [9, '9'], [10, '10']],
        widget=widgets.RadioSelectHorizontal
    )

    justice2 = models.IntegerField(
        label='Los actuales esfuerzos por recuperar la memoria histórica y eliminar los símbolos franquistas generan una división innecesaria en la sociedad española.',
        choices=[[0, '0'],
                 [1, '1'],
                 [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                 [7, '7'], [8, '8'], [9, '9'], [10, '10']],
        widget=widgets.RadioSelectHorizontal
    )

    justice3 = models.IntegerField(
        label='Las víctimas de la represión franquista no han recibido suficiente justicia ni reconocimiento en España.',
        choices=[[0, '0'],
                 [1, '1'],
                 [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                 [7, '7'], [8, '8'], [9, '9'], [10, '10']],
        widget=widgets.RadioSelectHorizontal
    )

    justice4 = models.IntegerField(
        label='España debería seguir investigando y procesando los crímenes cometidos durante la Guerra Civil y la dictadura franquista.',
        choices=[[0, '0'],
                 [1, '1'],
                 [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                 [7, '7'], [8, '8'], [9, '9'], [10, '10']],
        widget=widgets.RadioSelectHorizontal
    )

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
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.pid = player.participant.label
#        print(f"Retrieved pid from URL: {player.pid}")


class Sociodemograficas(Page):
    form_model = 'player'
    form_fields = [ "age", "gender", "level_studies", "employment_situation",
                    "political_spectrum", "political_spectrum_mother", "political_spectrum_father", "vote2023", "vote2023_otro",
                    "religiosity", "province",  "immigration_background", "birth_self", "birth_parents", "spanish_ascendance",
                    "income_level"]

class Memoria(Page): #"transmission_binary","transmission_no"
    form_model = 'player'
    form_fields = ["family_shared_stories",
                   "who_shared_stories_grandpa", "who_shared_stories_parents","who_shared_stories_other",
                   "who_shared_stories_noone",'story_detail_level', "familyside",'memory',
                   'p1_died_in_combat', 'p1_died_in_bombing', 'p1_assesinated', 'p1_dissapeared', 'p1_jail',
                   'p1_leftspain','p1_hiding', 'p1_lostjob', 'p1_another', 'p1_nothing',
                   'p2_died_in_combat', 'p2_died_in_bombing', 'p2_assesinated', 'p2_dissapeared', 'p2_jail',
                   'p2_leftspain', 'p2_hiding', 'p2_lostjob', 'p2_another', 'p2_nothing',
                   'p3_died_in_combat', 'p3_died_in_bombing', 'p3_assesinated', 'p3_dissapeared', 'p3_jail',
                   'p3_leftspain', 'p3_hiding', 'p3_lostjob', 'p3_another', 'p3_nothing','p1_responsible','p2_responsible',
                   'p3_responsible',
                    'family_memory_alignment','current_alignment'
                   ]




class Text1(Page):
    form_model = 'player'
    form_fields = ["pregunta_1",'pregunta_2', 'pregunta_3' , 'pregunta_4']
    def error_message(player,value):
        return player.set_error_message1(value)

class IntroChoice(Page):
    pass

class IntroChoice_Organizations(Page):
    def vars_for_template(player: Player):
        descriptions = [
            {'name': 'Fundación FAES',
            'description': 'La Fundación FAES es un think tank liberal-conservador que promueve valores como la libertad, la economía de mercado y la unidad nacional. Defiende políticas públicas que refuercen la competitividad, el emprendimiento y el fortalecimiento de las instituciones en España.'},
            {'name': 'Fundación AVANZA',
            'description': 'Laboratorio de Ideas Avanza es un think tank progresista que fomenta el debate sobre los grandes retos sociales. Promueve valores como la democracia social, la igualdad y los derechos humanos, trabajando por una sociedad más inclusiva y justa.'}]
        random.shuffle(descriptions)
        # Save the order to participant.vars
        player.participant.vars['organization_order'] = [d['name'] for d in descriptions]
        player.organization_order = ",".join([d['name'] for d in descriptions])

        return {'descriptions': descriptions}




class IntroChoice_Organizations_position(Page):
    form_model = 'player'
    form_fields = ['political_spectrum_faes', 'political_spectrum_avanza']
    def vars_for_template(player: Player):
        all_descriptions = {
            'Fundación FAES': 'La Fundación FAES es un think tank liberal-conservador que promueve valores como la libertad, la economía de mercado y la unidad nacional. Defiende políticas públicas que refuercen la competitividad, el emprendimiento y el fortalecimiento de las instituciones en España.',
            'Fundación AVANZA': 'Laboratorio de Ideas Avanza es un think tank progresista que fomenta el debate sobre los grandes retos sociales. Promueve valores como la democracia social, la igualdad y los derechos humanos, trabajando por una sociedad más inclusiva y justa.'
        }

        # Reconstruct order using the saved string from the previous page
        order = player.organization_order.split(',')  # or from participant.vars['organization_order']
        descriptions = [{'name': name, 'description': all_descriptions[name]} for name in order]

        return {'descriptions': descriptions}

class Choice(Page):
    form_model = 'player'
    form_fields = ['donation_faes', 'donation_avanza']


class Why(Page):
    form_model = 'player'
    form_fields = ['q_feedback_why']
    def vars_for_template(player):
        return {
            "donation_faes": player.donation_faes,
            "donation_avanza": player.donation_avanza,
        }


class Emociones(Page):
    form_model = 'player'
    def get_form_fields(player):
        e = ["happy", "sad", "fear", "anger", "patriotism", "guilt", "uncomfortable", "indifference",
            "misunderstanding", "nostalgia", "pride", "shame", "surprise", "compassion",'contempt']
        random.shuffle(e)
        return e

class Percepciones(Page):
    form_model = 'player'
    form_fields = ['political_spectrum_narrative', 'agreement','agreement_others',
                   'stigma_nationalists','stigma_republicans','learned_something']

class AP(Page):
    form_model = 'player'
    def get_form_fields(player):
        e = ['vox', 'pp', 'psoe', 'podemos']
        random.shuffle(e)
        return e


class IncStatements(Page):
    form_model = 'player'

    def get_form_fields(player):
        e = [
        'belief_immigration_crime',
        'belief_religious_abuse',
        'belief_abortion_deaths',
        'belief_gender_trends',
        'belief_white_red_terror',
        'belief_franco_growth',
        'belief_franco_kidnapping',
    ]

        random.shuffle(e)
        return e

class Trust(Page):
    form_model = 'player'
    def get_form_fields(player):
        e = ['trust_army', 'trust_civilguard','trust_church', 'trust_constitutionalcourt',  'trust_ombudsman', 'trust_parliament']
        random.shuffle(e)
        return e


class Enunciados(Page):
    form_model = 'player'
    form_fields = ['immigration_crime', 'welfare_dependency', 'traditional_values', 'gender_diversity',
             'justice1','justice2', 'justice3', 'justice4']


class Sources(Page):
    form_model = 'player'
    form_fields = ['transmission_school', 'transmission_family', 'transmission_friends',
                   'transmission_media',
                   'transmission_books', 'transmission_socialmedia','emotional_connection_family',
                   'credibility_family_vs_school','family_closeness','family_alignment',
                   'political_participation_future']

class Debriefing(Page):
    form_model = 'player'
    form_fields = []


class Fin(Page):
    form_model = 'player'
    form_fields = ['q_feedback', 'q_feedback_pilot']

    def js_vars(player):
        pid = player.pid
        link = "https://transit.nicequest.com/transit/participation?tp=co_0&c=ok&ticket=" + str(pid)
        return dict(
            completionlink=link
        )


page_sequence = [Bienvenida,
                 Sociodemograficas,
                 Memoria,
                 Text1,
                 IntroChoice,
                 IntroChoice_Organizations,
                 IntroChoice_Organizations_position,
                 Choice,
                 Why,
                 Emociones,
                 Percepciones,
                 IncStatements,
                 AP,
                 Enunciados,
                 Trust,
                 Sources,
                 Debriefing,
                 Fin]
