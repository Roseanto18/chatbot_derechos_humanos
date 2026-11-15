"""
CONTENIDO NUEVO (v5): preguntas frecuentes + Unidades 3 y 4 del temario de
"Normatividad de la Inteligencia Artificial" (UAEMéx).

Este archivo solo contiene DATOS; knowledge.py lo importa al final y agrega:
    TOPICS_NUEVOS   -> se suman a TOPICS
    CONTACTS_NUEVOS -> se suman a CONTACTS
    SOURCES_NUEVAS  -> se suman a SOURCES

Las palabras clave van SIN acentos y en minúsculas (ver models.py):
  - frase con espacios: debe aparecer completa;  - "palabra$": palabra exacta;  - "palabra": prefijo.

Todo dato que cambia con el tiempo (leyes en trámite, fechas de aplicación) lleva la nota "verifica".
"""


def _tabla(encabezados, filas):
    th = "".join(f"<th class='border border-slate-300 p-1 text-left'>{h}</th>" for h in encabezados)
    cuerpo = ""
    for fila in filas:
        celdas = "".join(
            f"<td class='border border-slate-300 p-1 align-top{' font-semibold' if i == 0 else ''}'>{c}</td>"
            for i, c in enumerate(fila))
        cuerpo += f"<tr>{celdas}</tr>"
    return f"<table class='mt-3 text-xs border-collapse w-full'><tr class='bg-emerald-50'>{th}</tr>{cuerpo}</table>"


CONTACTS_NUEVOS = {
    "condusef": {"name": "CONDUSEF – quejas contra bancos, fintech y financieras",
                 "url": "https://www.condusef.gob.mx"},
    "cofepris": {"name": "COFEPRIS – regulación sanitaria (dispositivos médicos y software médico)",
                 "url": "https://www.gob.mx/cofepris"},
}

SOURCES_NUEVAS = [
    {"name": "Reglamento (UE) 2016/679 – RGPD", "url": "https://eur-lex.europa.eu/eli/reg/2016/679/oj"},
    {"name": "Reglamento (UE) 2022/2065 – Ley de Servicios Digitales (DSA)", "url": "https://eur-lex.europa.eu/eli/reg/2022/2065/oj"},
    {"name": "Reglamento (UE) 2022/1925 – Ley de Mercados Digitales (DMA)", "url": "https://eur-lex.europa.eu/eli/reg/2022/1925/oj"},
    {"name": "Directiva (UE) 2024/2853 – Responsabilidad por productos defectuosos", "url": "https://eur-lex.europa.eu/eli/dir/2024/2853/oj"},
    {"name": "Reglamento (UE) 2023/1230 – Máquinas", "url": "https://eur-lex.europa.eu/eli/reg/2023/1230/oj"},
    {"name": "Parlamento Europeo – Ley de IA de la UE: primera normativa sobre inteligencia artificial",
     "url": "https://www.europarl.europa.eu/topics/es/article/20230601STO93804/ley-de-ia-de-la-ue-primera-normativa-sobre-inteligencia-artificial"},
    {"name": "Blueprint for an AI Bill of Rights (OSTP, 2022)", "url": "https://bidenwhitehouse.archives.gov/ostp/ai-bill-of-rights/"},
    {"name": "Principios de la OCDE sobre IA", "url": "https://oecd.ai/en/ai-principles"},
    {"name": "Alianza Global sobre Inteligencia Artificial (GPAI)", "url": "https://gpai.ai"},
    {"name": "Convenio Marco del Consejo de Europa sobre IA, derechos humanos, democracia y Estado de derecho",
     "url": "https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence"},
    {"name": "OMS – Ética y gobernanza de la IA para la salud (2021)", "url": "https://www.who.int/publications/i/item/9789240029200"},
    {"name": "Código Civil Federal", "url": "https://www.diputados.gob.mx/LeyesBiblio/pdf/CCF.pdf"},
    {"name": "Código Nacional de Procedimientos Penales", "url": "https://www.diputados.gob.mx/LeyesBiblio/pdf/CNPP.pdf"},
    {"name": "Ley Federal del Trabajo", "url": "https://www.diputados.gob.mx/LeyesBiblio/pdf/LFT.pdf"},
]

TOPICS_NUEVOS = [
    # ====================================================================== PREGUNTAS FRECUENTES
    {
        "id": "origen_dh",
        "titulo": "¿Quién creó los derechos humanos? ¿Quién me los dio?",
        "emoji": "🏛️",
        "boton": "¿Quién creó mis derechos?",
        "relacionados": ["que_son_dh", "lista_dh", "persona_vs_animal"],
        "keywords": [
            ("quien creo los derechos", 12), ("quien me dio mis derechos", 12), ("quien me los dio", 12),
            ("quin me los dio", 12), ("me los dio", 8), ("quien los creo", 10), ("quien los dio", 9),
            ("quien dio los derechos", 12), ("quien otorga los derechos", 12), ("quien me otorgo", 10),
            ("quien invento los derechos", 12), ("quien establecio los derechos", 11), ("quien hizo los derechos", 11),
            ("de donde vienen los derechos", 12), ("de donde salen los derechos", 12), ("de donde vienen mis derechos", 12),
            ("origen de los derechos", 11), ("origen de los derechos humanos", 12), ("historia de los derechos humanos", 12),
            ("quien da los derechos", 12), ("quien decide mis derechos", 10), ("quin creo", 8),
        ],
        "intro": (
            "<b>Respuesta corta:</b> nadie te los “dio”. Los derechos humanos se entienden como <b>inherentes a tu dignidad</b> desde que naces; "
            "las leyes y los Estados no los inventan: <b>los reconocen, los protegen y los garantizan</b>. "
            "Por eso la Constitución cambió su lenguaje en 2011: antes el Art. 1° hablaba de las “<i>garantías que otorga</i> esta Constitución” "
            "y hoy dice que todas las personas gozan de los “<i>derechos humanos reconocidos</i>” en ella y en los tratados internacionales (reforma del DOF del 10-jun-2011)."
            "<div class='mt-2 text-sm'><b>Matiz:</b> en la teoría del derecho hay dos posturas. Para el <i>iusnaturalismo</i> los derechos existen antes de cualquier ley; "
            "para el <i>positivismo</i> existen jurídicamente cuando una norma los reconoce. Hoy conviven: la idea nace de la dignidad y la ley los vuelve exigibles.</div>"
        ),
        "derechos_titulo": "Cómo se fueron reconociendo (línea del tiempo)",
        "derechos": [
            "<b>1215 – Carta Magna</b> (Inglaterra): limita el poder del rey. <b>1689 – Bill of Rights</b> inglés.",
            "<b>1776 – Declaración de Independencia</b> de EE. UU. y <b>1789 – Declaración de los Derechos del Hombre y del Ciudadano</b> (Francia): derechos “naturales” e iguales.",
            "<b>1917 – Constitución mexicana:</b> una de las primeras del mundo en reconocer <b>derechos sociales</b> (educación, Art. 3°; trabajo, Art. 123).",
            "<b>1945 – Carta de la ONU.</b> <b>10-dic-1948 – Declaración Universal de los Derechos Humanos</b>, aprobada por la Asamblea General de la ONU tras las atrocidades de la Segunda Guerra Mundial.",
            "<b>1966 – Pactos Internacionales</b> (derechos civiles y políticos; y económicos, sociales y culturales). <b>1969 – Convención Americana</b> (Pacto de San José), a la que México se adhirió en 1981.",
            "<b>2011 – Reforma constitucional en México:</b> los tratados de derechos humanos tienen rango constitucional y rige el principio <i>pro persona</i> (se aplica la norma que más te proteja).",
        ],
        "pasos_titulo": "¿Quién tiene la obligación de respetarlos?",
        "pasos": [
            "<b>Todas las autoridades</b>, en el ámbito de sus competencias, deben <b>promover, respetar, proteger y garantizar</b> los derechos humanos (CPEUM Art. 1°, párrafo tercero).",
            "Si una autoridad los viola, puedes acudir a la <b>CODHEM</b> o a la <b>CNDH</b> (quejas) y a los jueces (por ejemplo, el juicio de amparo).",
            "En la universidad, la <b>Defensoría de los Derechos Universitarios</b> atiende quejas de la comunidad.",
            "Tus derechos <b>no dependen</b> de que alguien te los otorgue ni de que los conozcas; pero conocerlos te permite exigirlos.",
        ],
        "contactos": ["codhem", "cndh", "defensoria_uaemex"],
        "fundamento": "CPEUM Art. 1° (reforma DOF 10-jun-2011); Declaración Universal de los Derechos Humanos (ONU, 10-dic-1948), Preámbulo y Art. 1; Convención Americana sobre Derechos Humanos.",
    },
    {
        "id": "acoso_como_saber",
        "titulo": "¿Cómo sé si estoy siendo víctima de acoso?",
        "emoji": "🔎",
        "boton": "¿Cómo sé si me acosan?",
        "relacionados": ["acoso_hostigamiento", "violentometro", "ley_olimpia", "violencia_docente"],
        "keywords": [
            ("como se si estoy siendo victima de acoso", 14), ("como saber si soy victima de acoso", 14),
            ("como se si soy victima de acoso", 14), ("como se si me acosan", 12), ("como saber si me acosan", 12),
            ("como saber si es acoso", 12), ("como se si es acoso", 12), ("como identificar el acoso", 11),
            ("como identificar acoso", 11), ("senales de acoso", 11), ("senales de que me acosan", 12),
            ("que es el acoso", 9), ("que es acoso", 9), ("que es el hostigamiento", 9), ("diferencia entre acoso y hostigamiento", 14),
            ("estoy siendo acosad", 8), ("victima de acoso", 7), ("me estan acosando", 6), ("es acoso", 6),
        ],
        "intro": (
            "El <b>acoso</b> es una conducta <b>no deseada</b> que se repite, o que abusa de un poder, y que te intimida, te incomoda o te daña. "
            "<b>No necesitas estar 100 % segura/o para pedir orientación</b>: dudar es normal, sobre todo si quien lo hace tiene autoridad sobre ti. "
            "Hazte estas cuatro preguntas:"
        ),
        "derechos_titulo": "Las 4 preguntas clave",
        "derechos": [
            "<b>¿Es no deseado?</b> No lo pediste, no lo consentiste o dijiste que no y siguió. Un cumplido mutuo o una amistad en la que ambos están cómodos no es acoso.",
            "<b>¿Hay insistencia o abuso de poder?</b> Se repite, o viene de alguien con poder sobre ti (profesor/a, jefe/a, líder de equipo). En el <b>acoso sexual</b> basta un solo evento si hay abuso de poder que te deja en indefensión.",
            "<b>¿Te hace sentir miedo, vergüenza, culpa o inseguridad?</b> Evitas lugares, personas o clases; cambias tu rutina; te cuesta concentrarte o dormir.",
            "<b>¿Te afecta en la escuela, el trabajo o tu vida?</b> Bajan tus calificaciones, faltas, temes represalias si dices que no.",
        ],
        "pasos_titulo": "Señales y tipos",
        "pasos": [
            "<b>Señales frecuentes:</b> piropos o comentarios sexuales; insistencia después de un “no”; mensajes o llamadas constantes; que te siga o vigile; tocamientos; "
            "propuestas de favores a cambio de calificaciones o beneficios; burlas, apodos o humillaciones repetidas; rumores o difusión de imágenes tuyas; te aíslan; represalias si lo rechazas.",
            "<b>Hostigamiento sexual:</b> hay <b>subordinación</b> (profesor/a–estudiante, jefe/a–empleado/a) y conductas de connotación lasciva. <b>Acoso sexual:</b> no hay subordinación, pero sí un abuso de poder que te deja en indefensión o riesgo (Ley General de Acceso de las Mujeres, Art. 13).",
            "<b>Otros tipos:</b> acoso escolar (bullying), laboral, digital o ciberacoso (puede ser delito: Ley Olimpia), y acoso en la pareja (revisa el violentómetro).",
            "<b>Si respondiste “sí” a dos o más preguntas</b>, toma en serio lo que sientes: guarda evidencia (mensajes, capturas, fechas, testigos) y pide orientación. No es tu culpa.",
            "Si estás en peligro ahora, llama al <b>911</b>. Para saber <b>qué hacer paso a paso</b>, abre el tema “Acoso o violencia de género”.",
        ],
        "contactos": ["sin_violencia", "defensoria_uaemex", "uaemex_psico", "fgjem", "911"],
        "fundamento": "Ley General de Acceso de las Mujeres a una Vida Libre de Violencias, Arts. 6 y 13; Ley de Acceso de las Mujeres a una Vida Libre de Violencia del Estado de México; Ley Olimpia (Edomex).",
    },
    {
        "id": "abuso_laboral_como_saber",
        "titulo": "¿Cómo sé si sufro abuso laboral?",
        "emoji": "💼",
        "boton": "¿Cómo sé si sufro abuso laboral?",
        "relacionados": ["abuso_laboral", "caso_laboral", "acoso_como_saber", "donde_ayuda"],
        "keywords": [
            ("como se si sufro abuso laboral", 14), ("como saber si sufro abuso laboral", 14), ("como saber si es abuso laboral", 13),
            ("como se si es abuso laboral", 13), ("como saber si hay abuso laboral", 13), ("como se si me explotan", 12),
            ("como saber si me explotan", 12), ("senales de abuso laboral", 12), ("como identificar el abuso laboral", 12),
            ("como identificar abuso laboral", 12), ("como saber si hay acoso laboral", 12), ("como se si sufro acoso laboral", 13),
            ("soy victima de abuso laboral", 12), ("es abuso laboral", 9), ("estoy sufriendo abuso laboral", 12),
            ("me estan explotando en el trabajo", 11), ("trato digno en el trabajo", 8),
        ],
        "intro": (
            "El <b>abuso laboral</b> es toda conducta en el trabajo que daña tu <b>dignidad, salud, libertad o derechos</b>. "
            "Para saber si lo estás viviendo, revisa estas cuatro áreas. Si en <b>una o más</b> aparecen varias señales, merece atención:"
        ),
        "derechos_titulo": "Revisa estas 4 áreas",
        "derechos": [
            "<b>1) Trato:</b> gritos, humillaciones, burlas, amenazas de despido, aislamiento, tareas imposibles o degradantes, vigilancia excesiva, castigos por quejarte.",
            "<b>2) Condiciones:</b> no te pagan o te pagan menos de lo pactado; no te dan aguinaldo (mínimo 15 días de salario, LFT Art. 87) ni las prestaciones de ley; no te inscriben al seguro social; "
            "horas extra sin pago; te piden firmar renuncias en blanco o te presionan para renunciar.",
            "<b>3) Discriminación o acoso:</b> te tratan distinto por género, edad, embarazo, discapacidad, origen, religión u orientación; comentarios o contacto sexual no deseado; pruebas de embarazo como requisito.",
            "<b>4) Salud y libertad:</b> ansiedad, insomnio, miedo de ir a trabajar; en casos graves, te retienen documentos o dinero, te impiden salir o te imponen deudas (puede ser trata o trabajo forzoso).",
        ],
        "pasos_titulo": "Cómo distinguirlo de una exigencia normal",
        "pasos": [
            "<b>Una exigencia no es abuso:</b> pedir resultados, evaluar tu desempeño o llamarte la atención de forma justificada y respetuosa es parte del trabajo.",
            "<b>Sí es señal de abuso</b> cuando la conducta es <b>humillante, desproporcionada, discriminatoria, repetida</b> o contradice la ley o tu contrato. Según el Convenio 190 de la OIT, puede bastar <b>una sola vez</b> si causa o puede causar daño.",
            "<b>Prueba rápida:</b> (a) ¿daña mi dignidad o mi salud? (b) ¿contradice la ley o lo acordado? (c) ¿se repite o hay abuso de poder? Con dos “sí”, documenta y consulta.",
            "<b>Siguiente paso:</b> anota fechas, hechos y testigos; guarda contrato, recibos y mensajes; no firmes nada bajo presión. Después abre el tema “Abuso laboral” para ver a dónde acudir (PROFEDET, CODHEM, Ministerio Público).",
            "Si eres practicante, becario/a o haces servicio social, <b>conservas tus derechos humanos</b>; avisa también a tu Facultad.",
        ],
        "contactos": ["profedet", "ipn_violentometro_laboral", "sin_violencia", "fgjem", "defensoria_uaemex"],
        "fundamento": "CPEUM Art. 123; Ley Federal del Trabajo, Arts. 3 y 87; Convenio 190 de la OIT, Art. 1; NOM-035-STPS-2018.",
    },

    # ====================================================================== PUENTES POR UNIDAD
    {
        "id": "unidad3_hub",
        "titulo": "Unidad 3 – Marco jurídico internacional de la IA",
        "emoji": "🌐",
        "boton": "Unidad 3: marco internacional",
        "relacionados": ["ue_modelo_rgpd", "ue_ai_act", "ue_dsa_dma", "eeuu_blueprint", "ia_nist_rmf", "ia_eeuu_vs_ue",
                         "ocde_gpai", "ia_unesco", "latam_ia"],
        "keywords": [
            ("unidad 3", 12), ("unidad tres", 12), ("unidad iii", 12), ("marco juridico internacional", 14),
            ("marco internacional de la ia", 12), ("regulacion internacional de la ia", 12), ("derecho internacional de la ia", 12),
            ("organismos internacionales de referencia", 12), ("modelos regulatorios internacionales", 12),
        ],
        "intro": (
            "La <b>Unidad 3</b> compara los modelos de regulación de la IA en el mundo para identificar buenas prácticas. Elige un subtema:"
            "<ul class='list-disc pl-5 mt-2 space-y-1'>"
            "<li><b>3.1 Unión Europea:</b> modelo de derechos y regulación proactiva, RGPD, AI Act, Ley de Servicios y de Mercados Digitales.</li>"
            "<li><b>3.2 Estados Unidos:</b> Blueprint for an AI Bill of Rights y NIST AI RMF.</li>"
            "<li><b>3.3 Organismos multilaterales:</b> OCDE, UNESCO y Foro/Alianza Global sobre IA (GPAI).</li>"
            "<li><b>3.4 Estrategias latinoamericanas.</b></li>"
            "<li><b>Comparativa</b> Unión Europea vs. Estados Unidos.</li>"
            "</ul>"
        ),
        "fundamento": "Programa de Normatividad de la IA (UAEMéx), Unidad temática 3.",
    },
    {
        "id": "unidad4_hub",
        "titulo": "Unidad 4 – Áreas específicas de regulación en IA",
        "emoji": "⚖️",
        "boton": "Unidad 4: áreas de regulación",
        "relacionados": ["ia_derechos_humanos", "datos_y_derechos_humanos", "ia_sesgos", "ia_libertad_expresion",
                         "ia_responsabilidad", "ia_salud_finanzas", "ia_seguridad_educacion_empleo",
                         "ia_alto_riesgo", "ia_generativa", "ia_vehiculos_robots"],
        "keywords": [
            ("unidad 4", 12), ("unidad cuatro", 12), ("unidad iv", 12), ("areas especificas de regulacion", 14),
            ("areas de regulacion de la ia", 12), ("areas criticas de la ia", 12), ("regulacion sectorial de la ia", 12),
            ("areas criticas en tecnologias", 12),
        ],
        "intro": (
            "La <b>Unidad 4</b> analiza las áreas críticas de la IA con implicaciones jurídicas y éticas. Elige un subtema:"
            "<ul class='list-disc pl-5 mt-2 space-y-1'>"
            "<li><b>4.1 IA y derechos humanos:</b> privacidad y datos, no discriminación y sesgos, libertad de expresión y contenidos generados por IA.</li>"
            "<li><b>4.2 Responsabilidad y rendición de cuentas:</b> civil y penal.</li>"
            "<li><b>4.3 Regulación sectorial:</b> salud, finanzas, seguridad pública y vigilancia, educación y empleo.</li>"
            "<li><b>4.4 Tecnologías críticas:</b> algoritmos de alto riesgo, IA generativa, vehículos autónomos, robots y sistemas autónomos.</li>"
            "</ul>"
        ),
        "fundamento": "Programa de Normatividad de la IA (UAEMéx), Unidad temática 4.",
    },

    # ====================================================================== UNIDAD 3 – UNIÓN EUROPEA
    {
        "id": "ue_modelo_rgpd",
        "titulo": "Unión Europea: modelo de derechos y RGPD",
        "emoji": "🇪🇺",
        "boton": "UE: modelo de derechos y RGPD",
        "relacionados": ["ue_ai_act", "ue_dsa_dma", "datos_y_derechos_humanos", "ia_eeuu_vs_ue"],
        "keywords": [
            ("rgpd", 10), ("gdpr", 10), ("reglamento general de proteccion de datos", 12),
            ("modelo europeo de derechos", 10), ("modelo de proteccion de derechos", 10), ("regulacion proactiva", 10),
            ("proteccion de datos en la union europea", 11), ("proteccion de datos en europa", 11),
            ("decisiones automatizadas rgpd", 12), ("derecho a no ser objeto de decisiones", 12),
            ("carta de los derechos fundamentales", 10), ("derecho al olvido", 8), ("evaluacion de impacto relativa a la proteccion de datos", 11),
            ("dpia", 9), ("perfilado", 6), ("profiling", 6), ("articulo 22 del rgpd", 12), ("impacto del rgpd", 12),
        ],
        "intro": (
            "El <b>modelo europeo</b> parte de que la tecnología debe servir a los <b>derechos fundamentales</b> y regula <b>de forma proactiva</b> (antes de que ocurra el daño), "
            "con leyes generales y obligatorias. Su base es la <b>Carta de los Derechos Fundamentales de la UE</b> (Art. 7, vida privada; Art. 8, protección de datos; Art. 21, no discriminación; Art. 47, tutela judicial efectiva). "
            "El <b>RGPD</b> (Reglamento (UE) 2016/679, aplicable desde el <b>25-may-2018</b>) es su pieza central para la IA, porque casi toda IA usa datos personales."
        ),
        "derechos_titulo": "Qué exige el RGPD (y por qué importa a la IA)",
        "derechos": [
            "<b>Principios (Art. 5):</b> licitud, lealtad y transparencia; limitación de la finalidad; <b>minimización</b> de datos; exactitud; limitación del plazo; integridad y confidencialidad; y <b>responsabilidad proactiva</b>.",
            "<b>Derechos de las personas (Arts. 12 a 22):</b> información, acceso, rectificación, supresión (“derecho al olvido”), limitación, portabilidad, oposición y <b>no ser objeto de decisiones basadas únicamente en tratamiento automatizado</b>.",
            "<b>Art. 22 – decisiones automatizadas:</b> tienes derecho a no ser sometido a una decisión únicamente automatizada, incluida la elaboración de perfiles, con efectos jurídicos o que te afecte significativamente. "
            "Hay excepciones (contrato, ley, consentimiento explícito), pero siempre con salvaguardas: <b>intervención humana, expresar tu punto de vista e impugnar la decisión</b>.",
            "<b>Datos sensibles (Art. 9):</b> origen racial, opiniones políticas, religión, salud, biometría para identificar, vida sexual; su tratamiento está prohibido salvo excepciones.",
            "<b>Privacidad desde el diseño y por defecto (Art. 25)</b> y <b>evaluación de impacto (Art. 35)</b> cuando el tratamiento, como la evaluación sistemática automatizada de personas, implique un alto riesgo.",
            "<b>Alcance extraterritorial (Art. 3):</b> aplica también a empresas fuera de la UE que ofrecen bienes o servicios a personas en la UE o vigilan su comportamiento. <b>Multas (Art. 83):</b> hasta 20 millones de euros o el 4 % del volumen de negocio mundial.",
        ],
        "pasos_titulo": "Impacto en la IA y ejemplos",
        "pasos": [
            "<b>Entrenar modelos</b> exige una base jurídica, minimizar datos y poder explicar el tratamiento: choca con la idea de “usar todos los datos disponibles”.",
            "<b>Ejemplos:</b> autoridades de Italia, Francia y Grecia multaron a <b>Clearview AI</b> por extraer imágenes faciales de internet; el regulador italiano limitó temporalmente ChatGPT en 2023 y multó a OpenAI con 15 millones de euros en diciembre de 2024 (verifica el estado de los recursos).",
            "<b>Relación con el AI Act:</b> son leyes <b>complementarias</b>; el AI Act no sustituye al RGPD, y ambos pueden aplicarse a un mismo sistema.",
            "<b>Para México:</b> la lógica de derechos ARCO y datos sensibles es parecida; la diferencia es el nivel de exigencia, las sanciones y el derecho expreso frente a decisiones automatizadas.",
        ],
        "contactos": [],
        "fundamento": "Reglamento (UE) 2016/679 (RGPD), Arts. 3, 5, 9, 12 a 22, 25, 35 y 83; Carta de los Derechos Fundamentales de la UE, Arts. 7, 8, 21 y 47; Programa de Normatividad de la IA, Unidad 3 (3.1.1 y 3.1.2).",
    },
    {
        "id": "ue_ai_act",
        "titulo": "AI Act: Reglamento de Inteligencia Artificial de la UE",
        "emoji": "📜",
        "boton": "AI Act (Ley de IA de la UE)",
        "relacionados": ["ia_alto_riesgo", "ia_requisitos", "ia_generativa", "ia_eeuu_vs_ue", "ue_modelo_rgpd"],
        "keywords": [
            ("ai act", 11), ("ley de ia de la union europea", 13), ("ley de ia de la ue", 13), ("ley de ia de europa", 13), ("ley de ia europea", 13), ("ley europea de ia", 13), ("ley de ia en europa", 13), ("ley de inteligencia artificial de la union europea", 13),
            ("reglamento de inteligencia artificial", 11), ("reglamento 2024 1689", 12), ("reglamento ue 2024 1689", 12),
            ("niveles de riesgo", 8), ("piramide de riesgo", 10), ("calendario del ai act", 12), ("cuando entra en vigor el ai act", 12),
            ("modelos de ia de proposito general", 11), ("oficina europea de ia", 10), ("que es el ai act", 13), ("que dice el ai act", 13),
        ],
        "intro": (
            "El <b>Reglamento (UE) 2024/1689</b> es la <b>primera ley horizontal sobre IA</b> del mundo. Entró en vigor el <b>1-ago-2024</b> y usa un <b>enfoque basado en riesgo</b>. "
            "Aplica a quien <b>proporciona o despliega</b> IA en la UE, aunque esté fuera de ella (Art. 2), y excluye usos militares, de defensa y seguridad nacional."
            + _tabla(
                ["Nivel", "Qué significa", "Ejemplos"],
                [
                    ["Inaceptable", "<b>Prohibido</b> (Art. 5)", "Manipulación, explotar vulnerabilidades, puntuación social, inferir emociones en escuelas y trabajos"],
                    ["Alto riesgo", "Permitido con <b>requisitos estrictos</b> (Arts. 6 a 49; Anexos I y III)", "Empleo, educación, crédito, biometría, justicia, productos como dispositivos médicos"],
                    ["Transparencia", "Obligaciones de <b>avisar</b> (Art. 50)", "Chatbots, deepfakes y contenido sintético"],
                    ["Riesgo mínimo", "Sin obligaciones; códigos voluntarios", "Filtros de spam, videojuegos"],
                ])
        ),
        "derechos_titulo": "Piezas clave",
        "derechos": [
            "<b>Modelos de IA de propósito general (Cap. V, Arts. 51 a 56):</b> documentación técnica, información a quienes los integran, <b>política de derechos de autor</b> y resumen público de los datos de entrenamiento. "
            "Si tienen <b>riesgo sistémico</b> (se presume cuando el entrenamiento supera 10²⁵ operaciones de cálculo), además: evaluaciones, pruebas adversarias, reporte de incidentes y ciberseguridad.",
            "<b>Alfabetización en IA (Art. 4):</b> quien usa IA en una organización debe contar con conocimientos suficientes.",
            "<b>Derechos de las personas:</b> presentar una <b>reclamación</b> ante la autoridad de vigilancia del mercado (Art. 85) y recibir una <b>explicación</b> de decisiones individuales con sistemas de alto riesgo (Art. 86).",
            "<b>Gobernanza:</b> Oficina Europea de IA, Comité de IA y autoridades nacionales. <b>Sanciones (Art. 99):</b> hasta 35 millones de euros o 7 % del volumen de negocio mundial.",
        ],
        "pasos_titulo": "Calendario (verifica fechas vigentes)",
        "pasos": [
            "<b>2-feb-2025:</b> aplican las prohibiciones (Art. 5) y la alfabetización en IA. <b>2-ago-2025:</b> reglas para modelos de propósito general y gobernanza.",
            "<b>2-ago-2026:</b> fecha general de aplicación prevista originalmente. En 2026 la UE acordó con el <b>Digital Omnibus</b> aplazar el <b>alto riesgo del Anexo III a 2-dic-2027</b> y el del <b>Anexo I a 2-ago-2028</b>, "
            "y añadir una prohibición de sistemas que generen material de abuso sexual infantil o contenido íntimo no consentido a partir del 2-dic-2026 (acuerdo político de mayo de 2026; confirma el texto final publicado).",
            "<b>Para ti como ingeniero/a:</b> si tu sistema se usa en la UE, aplica aunque lo desarrolles en México. Clasifica tu sistema por nivel de riesgo y documenta datos, pruebas y supervisión humana.",
        ],
        "contactos": [],
        "fundamento": "Reglamento (UE) 2024/1689, Arts. 2, 4, 5, 6, 50, 51 a 56, 85, 86 y 99 y Anexos I y III; Comisión Europea y Parlamento Europeo (Digital Omnibus, 2026); Programa de Normatividad de la IA, Unidad 3 (3.1.3).",
    },
    {
        "id": "ue_dsa_dma",
        "titulo": "Ley de Servicios Digitales (DSA) y Ley de Mercados Digitales (DMA)",
        "emoji": "🖥️",
        "boton": "UE: DSA y DMA (plataformas)",
        "relacionados": ["ue_ai_act", "ue_modelo_rgpd", "ia_libertad_expresion", "ia_eeuu_vs_ue"],
        "keywords": [
            ("ley de servicios digitales", 13), ("ley de mercados digitales", 13), ("digital services act", 13), ("digital markets act", 13),
            ("servicios digitales y mercados digitales", 14), ("dsa$", 9), ("dma$", 9), ("plataformas muy grandes", 10),
            ("guardianes de acceso", 10), ("gatekeeper", 9), ("patrones oscuros", 8), ("dark patterns", 8),
            ("sistemas de recomendacion", 6), ("moderacion de contenidos en la union europea", 12),
        ],
        "intro": (
            "Son dos leyes europeas que regulan a las <b>plataformas digitales</b>, donde operan los algoritmos de recomendación, moderación y publicidad. "
            "Complementan al RGPD y al AI Act."
            + _tabla(
                ["", "DSA – Servicios Digitales", "DMA – Mercados Digitales"],
                [
                    ["Norma", "Reglamento (UE) 2022/2065", "Reglamento (UE) 2022/1925"],
                    ["Objetivo", "Entorno en línea <b>seguro</b> y protección de derechos fundamentales", "Mercados digitales <b>justos y abiertos</b> (competencia)"],
                    ["A quién aplica", "Intermediarios, plataformas y, con más reglas, <b>plataformas y buscadores muy grandes</b> (45 millones o más de usuarios mensuales en la UE)", "<b>“Guardianes de acceso”</b> (gatekeepers) designados por la Comisión"],
                    ["Multas máximas", "Hasta 6 % del volumen de negocio mundial (Art. 52)", "Hasta 10 % (20 % si reinciden)"],
                ])
        ),
        "derechos_titulo": "DSA: qué cambia para las personas",
        "derechos": [
            "<b>Contenido ilícito:</b> mecanismos para notificarlo y que la plataforma actúe; si te moderan o suspenden, deben darte <b>los motivos</b> y vías de <b>recurso</b>, incluso extrajudicial.",
            "<b>Publicidad y menores:</b> se prohíbe la publicidad basada en perfiles de menores (Art. 28) y la basada en datos sensibles (Art. 26); se prohíben los <b>patrones oscuros</b> que manipulan decisiones (Art. 25).",
            "<b>Transparencia de los algoritmos de recomendación;</b> las plataformas muy grandes deben ofrecer una opción <b>sin perfilado</b> (Art. 38), evaluar <b>riesgos sistémicos</b> (desinformación, procesos electorales, derechos fundamentales) y someterse a <b>auditorías independientes</b> (Arts. 34 y 37).",
            "Aplicación general desde el <b>17-feb-2024</b>.",
        ],
        "pasos_titulo": "DMA y relación con la IA",
        "pasos": [
            "<b>DMA:</b> prohíbe, por ejemplo, favorecer los propios servicios en los resultados y <b>combinar datos personales</b> de distintos servicios sin consentimiento (Art. 5); exige interoperabilidad en ciertos casos. Aplicable desde el 2-may-2023.",
            "<b>Con la IA:</b> los sistemas de recomendación, la publicidad dirigida y la IA generativa integrada en plataformas quedan bajo estas reglas, además del AI Act (Art. 50, etiquetado de contenido sintético).",
            "<b>Lección para México:</b> no existe una norma equivalente; la moderación y la publicidad se rigen por leyes generales (datos personales, consumo, telecomunicaciones). Hay iniciativas en discusión (verifica).",
        ],
        "contactos": [],
        "fundamento": "Reglamento (UE) 2022/2065 (DSA), Arts. 20, 21, 25, 26, 28, 34, 37, 38 y 52; Reglamento (UE) 2022/1925 (DMA), Art. 5; Programa de Normatividad de la IA, Unidad 3 (3.1.4).",
    },

    # ====================================================================== UNIDAD 3 – ESTADOS UNIDOS
    {
        "id": "eeuu_blueprint",
        "titulo": "Estados Unidos: Blueprint for an AI Bill of Rights",
        "emoji": "🇺🇸",
        "boton": "EE. UU.: AI Bill of Rights",
        "relacionados": ["ia_nist_rmf", "ia_eeuu_vs_ue", "ia_detectar_vulneracion", "ia_requisitos"],
        "keywords": [
            ("blueprint for an ai bill of rights", 14), ("blueprint for an ai", 12), ("ai bill of rights", 12),
            ("carta de derechos de la ia", 12), ("declaracion de derechos de la ia", 12), ("carta de derechos de la inteligencia artificial", 13),
            ("principios de la casa blanca", 11), ("cinco principios de la casa blanca", 13), ("proteccion contra la discriminacion algoritmica", 11),
            ("alternativas humanas", 9), ("aviso y explicacion", 9), ("regulacion reactiva", 9), ("modelo de proteccion de derechos de estados unidos", 12),
            ("modelo estadounidense de derechos", 12),
        ],
        "intro": (
            "El <b>Blueprint for an AI Bill of Rights</b> (<i>Anteproyecto para una Carta de Derechos de la IA</i>) fue publicado en <b>octubre de 2022</b> por la Oficina de Política Científica y Tecnológica (OSTP) de la Casa Blanca. "
            "Es una <b>guía no vinculante</b>: no crea derechos exigibles ni sanciones, pero orienta cómo diseñar y usar <b>sistemas automatizados</b> que puedan afectar tus derechos, oportunidades o acceso a servicios esenciales. "
            "Hoy se consulta en el archivo de la administración anterior."
        ),
        "derechos_titulo": "Los 5 principios",
        "derechos": [
            "<b>1) Sistemas seguros y eficaces:</b> consulta a las personas afectadas, pruebas antes del uso y monitoreo continuo.",
            "<b>2) Protección contra la discriminación algorítmica:</b> evaluaciones de equidad desde el diseño, uso de datos representativos, accesibilidad y reportes públicos.",
            "<b>3) Privacidad de los datos:</b> recoger solo lo necesario, consentimiento significativo, protección reforzada para datos sensibles y límites a la vigilancia.",
            "<b>4) Aviso y explicación:</b> saber <b>que se usa</b> un sistema automatizado y <b>cómo contribuyó</b> al resultado, en lenguaje claro.",
            "<b>5) Alternativas, consideración y respaldo humanos:</b> poder <b>optar por no usarlo</b> y acudir a una persona; contar con una vía para apelar.",
        ],
        "pasos_titulo": "El modelo estadounidense frente al europeo",
        "pasos": [
            "<b>Enfoque:</b> en EE. UU. la protección de derechos se apoya en <b>leyes sectoriales ya existentes</b> (consumo, empleo, crédito, salud) y guías voluntarias; las agencias actúan sobre todo <b>después</b> del daño (FTC contra prácticas engañosas, EEOC y leyes de igualdad en el empleo, protección al consumidor financiero). "
            "La UE, en cambio, regula <b>antes</b> (ex ante) con una ley horizontal obligatoria.",
            "<b>Estado actual:</b> no hay ley federal general de IA (hasta donde se pudo verificar, nov. 2026). La orden ejecutiva de 2023 fue revocada en enero de 2025 y los estados (California, Colorado, Texas y otros) han legislado por su cuenta; confirma su situación.",
            "<b>Complemento técnico:</b> el <b>NIST AI RMF</b> (2023) traduce estos principios en prácticas de gestión de riesgos; pregunta por “NIST AI RMF”.",
            "Para ver la <b>comparación punto por punto</b> con la UE, abre “EE. UU. vs. Unión Europea”.",
        ],
        "contactos": [],
        "fundamento": "Blueprint for an AI Bill of Rights, OSTP, Casa Blanca (octubre de 2022); NIST AI RMF 1.0 (2023); Programa de Normatividad de la IA, Unidad 3 (3.2.1 y 3.2.2).",
    },

    # ====================================================================== UNIDAD 3 – MULTILATERALES Y LATAM
    {
        "id": "ocde_gpai",
        "titulo": "OCDE y Alianza Global sobre IA (GPAI): organismos multilaterales",
        "emoji": "🤝",
        "boton": "OCDE y GPAI",
        "relacionados": ["ia_unesco", "latam_ia", "ia_eeuu_vs_ue", "unidad3_hub"],
        "keywords": [
            ("principios de la ocde", 13), ("ocde y la ia", 12), ("ocde ia", 11), ("ocde$", 6), ("oecd$", 6), ("principios de la oecd", 13),
            ("gpai$", 9), ("foro global sobre ia", 14), ("foro global sobre inteligencia artificial", 14), ("alianza global sobre inteligencia artificial", 14),
            ("alianza global sobre ia", 14), ("global partnership on ai", 13), ("global partnership on artificial intelligence", 13),
            ("organismos multilaterales", 11), ("organismos internacionales", 8), ("convenio marco del consejo de europa", 12),
            ("consejo de europa y la ia", 12), ("tratado internacional de ia", 10),
        ],
        "intro": (
            "Además de las leyes de cada país, hay organismos que fijan <b>estándares y principios comunes</b> de IA. Casi todos son <b>voluntarios</b> (soft law), "
            "pero influyen en las leyes nacionales. Para la <b>UNESCO</b> abre “Ética de la IA (UNESCO)”."
        ),
        "derechos_titulo": "OCDE – Principios sobre IA",
        "derechos": [
            "La <b>Recomendación del Consejo de la OCDE sobre IA</b> se adoptó el <b>22-may-2019</b> y se <b>actualizó en mayo de 2024</b>. Es el <b>primer estándar intergubernamental</b> sobre IA; más de 40 países la han adoptado, entre ellos México.",
            "<b>Cinco principios basados en valores:</b> (1) crecimiento inclusivo, desarrollo sostenible y bienestar; (2) respeto del <b>Estado de derecho, los derechos humanos y los valores democráticos</b>, incluidas la equidad y la privacidad; (3) <b>transparencia y explicabilidad</b>; (4) solidez, seguridad y protección; (5) <b>rendición de cuentas</b>.",
            "<b>Cinco recomendaciones a los gobiernos:</b> invertir en investigación y desarrollo; fomentar un ecosistema digital; crear un entorno de políticas favorable; desarrollar capacidades humanas; y cooperar internacionalmente.",
            "La actualización de 2024 añadió temas como <b>desinformación</b>, mecanismos para <b>desactivar o corregir</b> sistemas y sostenibilidad ambiental. Su definición de “sistema de IA” inspiró la del AI Act.",
        ],
        "pasos_titulo": "GPAI y otros acuerdos",
        "pasos": [
            "<b>GPAI (Global Partnership on AI / Alianza Global sobre IA):</b> iniciativa lanzada en <b>junio de 2020</b> por 15 miembros fundadores, entre ellos <b>México</b>. Reúne gobiernos, industria, sociedad civil y academia en grupos de trabajo (IA responsable, gobernanza de datos, futuro del trabajo, innovación). "
            "En 2024 se integró con la OCDE (verifica la composición actual).",
            "<b>Consejo de Europa:</b> el <b>Convenio Marco sobre IA, derechos humanos, democracia y Estado de derecho</b> (abierto a firma en septiembre de 2024) es el <b>primer tratado internacional vinculante</b> sobre IA y está abierto a países no europeos.",
            "<b>ONU:</b> en marzo de 2024 la Asamblea General adoptó por consenso su primera resolución sobre sistemas de IA seguros y fiables para el desarrollo sostenible.",
            "<b>Tendencia:</b> la <b>armonización internacional</b> busca principios comunes (transparencia, no discriminación, supervisión humana, rendición de cuentas) aunque cada región legisle distinto.",
        ],
        "contactos": [],
        "fundamento": "Recomendación del Consejo de la OCDE sobre IA (OECD/LEGAL/0449; 2019, actualizada en 2024); Alianza Global sobre IA (GPAI); Convenio Marco del Consejo de Europa sobre IA (2024); Programa de Normatividad de la IA, Unidad 3 (3.3).",
    },
    {
        "id": "latam_ia",
        "titulo": "Estrategias y regulación de la IA en América Latina",
        "emoji": "🌎",
        "boton": "IA en Latinoamérica",
        "relacionados": ["ia_eeuu_vs_ue", "ocde_gpai", "ia_unesco", "unidad3_hub"],
        "keywords": [
            ("estrategias latinoamericanas", 13), ("estrategias latinoamericanas sobre ia", 14), ("america latina", 7), ("latinoamerica", 7),
            ("regulacion de la ia en america latina", 14), ("regulacion de la ia en latinoamerica", 14), ("ia en latinoamerica", 12),
            ("ia en america latina", 12), ("ia en brasil", 12), ("ia en chile", 12), ("ia en peru", 12), ("ia en colombia", 12),
            ("ia en argentina", 12), ("ia en uruguay", 12), ("pl 2338", 12), ("ley de ia de brasil", 13), ("ley de ia de peru", 13),
            ("ley 31814", 12), ("conpes 3975", 12), ("declaracion de santiago", 11), ("brasil", 3), ("peru$", 3), ("colombia", 3),
            ("regula brasil", 12), ("regula peru", 12), ("regula chile", 12), ("regula colombia", 12), ("regula argentina", 12), ("regula uruguay", 12),
            ("regulacion en brasil", 12), ("regulacion en peru", 12), ("regulacion en chile", 12), ("regulacion en colombia", 12), ("regulacion en argentina", 12),
            ("inteligencia artificial en brasil", 12), ("inteligencia artificial en peru", 12), ("inteligencia artificial en chile", 12), ("inteligencia artificial en colombia", 12),
        ],
        "intro": (
            "En la región <b>no hay una ley común</b>. La mayoría combina <b>estrategias nacionales</b> (políticas públicas) con <b>proyectos de ley</b> que, en general, "
            "<b>copian la lógica de riesgo del AI Act europeo</b> y añaden derechos de las personas afectadas. Es un campo que cambia rápido: <b>verifica el estado de cada norma</b>."
            + _tabla(
                ["País", "Instrumento", "Estado (verifica)"],
                [
                    ["México", "Documento de 2018 “Hacia una Estrategia de IA en México”; Principios de Chapultepec (29-ene-2026)", "Orientadores, <b>no vinculantes</b>. Sin ley general; hay iniciativas en el Congreso (por ejemplo, para facultar al Congreso a legislar en IA y una ley general)"],
                    ["Brasil", "<b>PL 2338/2023</b> (marco legal de la IA): clasificación por riesgo y derechos de las personas afectadas", "Aprobado por el Senado (dic. 2024); en trámite en la Cámara de Diputados, con comisión especial (según prensa de mayo de 2026)"],
                    ["Perú", "<b>Ley 31814</b> (2023) y su reglamento (D. S. 115-2025-PCM): usos prohibidos, de alto riesgo y de riesgo aceptable", "Reglamento vigente desde enero de 2026 según fuentes consultadas; sin régimen sancionador propio"],
                    ["Chile", "Política Nacional de IA y proyecto de ley que regula los sistemas de IA (2024), con enfoque de riesgo", "En el Congreso (verifica)"],
                    ["Colombia", "CONPES 3975 (2019): política nacional de transformación digital e IA; varios proyectos de ley", "Sin ley general (verifica)"],
                    ["Argentina y Uruguay", "Plan Nacional de IA (Argentina, 2019); estrategia nacional de IA (Uruguay, AGESIC)", "Estrategias y lineamientos; sin ley específica (verifica)"],
                ])
        ),
        "derechos_titulo": "Qué tienen en común",
        "derechos": [
            "<b>Enfoque de riesgo</b> inspirado en la UE (usos prohibidos, alto riesgo, riesgo bajo).",
            "<b>Principios compartidos:</b> derechos humanos, transparencia, no discriminación, supervisión humana y rendición de cuentas (coinciden con UNESCO y OCDE).",
            "<b>Cooperación regional:</b> la <b>Declaración de Santiago</b> (2023) y el Índice Latinoamericano de IA (ILIA) buscan una IA ética con visión regional.",
        ],
        "pasos_titulo": "Retos y buenas prácticas para adaptar a México",
        "pasos": [
            "<b>Retos comunes:</b> pocos recursos para vigilar y sancionar, autoridades poco coordinadas, brecha digital y de datos, y riesgo de copiar modelos extranjeros sin adaptarlos.",
            "<b>Buenas prácticas:</b> clasificar por riesgo, crear una <b>autoridad coordinadora</b>, exigir evaluaciones de impacto, proteger a grupos vulnerables y <b>participar en estándares regionales</b>.",
            "<b>Para México:</b> la discusión es si legislar con una ley general (como Brasil) o por sectores (como hoy), con base en los Principios de Chapultepec y los estándares de UNESCO y OCDE.",
        ],
        "contactos": [],
        "fundamento": "PL 2338/2023 (Brasil); Ley 31814 y D. S. 115-2025-PCM (Perú); CONPES 3975 (Colombia); Principios de Chapultepec (México, 2026); fuentes de prensa y análisis jurídicos consultados en nov. 2026; Programa de Normatividad de la IA, Unidad 3 (3.4).",
    },

    # ====================================================================== UNIDAD 4.1 – IA Y DERECHOS HUMANOS
    {
        "id": "ia_detectar_vulneracion",
        "titulo": "¿Cómo sé si un sistema de IA está vulnerando mis derechos humanos?",
        "emoji": "🚨",
        "boton": "¿Cómo sé si una IA vulnera derechos?",
        "relacionados": ["ia_requisitos", "ia_sesgos", "ia_responsabilidad", "caso_ia", "ia_alto_riesgo"],
        "keywords": [
            ("como se si un sistema de ia esta vulnerando", 15), ("como saber si un sistema de ia", 14), ("como saber si una ia", 14),
            ("como se si una ia", 14), ("como saber si la ia", 12), ("como se si la ia", 12), ("sistema de ia esta vulnerando", 14),
            ("ia esta vulnerando", 12), ("ia vulnera", 11), ("ia vulnere", 11), ("senales de que una ia", 12), ("ia me discrimina", 11),
            ("una ia me nego", 10), ("decision automatizada me perjudica", 11), ("detectar si una ia", 12), ("como detectar sesgo en una ia", 12),
            ("denunciar una ia", 11), ("vulnerando mis derechos", 5), ("como saber si un algoritmo", 12), ("como se si un algoritmo", 12),
            ("como reconocer una ia que vulnera", 13), ("lista de revision de ia", 11),
        ],
        "intro": (
            "No existe un “detector” único, pero puedes usar una <b>lista de revisión</b>. Un sistema de IA puede vulnerar derechos por <b>lo que decide</b>, "
            "por <b>cómo usa tus datos</b> o por <b>lo que oculta</b>. Si encuentras varias de estas señales, hay motivo para preguntar y reclamar:"
        ),
        "derechos_titulo": "Señales de alerta",
        "derechos": [
            "<b>Decide algo importante sobre ti</b> (beca, admisión, empleo, crédito, atención médica, vigilancia) y <b>nadie puede explicarte por qué</b>. → Transparencia y derecho a explicación (AI Act Art. 86; UNESCO).",
            "<b>No hay una persona</b> a quien apelar ni que pueda corregir la decisión. → Supervisión humana (AI Act Art. 14; Blueprint, principio 5).",
            "<b>Resultados sistemáticamente peores para un grupo</b> (mujeres, personas indígenas, con discapacidad, de cierta zona o tono de piel). → No discriminación (CPEUM Art. 1°).",
            "<b>Pide o deduce datos de más:</b> biometría, emociones, salud, ubicación, orientación sexual u opiniones, sin avisarte ni pedir consentimiento. → Privacidad y datos sensibles; en la UE está prohibido inferir emociones en escuelas y trabajos (Art. 5).",
            "<b>No te avisa que es una IA</b> o no marca el contenido sintético (deepfakes). → Transparencia (AI Act Art. 50; UNESCO párr. 127).",
            "<b>Te manipula</b> o explota vulnerabilidades (edad, urgencia económica), o te da una “calificación social”. → Práctica prohibida (AI Act Art. 5).",
            "<b>Vigilancia masiva</b> o reconocimiento facial en espacios públicos o escuelas, sin base legal ni límites. → Proporcionalidad y legalidad (CPEUM Art. 16; UNESCO párr. 26).",
            "<b>No hay vía de queja, reparación ni responsable identificable;</b> la organización dice “el sistema lo decidió”. → Rendición de cuentas (UNESCO párr. 68).",
        ],
        "pasos_titulo": "Cómo comprobarlo y qué hacer",
        "pasos": [
            "<b>Pregunta por escrito:</b> ¿qué decide el sistema?, ¿con qué datos?, ¿con qué criterios?, ¿quién es responsable? y ¿cómo apelo? Pide que <b>una persona revise tu caso</b>.",
            "<b>Prueba comparativa (para ingeniería):</b> compara tasas de aprobación y de error entre grupos. Una pista usada en EE. UU. es la <b>regla de los cuatro quintos</b>: si la tasa de selección de un grupo es menor al 80 % de la del grupo más favorecido, puede haber impacto adverso. "
            "Es una alerta, no una prueba definitiva.",
            "<b>Documenta:</b> capturas, fechas, resultados y comunicaciones. Ejerce tus <b>derechos ARCO</b> (acceso y oposición) para saber qué datos tuyos se usaron.",
            "<b>Acude a:</b> la Defensoría universitaria o la CODHEM si hay discriminación; a la autoridad de datos personales por uso indebido de tus datos; y al Ministerio Público si hay un delito (por ejemplo, un deepfake íntimo).",
            "<b>Si desarrollas el sistema:</b> revisa el tema “Requisitos de una IA responsable” y evalúa el impacto antes de desplegarlo.",
        ],
        "contactos": ["codhem", "defensoria_uaemex", "sabg", "cndh"],
        "fundamento": "Reglamento (UE) 2024/1689, Arts. 5, 14, 50 y 86; Recomendación de la UNESCO sobre la ética de la IA (2021, párrs. 26, 68 y 127); Blueprint for an AI Bill of Rights (2022); NIST AI RMF 1.0 (funciones Mapear y Medir); EEOC, Uniform Guidelines (29 CFR 1607.4D) para la regla de los cuatro quintos; CPEUM Arts. 1° y 16.",
    },
    {
        "id": "ia_sesgos",
        "titulo": "No discriminación y sesgos algorítmicos",
        "emoji": "⚖️",
        "boton": "Sesgos algorítmicos",
        "relacionados": ["ia_detectar_vulneracion", "ia_requisitos", "discriminacion_como_saber", "ia_nist_rmf"],
        "keywords": [
            ("sesgos algoritmicos", 11), ("sesgo algoritmico", 11), ("discriminacion algoritmica", 11), ("algoritmos discriminan", 10),
            ("ia discrimina", 10), ("no discriminacion y sesgos", 13), ("tipos de sesgo", 10), ("como evitar el sesgo", 11),
            ("equidad algoritmica", 10), ("fairness", 8), ("datos sesgados", 10), ("ejemplos de sesgo", 11), ("casos de sesgo", 11),
            ("sesgo en la ia", 11), ("sesgos en la ia", 11), ("sesgo en los algoritmos", 11), ("sesgos en los algoritmos", 11),
            ("que es un sesgo", 9), ("que es el sesgo", 9), ("compas", 5), ("gender shades", 10),
        ],
        "intro": (
            "Un <b>sesgo algorítmico</b> es un error sistemático que produce resultados <b>injustos para ciertas personas o grupos</b>. "
            "No suele ser “maldad” del sistema: viene de los <b>datos</b>, del <b>diseño</b> o del <b>uso</b>. El NIST distingue tres tipos: <b>sistémico</b> (desigualdades históricas de las instituciones), "
            "<b>computacional o estadístico</b> (datos poco representativos o mal medidos) y <b>cognitivo humano</b> (prejuicios de quien diseña o interpreta)."
        ),
        "derechos_titulo": "De dónde sale el sesgo",
        "derechos": [
            "<b>Datos históricos</b> que reflejan discriminación pasada o <b>poca representación</b> de algunos grupos.",
            "<b>Variables proxy:</b> datos “neutros” (código postal, apellido, tipo de teléfono) que sustituyen a una característica protegida.",
            "<b>Medir lo equivocado:</b> usar un indicador que no representa lo que se quiere decidir.",
            "<b>Bucles de retroalimentación:</b> el sistema influye en los datos futuros y refuerza el sesgo.",
            "<b>Uso fuera de contexto:</b> aplicar un modelo a una población distinta a la que se usó para entrenarlo.",
        ],
        "pasos_titulo": "Casos documentados, marco legal y cómo mitigarlo",
        "pasos": [
            "<b>Contratación (Amazon, ~2018):</b> una herramienta experimental de selección de currículos penalizaba los que incluían la palabra “mujeres”; la empresa la descartó (reportado por Reuters).",
            "<b>Reconocimiento facial (Gender Shades, 2018):</b> sistemas comerciales tenían errores de cerca de 35 % en mujeres de piel oscura frente a menos de 1 % en hombres de piel clara.",
            "<b>Justicia penal (COMPAS, 2016):</b> un análisis de ProPublica halló más falsos positivos en personas negras; el caso muestra que hay <b>definiciones de equidad en conflicto</b> y que su evaluación es debatida.",
            "<b>Beneficios sociales (Países Bajos):</b> un algoritmo de perfilado señaló injustamente a miles de familias por fraude con criterios discriminatorios; el gobierno renunció en 2021.",
            "<b>Marco legal:</b> en México se aplica la prohibición general de discriminar (CPEUM Art. 1° y Ley Federal para Prevenir y Eliminar la Discriminación); hasta donde se pudo verificar no hay norma específica sobre sesgos algorítmicos. "
            "En la UE, el AI Act exige gobernanza de datos con <b>examen de posibles sesgos</b> (Art. 10); en EE. UU., el Blueprint (principio 2) y las leyes antidiscriminación; la UNESCO pide un <b>recurso efectivo</b> (párr. 29).",
            "<b>Cómo mitigarlo:</b> auditar la representatividad de los datos; <b>medir errores y resultados por grupo</b>; evitar variables proxy; probar con personas diversas; documentar (fichas de datos y de modelo); mantener supervisión humana y un canal de apelación; monitorear tras el despliegue.",
            "<b>Matiz técnico:</b> en general no se pueden cumplir todas las definiciones de equidad a la vez; hay que elegir según el contexto y explicar la decisión.",
        ],
        "contactos": ["conapred", "codhem", "defensoria_uaemex"],
        "fundamento": "CPEUM Art. 1°; Reglamento (UE) 2024/1689, Arts. 5 y 10; Recomendación de la UNESCO (2021, párr. 29); NIST AI RMF 1.0 (sec. 3.7 y SP 1270 sobre sesgo); Buolamwini y Gebru (2018), Gender Shades; ProPublica (2016); Reuters (2018); Programa de Normatividad de la IA, Unidad 4 (4.1.2).",
    },
    {
        "id": "ia_libertad_expresion",
        "titulo": "Libertad de expresión y contenidos generados por IA",
        "emoji": "🗣️",
        "boton": "Libertad de expresión e IA",
        "relacionados": ["ia_generativa", "ue_dsa_dma", "violencia_digital", "ley_olimpia"],
        "keywords": [
            ("libertad de expresion e ia", 13), ("libertad de expresion y ia", 13), ("libertad de expresion y contenidos generados por ia", 15),
            ("libertad de expresion y la ia", 13), ("libertad de expresion e inteligencia artificial", 13), ("libertad de expresion", 8),
            ("contenidos generados por ia", 11), ("contenido generado por ia", 11), ("desinformacion", 7), ("fake news", 7), ("noticias falsas", 7),
            ("censura", 6), ("deepfakes y desinformacion", 10), ("deepfakes electorales", 10), ("moderacion de contenidos", 7), ("manipulacion electoral con ia", 11), ("ia y elecciones", 10),
            ("derecho a la informacion y ia", 9),
        ],
        "intro": (
            "La IA toca la <b>libertad de expresión</b> de tres maneras: <b>decide qué se ve</b> (moderación y recomendación), <b>produce contenido</b> (texto, imágenes, audio, video) y "
            "<b>vigila</b> lo que decimos, lo que puede generar un efecto inhibidor. El reto es proteger la expresión sin permitir engaños ni daños a terceros."
        ),
        "derechos_titulo": "Marco de derechos",
        "derechos": [
            "<b>CPEUM Art. 6°:</b> la manifestación de las ideas no será objeto de inquisición judicial o administrativa, salvo que ataque a la moral, la vida privada o los derechos de terceros, provoque algún delito o perturbe el orden público. "
            "<b>Art. 7°:</b> es inviolable la libertad de difundir opiniones, información e ideas por cualquier medio; no hay censura previa.",
            "<b>Estándar internacional:</b> DUDH Art. 19; el Pacto de Derechos Civiles y Políticos (Art. 19) y la Convención Americana (Art. 13) permiten restricciones solo si son <b>legales, con un fin legítimo y necesarias y proporcionales</b>, y prohíben la censura previa.",
            "<b>Tensiones:</b> (a) moderación automática con <b>falsos positivos</b> o sesgo hacia ciertas lenguas y dialectos; (b) <b>desinformación</b> y <b>deepfakes</b> (elecciones, suplantación); (c) filtros que bloquean contenido legítimo, como sátira o periodismo; (d) vigilancia que desalienta hablar.",
        ],
        "pasos_titulo": "Cómo responden las normas",
        "pasos": [
            "<b>UE:</b> el AI Act exige avisar cuando interactúas con una IA y <b>marcar el contenido sintético</b>, incluidos los deepfakes (Art. 50), con cuidado especial para obras artísticas o satíricas; la DSA obliga a explicar la moderación, ofrecer recurso y evaluar riesgos de desinformación.",
            "<b>EE. UU.:</b> la Primera Enmienda protege ampliamente la expresión; predominan la autorregulación y leyes estatales (por ejemplo, sobre deepfakes electorales). La ley <b>TAKE IT DOWN</b> (mayo de 2025) penaliza difundir imágenes íntimas sin consentimiento, incluidas las generadas con IA, y exige que las plataformas las retiren.",
            "<b>México:</b> no hay una ley general sobre contenido generado por IA; hay iniciativas para identificarlo (verifica). Se aplican reglas generales como el derecho de réplica, y si el contenido es íntimo sexual y no consentido, puede constituir delito por la <b>Ley Olimpia</b>.",
            "<b>UNESCO:</b> promueve que la IA no deteriore el acceso a información diversa y confiable ni se use para engañar de forma deliberada.",
            "<b>Buenas prácticas:</b> etiquetar contenido sintético y registrar su origen (marcas de agua, metadatos de procedencia); no censurar sin explicar y sin <b>apelación humana</b>; proteger sátira y periodismo; verificar antes de difundir.",
        ],
        "contactos": ["codhem", "fgjem", "sin_violencia"],
        "fundamento": "CPEUM Arts. 6° y 7°; DUDH Art. 19; Pacto Internacional de Derechos Civiles y Políticos Art. 19; Convención Americana Art. 13; Reglamento (UE) 2024/1689 Art. 50; Reglamento (UE) 2022/2065 (DSA); TAKE IT DOWN Act (EE. UU., 2025); Programa de Normatividad de la IA, Unidad 4 (4.1.3).",
    },

    # ====================================================================== UNIDAD 4.2 – RESPONSABILIDAD
    {
        "id": "ia_responsabilidad",
        "titulo": "Responsabilidad civil y penal por decisiones de la IA",
        "emoji": "⚖️",
        "boton": "¿Quién responde si la IA causa un daño?",
        "relacionados": ["ia_detectar_vulneracion", "ia_vehiculos_robots", "ia_cumplimiento", "ia_requisitos"],
        "keywords": [
            ("responsabilidad civil por decisiones automatizadas", 15), ("responsabilidad penal en casos de ia", 15),
            ("responsabilidad y rendicion de cuentas", 13), ("responsabilidad civil", 8), ("responsabilidad penal", 8),
            ("quien es responsable cuando la ia", 13), ("quien responde si un auto autonomo", 17), ("quien responde si un vehiculo autonomo", 17), ("quien responde en un accidente", 13), ("quien paga los danos", 11), ("quien responde si la ia", 13), ("quien es el responsable de la ia", 13),
            ("quien es responsable de una ia", 13), ("quien es el culpable", 8), ("de quien es la culpa", 8),
            ("responsabilidad de la ia", 12), ("culpa de la ia", 10), ("la ia comete un delito", 13), ("una ia puede cometer un delito", 14),
            ("ia autonoma", 8), ("danos causados por ia", 12), ("danos causados por una ia", 12), ("danos por ia", 10),
            ("responsabilidad objetiva", 8), ("responsabilidad por producto", 9), ("directiva de responsabilidad", 10),
            ("rendicion de cuentas", 7), ("indemnizacion por ia", 10),
        ],
        "intro": (
            "<b>Regla de oro:</b> una IA <b>no responde</b> por sí misma; <b>siempre responden personas</b> (físicas o morales). La UNESCO pide que la responsabilidad recaiga en personas y que <b>no se otorgue personalidad jurídica</b> a la IA (párr. 68). "
            "La duda es <b>cuál persona</b>: quien la diseñó, quien la vendió, quien la usa o quien la supervisa."
        ),
        "derechos_titulo": "Responsabilidad civil (reparar el daño)",
        "derechos": [
            "<b>Por culpa o dolo (Código Civil Federal Art. 1910):</b> quien, obrando ilícitamente o contra las buenas costumbres, cause un daño a otro está obligado a repararlo, salvo que demuestre culpa inexcusable de la víctima.",
            "<b>Objetiva por riesgo (Art. 1913):</b> quien usa mecanismos, instrumentos o aparatos <b>peligrosos por sí mismos</b> responde aunque no obre ilícitamente. Se discute si algunos sistemas de IA de alto riesgo encajan; <b>no hay un criterio general</b> (vacío normativo).",
            "<b>Patrones y empresas (Art. 1924):</b> responden por los daños de sus dependientes en el ejercicio de sus funciones; por analogía se discute su responsabilidad por los sistemas que despliegan. <b>Daño moral:</b> Art. 1916.",
            "<b>UE:</b> la nueva Directiva (UE) 2024/2853 trata el <b>software, incluida la IA, como “producto”</b>: responsabilidad objetiva del fabricante, presunciones y acceso a pruebas. Los Estados deben incorporarla a más tardar el <b>9-dic-2026</b>. "
            "La propuesta de Directiva específica sobre responsabilidad en IA fue retirada por la Comisión (verifica).",
            "<b>EE. UU.:</b> se aplican la responsabilidad por productos defectuosos y la negligencia, que varían por estado; las plataformas tienen una protección especial por contenido de terceros (Sec. 230).",
        ],
        "pasos_titulo": "Responsabilidad penal (castigar un delito)",
        "pasos": [
            "<b>Principio:</b> la responsabilidad penal es <b>personal y exige culpabilidad</b>. Un sistema de IA no tiene conciencia ni voluntad, por lo que <b>no puede ser autor de un delito</b>.",
            "<b>Quién puede responder:</b> quien usa la IA <b>como instrumento</b> para delinquir (fraude, suplantación, deepfakes íntimos); quien causa un daño por <b>imprudencia</b> (diseño o supervisión negligente, como un accidente de vehículo autónomo) o por <b>omisión</b> de un deber de cuidado.",
            "<b>Personas morales:</b> el Código Nacional de Procedimientos Penales (Art. 421) las hace responsables de delitos cometidos a su nombre, por su cuenta o en su beneficio cuando hubo <b>inobservancia del debido control en su organización</b>; por eso importan los programas de cumplimiento (Unidad 5).",
            "<b>La “brecha de responsabilidad”:</b> cuando un sistema autónomo actúa de forma imprevisible, puede ser difícil probar culpa. El Parlamento Europeo propuso en 2020 responsabilidad objetiva para IA de alto riesgo con seguro obligatorio.",
            "<b>Para ingeniería:</b> conserva <b>registros y documentación</b>, define quién supervisa, evalúa riesgos antes de desplegar, fija responsabilidades en los <b>contratos</b> y considera seguros.",
        ],
        "contactos": ["codhem", "fgjem"],
        "fundamento": "Código Civil Federal, Arts. 1910, 1913, 1916 y 1924; Código Nacional de Procedimientos Penales, Art. 421; Recomendación de la UNESCO (2021, párr. 68); Directiva (UE) 2024/2853; Reglamento (UE) 2024/1689 (Arts. 12 y 14); Programa de Normatividad de la IA, Unidad 4 (4.2).",
    },

    # ====================================================================== UNIDAD 4.3 – REGULACIÓN SECTORIAL
    {
        "id": "ia_salud_finanzas",
        "titulo": "IA en salud y en el sector financiero",
        "emoji": "🏥",
        "boton": "IA en salud y finanzas",
        "relacionados": ["ia_seguridad_educacion_empleo", "ia_alto_riesgo", "datos_y_derechos_humanos", "ia_responsabilidad"],
        "keywords": [
            ("diagnostico asistido", 13), ("ia en salud", 11), ("inteligencia artificial en salud", 13), ("ia en medicina", 11), ("ia medica", 10),
            ("diagnostico con ia", 11), ("software medico", 9), ("dispositivo medico", 8), ("ia en hospitales", 10),
            ("fintech", 10), ("ia en finanzas", 11), ("ia en el sector financiero", 12), ("ia en los bancos", 10), ("scoring crediticio", 12),
            ("score crediticio", 10), ("calificacion crediticia", 10), ("credito y ia", 10), ("ia y credito", 10), ("buro de credito", 8),
            ("ia en salud y finanzas", 14), ("me nego un credito", 12), ("me nego el credito", 12), ("banco me nego", 11), ("credito", 4), ("banco", 3),
        ],
        "intro": (
            "En <b>salud</b> y <b>finanzas</b> una decisión automatizada puede cambiar tu tratamiento o tu acceso a crédito. Por eso son sectores de <b>alto riesgo</b> y de datos sensibles. "
            "El principio común: <b>la IA apoya, una persona responsable decide</b> y tú puedes pedir explicación y revisión."
        ),
        "derechos_titulo": "Salud (diagnóstico asistido)",
        "derechos": [
            "<b>Riesgos:</b> errores de diagnóstico; datos no representativos; sesgos. Un algoritmo usado en EE. UU. para asignar programas de atención subestimó las necesidades de pacientes negros porque medía el <b>gasto</b> en salud, no la necesidad (Obermeyer et al., <i>Science</i>, 2019).",
            "<b>Datos:</b> los datos de salud son <b>datos personales sensibles</b>; el expediente clínico está sujeto a confidencialidad y normas oficiales (NOM-004-SSA3-2012).",
            "<b>México:</b> hasta donde se pudo verificar no hay una ley específica de IA médica; el <b>software con fin diagnóstico o terapéutico</b> puede considerarse <b>dispositivo médico</b> y requerir registro sanitario ante la COFEPRIS (verifica).",
            "<b>UE:</b> los productos sanitarios con IA son de <b>alto riesgo</b> (AI Act, Anexo I, con los reglamentos de dispositivos médicos); aplicación aplazada a 2028 (verifica). <b>EE. UU.:</b> la FDA regula el “software como dispositivo médico”.",
            "<b>OMS (2021):</b> seis principios: proteger la autonomía; promover el bienestar y la seguridad; transparencia y explicabilidad; responsabilidad; inclusión y equidad; y una IA sostenible.",
            "<b>Para ti como paciente:</b> tienes derecho a información clara y consentimiento informado; <b>el profesional de la salud decide</b> y puede explicarte qué papel tuvo la IA.",
        ],
        "pasos_titulo": "Sector financiero (fintech y scoring crediticio)",
        "pasos": [
            "<b>Riesgos:</b> exclusión de personas sin historial; variables proxy (código postal, tipo de teléfono, redes sociales); decisiones opacas; cobranza automatizada abusiva.",
            "<b>UE:</b> evaluar la solvencia o calificación crediticia de personas físicas es <b>IA de alto riesgo</b> (AI Act, Anexo III), y el RGPD (Art. 22) protege contra decisiones únicamente automatizadas.",
            "<b>EE. UU.:</b> las leyes de igualdad de oportunidades de crédito exigen explicar <b>las razones específicas</b> de una negativa, aunque la decisión use un algoritmo complejo.",
            "<b>México:</b> la <b>Ley Fintech</b> (Ley para Regular las Instituciones de Tecnología Financiera, 2018) y la CNBV regulan estas empresas; la Ley para Regular las Sociedades de Información Crediticia te da derecho a consultar y corregir tu reporte. Hasta donde se pudo verificar, no hay una norma específica sobre IA en crédito.",
            "<b>Qué puedes hacer:</b> pide por escrito el motivo de una negativa, solicita revisión por una persona, corrige tu historial y presenta una queja ante la <b>CONDUSEF</b>.",
        ],
        "contactos": ["condusef", "cofepris", "codhem"],
        "fundamento": "Reglamento (UE) 2024/1689 (Art. 6, Anexos I y III); RGPD Art. 22; OMS, Ética y gobernanza de la IA para la salud (2021); NOM-004-SSA3-2012; Ley para Regular las Instituciones de Tecnología Financiera; Obermeyer et al. (2019); Programa de Normatividad de la IA, Unidad 4 (4.3.1 y 4.3.2).",
    },
    {
        "id": "ia_seguridad_educacion_empleo",
        "titulo": "IA en seguridad pública, educación y empleo",
        "emoji": "🎓",
        "boton": "IA en seguridad, educación y empleo",
        "relacionados": ["ia_salud_finanzas", "ia_alto_riesgo", "abuso_laboral", "derechos_estudiante", "ia_sesgos"],
        "keywords": [
            ("ia en seguridad publica y vigilancia", 15), ("ia en seguridad publica", 12), ("ia en vigilancia", 11), ("vigilancia con ia", 11),
            ("vigilancia masiva", 9), ("reconocimiento facial en", 10), ("policia predictiva", 11), ("ia en la policia", 10),
            ("ia en educacion y empleo", 14), ("ia en educacion", 12), ("ia en la educacion", 12), ("ia en la escuela", 11), ("ia en las escuelas", 11),
            ("ia en el trabajo", 11), ("ia y empleo", 11), ("ia en el empleo", 11), ("ia en recursos humanos", 11), ("seleccion de personal con ia", 12),
            ("contratacion con ia", 11), ("detector de ia", 9), ("proctoring", 10), ("vigilancia en examenes", 10), ("herramientas de contratacion automatizadas", 12), ("ia para calificar", 12), ("calificacion automatica", 11), ("me califico una ia", 12),
        ],
        "intro": (
            "En estos tres ámbitos la IA puede <b>vigilar, evaluar o decidir</b> sobre personas que tienen poca capacidad de negociar. Por eso la UE los trata como <b>alto riesgo</b> "
            "(AI Act, Anexo III) y prohíbe algunos usos. Tus derechos clave: <b>legalidad, privacidad, no discriminación, explicación y revisión humana</b>."
        ),
        "derechos_titulo": "Seguridad pública y vigilancia",
        "derechos": [
            "<b>Riesgos:</b> falsos positivos del reconocimiento facial (el NIST halló diferencias de error por edad, sexo y origen en 2019); detenciones erróneas (como el caso de Robert Williams, en Detroit, 2020); vigilancia masiva y efecto inhibidor.",
            "<b>Derechos en juego:</b> privacidad y protección de datos (CPEUM Art. 16), legalidad, presunción de inocencia (Art. 20) y no discriminación.",
            "<b>UE (AI Act, Art. 5):</b> prohíbe la identificación biométrica remota “en tiempo real” en espacios públicos con fines policiales salvo excepciones estrictas y con autorización; prohíbe predecir delitos solo por el perfil de una persona y crear bases faciales con imágenes extraídas masivamente.",
            "<b>UNESCO:</b> la IA no debe usarse para vigilancia masiva ni puntuación social (párr. 26). <b>EE. UU.:</b> algunas ciudades limitaron el reconocimiento facial policial (San Francisco, 2019) e Illinois tiene una ley de privacidad biométrica (BIPA).",
            "<b>México:</b> la vigilancia con IA debe respetar los límites generales del Art. 16 y de las leyes de datos personales; hasta donde se pudo verificar, no hay una ley federal específica sobre reconocimiento facial (verifica).",
        ],
        "pasos_titulo": "Educación y empleo",
        "pasos": [
            "<b>Educación:</b> usos como la vigilancia en exámenes (<i>proctoring</i>), los detectores de textos de IA, la predicción de deserción o la calificación automática. Riesgos: falsos positivos (un estudio de Stanford halló que los detectores penalizan a quienes escriben en un segundo idioma), sesgo y privacidad.",
            "<b>UE:</b> es de alto riesgo decidir el acceso o la admisión, evaluar resultados y vigilar exámenes, y se <b>prohíbe inferir emociones</b> en centros educativos y de trabajo salvo razones médicas o de seguridad. <b>UNESCO (párr. 104):</b> la IA debe apoyar el aprendizaje sin reducir capacidades ni usar de forma indebida los datos del estudiantado.",
            "<b>En tu universidad:</b> una calificación o sanción no debe depender solo de una herramienta automática; tienes derecho a una <b>revisión por una persona</b> (ver “Derechos como estudiante”).",
            "<b>Empleo:</b> filtrado de currículos, entrevistas en video, evaluación del desempeño y gestión algorítmica. En México, la LFT prohíbe negarse a contratar por origen, sexo, edad, discapacidad, religión, estado civil u otros criterios discriminatorios (Art. 133, fracc. I), y la NOM-035 protege frente a riesgos psicosociales.",
            "<b>Más reglas:</b> en la UE, la Directiva (UE) 2024/2831 regula la gestión algorítmica del trabajo en plataformas (incorporación a finales de 2026). En la ciudad de Nueva York, la Ley Local 144 (2023) exige <b>auditorías de sesgo</b> y avisos a candidatos. En México hay iniciativas para informar cuando la IA intervenga y exigir intervención humana (verifica).",
        ],
        "contactos": ["codhem", "defensoria_uaemex", "profedet", "conapred"],
        "fundamento": "CPEUM Arts. 3°, 16, 20 y 123; Ley Federal del Trabajo, Art. 133 fracc. I; Reglamento (UE) 2024/1689 (Art. 5 y Anexo III); Directiva (UE) 2024/2831; UNESCO (2021, párrs. 26 y 104); NIST IR 8280 (2019); Liang et al. (2023); Programa de Normatividad de la IA, Unidad 4 (4.3.3 y 4.3.4).",
    },

    # ====================================================================== UNIDAD 4.4 – TECNOLOGÍAS CRÍTICAS
    {
        "id": "ia_generativa",
        "titulo": "IA generativa: riesgos jurídicos y obligaciones",
        "emoji": "✨",
        "boton": "IA generativa",
        "relacionados": ["ia_libertad_expresion", "ue_ai_act", "violencia_digital", "privacidad_datos"],
        "keywords": [
            ("regulacion de la ia generativa", 14), ("que es la ia generativa", 12), ("riesgos de la ia generativa", 13), ("ia generativa", 9),
            ("modelos de lenguaje", 8), ("llm$", 8), ("alucinaciones", 9), ("derechos de autor y ia", 11), ("derechos de autor y contenido", 12), ("derechos de autor", 7), ("copyright", 7), ("obras generadas por ia", 11), ("derechos de autor en contenidos generados", 12),
            ("modelos fundacionales", 9), ("modelos fundacion", 9), ("contenido sintetico", 9), ("marca de agua", 8), ("chatgpt", 5),
            ("propiedad intelectual y ia", 11), ("ia generativa y derechos de autor", 13), ("usar chatgpt", 7),
        ],
        "intro": (
            "La <b>IA generativa</b> crea texto, imágenes, audio, video o código a partir de modelos entrenados con enormes cantidades de datos. "
            "Plantea riesgos jurídicos nuevos y por eso aparece en leyes y guías recientes."
        ),
        "derechos_titulo": "Riesgos jurídicos principales",
        "derechos": [
            "<b>Datos personales y privacidad:</b> los modelos pueden entrenarse con datos personales; lo que escribes en un <i>prompt</i> puede incluir información sensible o confidencial.",
            "<b>Alucinaciones y desinformación:</b> pueden producir datos falsos con apariencia convincente; no deben usarse sin verificar en temas legales, médicos o académicos.",
            "<b>Derechos de autor:</b> hay disputas por entrenar con obras protegidas y sobre quién es autor de lo generado. En México la ley vincula la autoría con personas físicas, y la titularidad de obras creadas solo por IA es un tema abierto (verifica criterios). "
            "En EE. UU., la Oficina de Derechos de Autor y los tribunales exigen <b>autoría humana</b> (<i>Thaler v. Perlmutter</i>, 2025).",
            "<b>Deepfakes y violencia digital:</b> pueden suplantar identidad o crear imágenes íntimas falsas; esto puede ser delito (Ley Olimpia).",
            "<b>Seguridad y mal uso:</b> fraudes, ingeniería social, generación de código malicioso.",
            "<b>Integridad académica:</b> la UNESCO publicó en 2023 una guía para el uso de IA generativa en educación e investigación.",
        ],
        "pasos_titulo": "Qué exige el AI Act y buenas prácticas",
        "pasos": [
            "<b>Transparencia (Art. 50):</b> avisar cuando alguien interactúa con una IA y <b>marcar el contenido sintético</b> en formato legible por máquinas; etiquetar los deepfakes.",
            "<b>Modelos de propósito general (Arts. 53 a 55):</b> documentación técnica, <b>política de derechos de autor</b> (respetar la reserva de derechos de quien no quiere que se use su obra), resumen público del contenido de entrenamiento y, si hay riesgo sistémico, evaluaciones y reporte de incidentes. "
            "Existe un <b>Código de buenas prácticas</b> voluntario para estos modelos (2025).",
            "<b>Para quien la usa:</b> no subas datos personales ni confidenciales; verifica y cita las fuentes; revisa los términos de uso; declara cuando usaste IA en trabajos académicos.",
            "<b>Para quien la desarrolla:</b> documenta los datos, prueba con grupos diversos, ofrece avisos claros, registra el origen del contenido y define quién responde.",
            "<i>Transparencia:</i> este asistente <b>no usa IA generativa</b>; sus respuestas son textos revisados.",
        ],
        "contactos": [],
        "fundamento": "Reglamento (UE) 2024/1689, Arts. 50 y 53 a 55; UNESCO, Guía para la IA generativa en educación e investigación (2023); Thaler v. Perlmutter (D.C. Cir., 2025); Programa de Normatividad de la IA, Unidad 4 (4.4.2) y Unidad 5 (5.5.2).",
    },
    {
        "id": "ia_vehiculos_robots",
        "titulo": "Vehículos autónomos, robots y sistemas autónomos",
        "emoji": "🚗",
        "boton": "Vehículos autónomos y robots",
        "relacionados": ["ia_responsabilidad", "ia_alto_riesgo", "ia_unesco", "unidad4_hub"],
        "keywords": [
            ("auto autonomo", 13), ("carro autonomo", 13), ("coche autonomo", 13), ("vehiculos autonomos", 13), ("vehiculo autonomo", 13), ("coches autonomos", 13), ("carros autonomos", 13), ("autos autonomos", 13),
            ("conduccion autonoma", 13), ("autos sin conductor", 12), ("robots y sistemas autonomos", 15), ("sistemas autonomos", 10),
            ("robotica", 8), ("robots", 7), ("armas autonomas", 13), ("robots asesinos", 11), ("leyes de asimov", 11), ("personalidad electronica", 12),
            ("personalidad juridica de los robots", 13), ("derechos de los robots", 12), ("drones", 6), ("tesla autopilot", 9), ("robotaxi", 10),
        ],
        "intro": (
            "Cuando la IA se integra en <b>máquinas que actúan en el mundo físico</b>, el daño puede ser corporal y la regulación se parece más a la de <b>seguridad de productos</b> que a la de datos."
        ),
        "derechos_titulo": "Vehículos autónomos",
        "derechos": [
            "<b>Niveles de automatización (SAE J3016):</b> 0 sin automatización; 1 asistencia; 2 automatización parcial (<b>el conductor vigila siempre</b>); 3 condicionada (el sistema conduce, pero la persona debe retomar el control); 4 alta (sin conductor en zonas definidas); 5 total.",
            "<b>La pregunta clave:</b> ¿quién responde en un accidente? Puede ser el conductor, el fabricante, el operador de la flota o el proveedor del software; depende del nivel y de si el sistema funcionó como se esperaba (ver “Responsabilidad”).",
            "<b>Ética:</b> la Comisión de Ética alemana (2017) fijó 20 reglas: priorizar la protección de la vida humana y <b>prohibir discriminar</b> por rasgos personales en dilemas inevitables.",
            "<b>Normas:</b> Convención de Viena sobre Circulación Vial (1968, con reformas de 2016); Reglamento n.º 157 de la ONU (sistemas ALKS, 2021); en la UE, reglas de homologación para sistemas de conducción automatizada; en el Reino Unido, la <i>Automated Vehicles Act</i> (2024). "
            "<b>EE. UU.:</b> sin ley federal general; la NHTSA exige reportar choques y los estados dan los permisos.",
            "<b>México:</b> hasta donde se pudo verificar no hay marco federal específico; se aplican la Ley General de Movilidad y Seguridad Vial (2022) y los reglamentos de tránsito locales, con una persona conductora responsable (verifica).",
        ],
        "pasos_titulo": "Robots y sistemas autónomos",
        "pasos": [
            "<b>Seguridad técnica:</b> normas ISO para robots industriales (ISO 10218), colaborativos (ISO/TS 15066) y de asistencia personal (ISO 13482). La UE aprobó el <b>Reglamento de Máquinas (UE) 2023/1230</b> (aplicable desde enero de 2027), que cubre máquinas con comportamiento autónomo o basado en aprendizaje automático.",
            "<b>¿Derechos o personalidad para robots?</b> El Parlamento Europeo planteó en 2017 una “personalidad electrónica”, pero más de 150 especialistas lo rechazaron en 2018, y la UNESCO (2021) dice que <b>no debe otorgarse personalidad jurídica</b> a los sistemas de IA. Las “leyes de la robótica” de Asimov son <b>ficción</b>, no derecho.",
            "<b>Armas autónomas letales:</b> se discuten en la ONU (Convención sobre Ciertas Armas Convencionales y la Asamblea General). El eje es el <b>control humano significativo</b> y el cumplimiento del derecho internacional humanitario. El AI Act excluye los usos militares.",
            "<b>Robots de cuidado y sociales:</b> riesgos de privacidad y de <b>engaño emocional</b>; la UNESCO pide que las personas sepan cuando interactúan con una IA que imita rasgos humanos (párr. 127).",
            "<b>Para ingeniería:</b> diseña con <b>paro de emergencia</b> y modo seguro, registro de eventos, pruebas en entornos controlados y documentación de límites del sistema.",
        ],
        "contactos": [],
        "fundamento": "SAE J3016; Convención de Viena sobre Circulación Vial (1968); Reglamento ONU n.º 157; Reglamento (UE) 2023/1230; Recomendación de la UNESCO (2021, párrs. 68 y 127); Comisión de Ética alemana sobre conducción automatizada (2017); Programa de Normatividad de la IA, Unidad 4 (4.4.3 y 4.4.4).",
    },
]
