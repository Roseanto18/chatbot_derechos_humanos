"""
BASE DE CONOCIMIENTO DEL CHATBOT
================================
Aquí vive TODO el contenido. Para agregar un tema nuevo solo copias un bloque
de TOPICS y lo editas; no tienes que tocar models.py.

Cada tema tiene:
  id          identificador único (sin espacios)
  titulo      título que ve el usuario
  emoji       decoración
  boton       texto corto del botón rápido (opcional)
  urgente     True = si coincide, se muestra antes que cualquier otro tema
  keywords    lista de (palabra_o_frase, peso). Se escriben SIN acentos y en
              minúsculas. Una palabra suelta funciona como "prefijo":
              "discrimin" detecta discriminan, discriminación, discriminado...
              Una frase (con espacios) debe aparecer completa.
              Peso 3 = señal fuerte, 2 = media, 1 = débil.
  intro       texto introductorio (admite <b> y <i>)
  derechos    lista de derechos que aplican
  pasos       lista ordenada de qué hacer
  contactos   ids de CONTACTS que se mostrarán
  fundamento  base legal (para transparencia y para tu documento de normatividad)
"""

# ---------------------------------------------------------------------------
# CONTACTOS  (verificados en fuentes oficiales/prensa el 11-nov-2026;
# los marcados con VERIFICAR vienen de tu versión original y conviene
# confirmarlos con la Facultad antes de la entrega)
# ---------------------------------------------------------------------------
CONTACTS = {
    "911": {"name": "Emergencias", "phone": "911",
            "note": "Riesgo inmediato, las 24 h."},
    "089": {"name": "Denuncia anónima", "phone": "089"},
    "codhem": {
        "name": "CODHEM – Comisión de Derechos Humanos del Estado de México",
        "phone": "800 999 4000", "phone2": "(722) 236 0560",
        "note": "Atiende las 24 h, los 365 días. Presentar una queja es gratuito.",
        "url": "https://www.codhem.org.mx"},
    "cndh": {"name": "CNDH – Comisión Nacional de los Derechos Humanos",
             "phone": "800 715 2000", "url": "https://www.cndh.org.mx"},
    "linea_vida": {"name": "Línea de la Vida (apoyo emocional)",
                   "phone": "800 911 2000"},
    "sin_violencia": {
        "name": "Línea Sin Violencia (Gobierno del Edomex)",
        "phone": "800 108 4053",
        "note": "Orientación jurídica y psicológica para mujeres, hijas e hijos."},
    "hombre_a_hombre": {"name": "Línea Hombre a Hombre (Gobierno del Edomex)",
                        "phone": "800 900 4321"},
    "trata_edomex": {"name": "Línea contra la Trata de Personas (Edomex)",
                     "phone": "800 832 4745"},
    "trata_nacional": {"name": "Línea Nacional contra la Trata de Personas",
                       "phone": "800 5533 000"},
    "fgjem": {
        "name": "Fiscalía General de Justicia del Estado de México",
        "phone": "800 702 8770",
        "note": "Atención ciudadana y denuncia. También puedes acudir a cualquier Ministerio Público."},
    "ceavem": {
        "name": "CEAVEM – Comisión Ejecutiva de Atención a Víctimas del Estado de México",
        "phone": "(722) 275 8664",
        "note": "Consejería Jurídica, Paseo de los Cisnes Núm. 49, Col. La Asunción, Metepec.",
        "url": "https://ceavem.edomex.gob.mx/"},
    "infoem": {"name": "INFOEM – Transparencia y datos personales del Edomex",
               "url": "https://www.infoem.org.mx"},
    "uaemex_psico": {
        "name": "Servicio de Atención Psicológica – Facultad de Ingeniería UAEMéx",
        "url": "https://ingenieria.uaemex.mx/servicios/internos/atenci%C3%B3n-psicologica.html"},
    "uaemex_clinica": {
        "name": "Clínica Multidisciplinaria de Salud (Salud Mental UAEMéx)",
        "url": "https://sevepe.uaemex.mx/salud/cl%C3%ADnica-multidisciplinaria-de-salud/salud-mental.html"},
    "uaemex_portal": {"name": "Portal oficial de la Facultad de Ingeniería",
                      "url": "https://ingenieria.uaemex.mx/"},
    "uaemex_general": {
        "name": "UAEMéx – Teléfono general", "phone": "722 226 2300",
        "note": "VERIFICAR: dato de la versión original del proyecto."},
    "procuraduria_nna": {
        "name": "Procuraduría de Protección de Niñas, Niños y Adolescentes (DIF municipal / DIFEM)",
        "note": "Acude al DIF de tu municipio o al DIFEM. VERIFICAR: teléfono directo de la Procuraduría de tu municipio.",
        "url": "https://difem.edomex.gob.mx"},
    "conapred": {
        "name": "CONAPRED – Consejo Nacional para Prevenir la Discriminación",
        "note": "Orientación y quejas por discriminación (ámbito federal y particulares). VERIFICAR teléfono vigente en su sitio.",
        "url": "https://www.conapred.org.mx"},
    "defensoria_uaemex": {
        "name": "Defensoría de los Derechos Universitarios de la UAEMéx",
        "note": "Instancia universitaria para quejas por afectación a derechos de estudiantes. "
                "Pregunta en la Facultad cómo contactarla o consulta el portal de la UAEMéx.",
        "url": "https://www.uaemex.mx"},
}

# ---------------------------------------------------------------------------
# FUENTES OFICIALES
# ---------------------------------------------------------------------------
SOURCES = [
    {"name": "Constitución Política de los Estados Unidos Mexicanos (CPEUM)",
     "url": "https://www.diputados.gob.mx/LeyesBiblio/pdf/CPEUM.pdf"},
    {"name": "Declaración Universal de los Derechos Humanos (ONU)",
     "url": "https://www.un.org/es/about-us/universal-declaration-of-human-rights"},
    {"name": "Ley General de Víctimas (México)",
     "url": "https://www.diputados.gob.mx/LeyesBiblio/pdf/LGV.pdf"},
    {"name": "Ley de los Derechos de Niñas, Niños y Adolescentes del Estado de México",
     "url": "https://legislacion.edomex.gob.mx/"},
    {"name": "Ley General de Acceso de las Mujeres a una Vida Libre de Violencia",
     "url": "https://www.diputados.gob.mx/LeyesBiblio/pdf/LGAMVLV.pdf"},
    {"name": "Comisión Nacional de los Derechos Humanos (CNDH)",
     "url": "https://www.cndh.org.mx/"},
    {"name": "Comisión de Derechos Humanos del Estado de México (CODHEM)",
     "url": "https://www.codhem.org.mx"},
]

# ---------------------------------------------------------------------------
# TEMAS
# ---------------------------------------------------------------------------
TOPICS = [
    # ------------------------------------------------------------------ URGENTES
    {
        "id": "crisis_emocional",
        "titulo": "Estoy aquí contigo",
        "emoji": "💚",
        "urgente": True,
        "keywords": [
            ("quiero morir", 4), ("quiero morirme", 4), ("suicid", 4),
            ("quitarme la vida", 4), ("no quiero vivir", 4),
            ("hacerme dano", 4), ("lastimarme", 3), ("acabar con todo", 3),
            ("ya no puedo mas", 3), ("no aguanto mas", 3),
            ("mejor muerto", 4), ("mejor muerta", 4),
        ],
        "intro": (
            "Siento mucho que estés pasando por algo tan pesado. Lo que sientes importa "
            "y <b>no tienes que enfrentarlo a solas</b>."
        ),
        "pasos": [
            "Si estás en peligro ahora o piensas hacerte daño en este momento, llama al <b>911</b>.",
            "Marca a la <b>Línea de la Vida: 800 911 2000</b> para hablar con una persona que te escuche.",
            "Busca ahora a alguien de confianza (familiar, amistad, compañero/a) y dile cómo te sientes. "
            "Si puedes, no te quedes solo/a.",
            "Cuando te sientas con más calma, el servicio de atención psicológica de la Facultad puede acompañarte.",
        ],
        "contactos": ["911", "linea_vida", "uaemex_psico"],
        "fundamento": "Derecho a la protección de la salud (Art. 4° CPEUM).",
    },
    {
        "id": "emergencia",
        "titulo": "Ayuda inmediata",
        "emoji": "🚨",
        "boton": "Es una emergencia",
        "urgente": True,
        "keywords": [
            ("emergencia", 3), ("auxilio", 3), ("socorro", 3),
            ("me quieren matar", 4), ("me estan golpeando", 4), ("me golpean", 3),
            ("me siguen", 3), ("me persiguen", 3), ("secuestr", 4),
            ("peligro", 3), ("amenaz", 2), ("amenazas de muerte", 4), ("me amenazan de muerte", 4),
            ("me quieren hacer dano", 4), ("tengo miedo", 2), ("ayuda urgente", 3),
            ("estoy en riesgo", 3),
        ],
        "intro": "Si tu vida o tu integridad están en riesgo <b>ahora</b>, lo primero es ponerte a salvo.",
        "pasos": [
            "Llama al <b>911</b> y di dónde estás.",
            "Aléjate del peligro si puedes hacerlo de forma segura y ve a un lugar con gente.",
            "Cuando estés a salvo, documenta lo ocurrido y busca atención médica si la necesitas.",
            "Puedes denunciar de forma anónima al <b>089</b> o ante el Ministerio Público.",
        ],
        "relacionados": ["donde_ayuda", "emergencia_menores"],
        "contactos": ["911", "089", "codhem", "ceavem", "linea_vida"],
        "fundamento": "Derecho a la vida y a la integridad personal (Art. 1° CPEUM y tratados internacionales).",
    },
    # ------------------------------------------------------------------ DERECHOS
    {
        "id": "derechos_generales",
        "titulo": "Tus derechos humanos",
        "emoji": "⚖️",
        "boton": "¿Cuáles son mis derechos?",
        "keywords": [
            ("cuales son mis derechos", 5), ("derechos humanos", 3), ("mis derechos", 3),
            ("que derechos", 3), ("garantias", 2), ("constitucion", 2),
            ("articulo 1", 2), ("derechos", 1), ("derecho", 1),
        ],
        "intro": (
            "El <b>Artículo 1° de la Constitución</b> reconoce que todas las personas en México "
            "gozan de los derechos humanos de la Constitución y de los tratados internacionales. "
            "Nadie te los \"da\": ya son tuyos, y las autoridades están obligadas a promoverlos, "
            "respetarlos, protegerlos y garantizarlos."
        ),
        "derechos": [
            "<b>Igualdad y no discriminación</b> (Art. 1° y 4°).",
            "<b>Educación</b> (Art. 3°).",
            "<b>Salud, vivienda digna, agua y medio ambiente sano</b> (Art. 4°).",
            "<b>Libertad de expresión y acceso a la información</b> (Art. 6° y 7°).",
            "<b>Petición, reunión y asociación</b> (Art. 8° y 9°).",
            "<b>Libertad personal, debido proceso y presunción de inocencia</b> (Art. 14, 16, 19 y 20).",
            "<b>Privacidad y protección de tus datos personales</b> (Art. 6° y 16).",
            "<b>Acceso a la justicia</b> (Art. 17).",
            "<b>Trabajo digno</b> (Art. 5° y 123).",
            "<b>Una vida libre de violencia.</b>",
        ],
        "pasos": [
            "Si crees que violaron un derecho tuyo, anota qué pasó, cuándo, dónde y quién estuvo presente.",
            "Guarda pruebas: mensajes, capturas, fotos, documentos, nombres de testigos.",
            "Acude a la <b>CODHEM</b>: presentar una queja es gratuito y puedes hacerlo en línea.",
            "Si ocurrió dentro de la universidad, empieza por la Defensoría de los Derechos Universitarios.",
            "Cuéntame tu situación (por ejemplo: \"me discriminan en mi salón\") y te oriento con más detalle.",
        ],
        "relacionados": ["lista_dh", "derechos_estudiante", "estudiante_vs_ciudadano", "casos_practicos"],
        "contactos": ["codhem", "cndh", "defensoria_uaemex"],
        "fundamento": "CPEUM Art. 1°; Declaración Universal de los Derechos Humanos (ONU).",
    },
    {
        "id": "discriminacion",
        "titulo": "Discriminación",
        "emoji": "🤝",
        "boton": "Me discriminan",
        "keywords": [
            ("discrimin", 4), ("racis", 3), ("homofob", 3), ("transfob", 3),
            ("xenofob", 3), ("machis", 2), ("por ser mujer", 3), ("por ser indigena", 3),
            ("por mi religion", 3), ("por mi color", 3), ("trato desigual", 3),
            ("me excluyen", 3), ("me excluyeron", 3), ("indigena", 1), ("lgbt", 2),
            ("discapacid", 2),
        ],
        "intro": (
            "Discriminar es tratar de forma desigual o excluir a alguien por una característica personal, "
            "afectando su dignidad o el ejercicio de sus derechos."
        ),
        "derechos": [
            "Nadie puede negarte un servicio, inscripción, trato digno u oportunidades por origen étnico o nacional, "
            "género, edad, discapacidad, condición social, salud, religión, opiniones, preferencias sexuales, "
            "estado civil u otra condición que atente contra tu dignidad.",
            "Si tienes una discapacidad, tienes derecho a <b>ajustes razonables</b> para estudiar en igualdad de condiciones.",
            "Tienes derecho a presentar una queja sin sufrir represalias.",
        ],
        "pasos": [
            "Documenta: fecha, lugar, quién lo hizo, qué dijo o hizo y si hubo testigos. Guarda capturas o mensajes.",
            "Si es posible, pide por escrito la razón de la decisión que te afecta.",
            "Si ocurre en la Facultad, acude a la Defensoría de los Derechos Universitarios o a las autoridades de tu Facultad.",
            "Presenta una queja ante la <b>CODHEM</b> (gratuita, también en línea). Entre más pronto, mejor: "
            "las quejas suelen tener plazo, normalmente de un año desde los hechos.",
        ],
        "relacionados": ["discriminacion_como_saber", "caso_discriminacion"],
        "contactos": ["codhem", "defensoria_uaemex", "cndh"],
        "fundamento": "CPEUM Art. 1° (último párrafo); Ley Federal para Prevenir y Eliminar la Discriminación.",
    },
    {
        "id": "acoso_hostigamiento",
        "titulo": "Acoso u hostigamiento sexual",
        "emoji": "🛡️",
        "boton": "Acoso o violencia de género",
        "keywords": [
            ("acoso", 4), ("acosa", 4), ("hostig", 4), ("tocamient", 4), ("manose", 4),
            ("violencia de genero", 4), ("abuso sexual", 4), ("agresion sexual", 4),
            ("violacion", 4), ("violaron", 4), ("violarme", 4), ("insinu", 3), ("piropo", 2),
            ("sexual", 2), ("me toco", 3), ("me tocaron", 3), ("me tocan", 3), ("me toca sin", 4), ("me estan tocando", 4), ("me incomoda", 2),
            ("profesor me", 2), ("maestro me", 2), ("companero me", 1),
        ],
        "intro": (
            "<b>Lo que viviste no es tu culpa.</b> En la ley, el <b>hostigamiento</b> sexual ocurre cuando hay una relación "
            "de subordinación (por ejemplo, profesor/a–estudiante) y el <b>acoso</b> sexual cuando hay un ejercicio abusivo de poder "
            "que te deja en indefensión, aunque no haya subordinación."
        ),
        "derechos": [
            "Derecho a ser escuchado/a con respeto, sin que dudes de ti o te culpen (sin revictimización).",
            "Derecho a asesoría jurídica y atención psicológica.",
            "Derecho a denunciar y a solicitar medidas de protección cuando proceda.",
            "Derecho a no sufrir represalias académicas por denunciar.",
        ],
        "pasos": [
            "<b>Tu seguridad primero:</b> aléjate de la situación si puedes y busca a alguien de confianza.",
            "Guarda evidencia: mensajes, capturas, audios, fechas, nombres de testigos. No borres nada.",
            "Llama a la <b>Línea Sin Violencia</b> para orientación jurídica y psicológica.",
            "Puedes denunciar ante el <b>Ministerio Público</b> (Fiscalía del Edomex). Hay agencias especializadas en violencia sexual y de género.",
            "En la universidad, acude a la Defensoría de los Derechos Universitarios y a las autoridades de tu Facultad.",
            "Si estás en peligro ahora, llama al <b>911</b>.",
        ],
        "relacionados": ["violencia_docente", "caso_hostigamiento", "donde_ayuda"],
        "contactos": ["sin_violencia", "fgjem", "ceavem", "defensoria_uaemex", "uaemex_psico", "911"],
        "fundamento": "Ley General de Acceso de las Mujeres a una Vida Libre de Violencia; Ley General de Víctimas.",
    },
    {
        "id": "violencia_pareja_familia",
        "titulo": "Violencia en la pareja o la familia",
        "emoji": "🏠",
        "boton": "Violencia en casa o pareja",
        "keywords": [
            ("violencia familiar", 4), ("violencia domestica", 4), ("violencia en casa", 4),
            ("mi pareja me", 3), ("mi novio me", 3), ("mi novia me", 3), ("mi esposo me", 3),
            ("mi esposa me", 3), ("mi papa me", 2), ("mi mama me", 2), ("me pega", 3),
            ("me pegan", 3), ("me golpea", 3), ("maltrat", 3), ("celos", 1), ("control", 1),
        ],
        "intro": "Ninguna forma de violencia en casa o en la pareja es aceptable, ni es tu culpa. Hay apoyo y puedes pedirlo.",
        "derechos": [
            "Derecho a una vida libre de violencia.",
            "Derecho a atención médica, psicológica y asesoría jurídica gratuitas.",
            "Derecho a solicitar medidas u órdenes de protección ante la autoridad.",
        ],
        "pasos": [
            "Si hay peligro inmediato, llama al <b>911</b>.",
            "Habla con una persona de confianza y, si puedes, ten a la mano tus documentos importantes y un lugar seguro al cual ir.",
            "Llama a la <b>Línea Sin Violencia</b> (mujeres, hijas e hijos) o a <b>Hombre a Hombre</b> (hombres que viven violencia o desean cambiar conductas).",
            "Puedes denunciar ante el Ministerio Público y pedir acompañamiento a la CEAVEM.",
        ],
        "contactos": ["911", "sin_violencia", "hombre_a_hombre", "fgjem", "ceavem"],
        "fundamento": "Ley General de Acceso de las Mujeres a una Vida Libre de Violencia; Ley General de Víctimas.",
    },
    {
        "id": "detencion_policia",
        "titulo": "Si te detiene la policía",
        "emoji": "👮",
        "boton": "Me detuvo la policía",
        "keywords": [
            ("me detuvo", 4), ("me detuvieron", 4), ("me detienen", 4), ("detencion", 4),
            ("detenido", 3), ("detenida", 3), ("policia", 2), ("patrulla", 2), ("me paro la policia", 4), ("me pararon", 3), ("me pidio dinero", 3),
            ("me arrestaron", 4), ("arresto", 3), ("me revisaron", 3), ("me esculcaron", 3),
            ("ministerio publico", 2), ("abuso de autoridad", 4), ("extors", 3), ("me pidieron dinero", 3),
        ],
        "intro": "Aunque una autoridad te detenga, <b>conservas tus derechos</b>. Mantén la calma y no te resistas físicamente.",
        "derechos": [
            "A que te informen <b>quién te detiene y por qué</b>.",
            "A <b>guardar silencio</b>: no estás obligado/a a declarar.",
            "A un <b>abogado/a</b>; si no tienes, el Estado debe darte un defensor público.",
            "A avisar a un familiar o persona de confianza.",
            "A no ser incomunicado/a, ni sufrir tortura, golpes o malos tratos.",
            "A ser puesto/a <b>sin demora</b> a disposición del Ministerio Público, y a atención médica si estás lesionado/a.",
            "A la presunción de inocencia.",
        ],
        "pasos": [
            "Pregunta nombre, corporación y número de patrulla o placa; si puedes, anótalos.",
            "No firmes nada sin leerlo y sin tu abogado/a.",
            "Pide que avisen a tu familia o a alguien de confianza.",
            "Si hubo abuso, extorsión o maltrato, presenta queja en la <b>CODHEM</b> (atiende 24 h) y denuncia ante el Ministerio Público.",
        ],
        "contactos": ["codhem", "fgjem", "089", "911"],
        "fundamento": "CPEUM Art. 14, 16, 19, 20 y 21; Ley Nacional del Registro de Detenciones.",
    },
    {
        "id": "victima_delito",
        "titulo": "Si fuiste víctima de un delito",
        "emoji": "📝",
        "boton": "Fui víctima de un delito",
        "keywords": [
            ("victima", 3), ("me robaron", 4), ("robo", 3), ("asalto", 4), ("me asaltaron", 4),
            ("denunciar", 3), ("denuncia", 3), ("fraude", 3), ("me estafaron", 4), ("estafa", 3),
            ("delito", 3), ("amenaz", 3), ("lesiones", 2), ("me agredieron", 3), ("agredi", 2),
            ("reparacion del dano", 3),
        ],
        "intro": "Si fuiste víctima de un delito, la <b>Ley General de Víctimas</b> te reconoce derechos y apoyo del Estado.",
        "derechos": [
            "Trato digno, sin que te culpen ni te revictimicen.",
            "Atención médica y psicológica.",
            "Asesoría jurídica gratuita.",
            "A ser informado/a del avance de tu caso.",
            "A la reparación del daño.",
        ],
        "pasos": [
            "Ponte a salvo y, si hay lesiones, busca atención médica.",
            "Conserva pruebas: fotos, mensajes, ticket, videos, nombres de testigos.",
            "Denuncia ante el <b>Ministerio Público</b> de la Fiscalía del Edomex (también puedes iniciar por teléfono o por la AppFGJEM).",
            "Acude a la <b>CEAVEM</b> para solicitar asesoría jurídica y acompañamiento.",
        ],
        "contactos": ["fgjem", "ceavem", "089", "911"],
        "fundamento": "Ley General de Víctimas; CPEUM Art. 20 apartado C.",
    },
    {
        "id": "violencia_digital",
        "titulo": "Violencia digital y ciberacoso",
        "emoji": "📱",
        "boton": "Ciberacoso o fotos íntimas",
        "keywords": [
            ("ciberacoso", 4), ("ciberbullying", 4), ("fotos intimas", 4), ("nudes", 3),
            ("difundieron", 3), ("difunden", 3), ("ley olimpia", 4), ("sextors", 4),
            ("me chantajean", 3), ("chantaje", 3), ("suplantan", 3), ("hackearon", 3),
            ("redes sociales", 2), ("video intimo", 4), ("me graban", 2), ("filtraron", 3),
            ("bullying", 3), ("deepfake", 4), ("foto falsa", 3), ("montaje", 2),
        ],
        "intro": (
            "Difundir imágenes íntimas sin consentimiento, acosar o chantajear por internet <b>puede ser delito</b> "
            "(la llamada <b>Ley Olimpia</b> y otras reformas lo reconocen), aunque el contenido sea <b>real o simulado</b>. "
            "No es tu culpa."
        ),
        "derechos": [
            "Derecho a la privacidad y a que no se difundan tus imágenes íntimas sin tu consentimiento.",
            "Derecho a solicitar el retiro del contenido y a denunciar.",
            "Derecho a atención psicológica y jurídica.",
        ],
        "pasos": [
            "<b>No borres nada.</b> Captura pantalla con fecha, usuario y enlace; conserva el teléfono y los mensajes originales (la evidencia digital es frágil y se puede perder).",
            "Reporta el contenido en la plataforma para solicitar su retiro.",
            "Si te chantajean (sextorsión), <b>no pagues ni cedas</b>; corta contacto y guarda las pruebas.",
            "Denuncia ante el Ministerio Público de la Fiscalía del Edomex y pide <b>medidas de protección</b> y el retiro del contenido.",
            "<b>Si la imagen es de una persona menor de 18 años:</b> no la reenvíes ni la guardes; avisa a un adulto de confianza y denuncia de inmediato.",
            "Pide apoyo emocional; no tienes que cargarlo en soledad.",
            "Para entender qué sanciona la ley, pulsa “¿Qué es la Ley Olimpia?”.",
        ],
        "relacionados": ["ley_olimpia", "caso_foto_intima"],
        "contactos": ["fgjem", "sin_violencia", "uaemex_psico", "911"],
        "fundamento": "Reformas conocidas como Ley Olimpia (leyes federales y estatales); CPEUM Art. 6° y 16.",
    },
    {
        "id": "trata",
        "titulo": "Trata de personas",
        "emoji": "🧭",
        "keywords": [
            ("trata", 3), ("explotacion", 3), ("me retienen", 4), ("no me dejan salir", 4),
            ("me quitaron mis documentos", 4), ("oferta de trabajo falsa", 3), ("deuda", 1),
        ],
        "intro": "La trata de personas es un delito grave que vulnera la libertad y la dignidad. Hay señales que ayudan a reconocerla.",
        "derechos": [
            "Derecho a la libertad, a la integridad y a la dignidad.",
            "Derecho a protección y atención como víctima.",
        ],
        "pasos": [
            "Señales de alerta: te quitan documentos, te impiden salir o comunicarte, te exigen pagar una \"deuda\" o la oferta de trabajo no coincide con la realidad.",
            "No confrontes a quien te retiene si ello te pone en riesgo; busca el momento seguro para pedir ayuda.",
            "Llama al <b>911</b> o a la línea contra la trata.",
        ],
        "contactos": ["911", "trata_edomex", "trata_nacional", "ceavem"],
        "fundamento": "Ley General para Prevenir, Sancionar y Erradicar los Delitos en Materia de Trata de Personas.",
    },
    # ------------------------------------------------------------------ UNIVERSIDAD
    {
        "id": "estudiante_vs_ciudadano",
        "titulo": "Derechos como estudiante y como ciudadano/a: ¿cuál es la diferencia?",
        "emoji": "🆚",
        "boton": "Estudiante vs. ciudadano/a",
        "relacionados": ["derechos_estudiante", "derechos_generales", "lista_dh"],
        "keywords": [
            ("diferencia entre mis derechos", 9), ("diferencia entre los derechos", 9),
            ("diferencia entre derechos", 9), ("diferencia entre ser estudiante", 9),
            ("como ciudadano", 8), ("como ciudadana", 8), ("derechos de ciudadano", 8),
            ("derechos del ciudadano", 8), ("derechos de un ciudadano", 8), ("derechos ciudadanos", 8),
            ("estudiante y ciudadano", 9), ("ciudadano y estudiante", 9), ("ciudadania", 4), ("ciudadano", 4),
            ("ciudadana", 4), ("es lo mismo", 2), ("diferencia", 2),
        ],
        "intro": (
            "Son <b>capas distintas que se suman</b>, no derechos que se sustituyen. Ser estudiante <b>no te quita</b> ningún derecho que tienes como persona."
        ),
        "derechos_titulo": "Cómo se distinguen",
        "derechos": [
            "<b>Como persona (derechos humanos):</b> los tienes siempre, desde que naces, sin importar tu edad o nacionalidad: dignidad, igualdad y no discriminación, "
            "integridad, libertad de expresión, privacidad, acceso a la justicia, educación, salud, etc. (Art. 1° CPEUM). Dentro de la Facultad siguen vigentes.",
            "<b>Como ciudadano/a:</b> la ciudadanía es un <b>estatus legal</b> que se adquiere al cumplir 18 años siendo mexicano/a (Art. 34 CPEUM). "
            "Añade <b>derechos políticos</b>, como votar, ser votado/a para cargos públicos, asociarte para asuntos políticos del país y participar en la vida pública (Art. 35). "
            "Una persona menor de 18 años tiene derechos humanos, pero aún no es ciudadana en sentido legal.",
            "<b>Como estudiante:</b> es una <b>condición dentro de la universidad</b>. Te da derechos universitarios (por ejemplo, conocer los criterios de evaluación, "
            "pedir revisión de examen, ser escuchado/a antes de una sanción, usar los servicios de apoyo) y también <b>obligaciones</b> (reglamentos, normas de convivencia) "
            "que reconoce la Legislación Universitaria de la UAEMéx.",
            "<b>Límite importante:</b> los reglamentos de la universidad <b>no pueden violar</b> tus derechos humanos. Si una norma o una autoridad universitaria los afecta, "
            "puedes reclamarlo ante la Defensoría de los Derechos Universitarios y, según el caso, ante la CODHEM.",
        ],
        "pasos_titulo": "Un ejemplo",
        "pasos": [
            "Votar en elecciones: derecho de <b>ciudadano/a</b> (si tienes 18 años o más).",
            "Que no te humillen ni discriminen en clase: derecho de <b>toda persona</b>, y además lo protege la normatividad universitaria.",
            "Pedir revisión de un examen: derecho de <b>estudiante</b>.",
        ],
        "contactos": ["defensoria_uaemex", "codhem"],
        "fundamento": "CPEUM Arts. 1°, 34 y 35; Legislación Universitaria de la UAEMéx.",
    },
    {
        "id": "derechos_estudiante",
        "titulo": "Tus derechos como estudiante",
        "emoji": "🎓",
        "boton": "Mis derechos como estudiante",
        "relacionados": ["estudiante_vs_ciudadano", "derechos_generales", "violencia_docente", "proteccion_menores"],
        "keywords": [
            ("derechos como estudiante", 9), ("derechos de los estudiantes", 9), ("derechos del estudiante", 9),
            ("derechos del alumno", 9), ("derechos de los alumnos", 9), ("derechos de un estudiante", 9),
            ("mis derechos en la escuela", 8), ("mis derechos en la facultad", 8), ("mis derechos universitarios", 8),
            ("estudiante", 3), ("alumno", 3), ("alumna", 3), ("escuela", 2), ("facultad", 2),
            ("calificacion", 3), ("reprobar", 2), ("reprobaron", 3), ("injusto", 2),
            ("maestro", 2), ("profesor", 2), ("docente", 2), ("inscripcion", 3), ("beca", 3),
            ("derechos universitarios", 4), ("sancion", 3), ("expulsar", 3), ("expulsion", 3),
            ("baja", 1), ("revision de examen", 4), ("derecho a la educacion", 4), ("educacion", 2),
            ("me humilla", 2), ("me grita", 2), ("me trata mal", 3), ("abuso de autoridad", 3),
        ],
        "intro": (
            "Como estudiante tienes <b>dos tipos de derechos</b>: los <b>derechos humanos que tiene toda persona</b> "
            "(los “normales”, que nadie te quita por ser estudiante) y los <b>derechos universitarios</b> que reconoce la "
            "legislación de la UAEMéx."
        ),
        "derechos_titulo": "Tus derechos",
        "derechos": [
            "<b>Como persona (derechos humanos):</b> dignidad, igualdad y no discriminación (Art. 1°); libertad de expresión, de petición y de "
            "asociación (Arts. 6°, 8° y 9°); privacidad y protección de tus datos personales (Art. 16); integridad y una vida libre de violencia.",
            "<b>Como estudiante:</b> derecho a la educación (Art. 3°) sin discriminación y en un entorno seguro y libre de violencia.",
            "Trato digno y respetuoso de docentes y autoridades.",
            "Conocer los criterios con que eres evaluado/a y pedir revisión conforme a la normatividad universitaria.",
            "Ser escuchado/a antes de que se te imponga una sanción.",
            "Acceder a los servicios de apoyo de la universidad, incluidos los de salud mental.",
            "Presentar quejas o peticiones <b>sin sufrir represalias</b> académicas.",
            "Si eres <b>menor de 18 años</b>, además tienes los derechos de niñas, niños y adolescentes (pulsa “Protección de menores”).",
        ],
        "pasos": [
            "Revisa la <b>Legislación Universitaria</b> de la UAEMéx (Estatuto Universitario y reglamentos aplicables).",
            "Plantea el problema primero con tu docente o la coordinación correspondiente, <b>por escrito</b> y conservando acuse.",
            "Si no hay respuesta o se afecta tu derecho, acude a la <b>Defensoría de los Derechos Universitarios</b>.",
            "Si se trata de violencia, discriminación o abuso de autoridad, también puedes acudir a la CODHEM.",
        ],
        "contactos": ["defensoria_uaemex", "uaemex_portal", "uaemex_general", "codhem"],
        "fundamento": "CPEUM Art. 3° y 1°; Legislación Universitaria de la UAEMéx.",
    },
    {
        "id": "salud_mental",
        "titulo": "Apoyo psicológico – Facultad de Ingeniería UAEMéx",
        "emoji": "💛",
        "boton": "Apoyo psicológico",
        "keywords": [
            ("psico", 3), ("emocional", 3), ("salud mental", 4), ("ansiedad", 4), ("depresion", 4),
            ("deprimid", 3), ("triste", 3), ("estres", 3), ("agobiad", 3), ("terapia", 3),
            ("no puedo dormir", 3), ("panico", 3), ("burnout", 3),
            ("me siento solo", 4), ("me siento sola", 4), ("desahog", 3), ("sin ganas", 3), ("no tengo ganas", 3),
            ("me siento triste", 4), ("me siento mal", 3), ("solo", 1), ("sola", 1),
        ],
        "intro": (
            "Cuidar tu salud mental es un derecho. Como integrante de la comunidad de la Facultad de Ingeniería "
            "puedes acceder a atención psicológica y orientación."
        ),
        "pasos": [
            "Entra al servicio de atención psicológica de la Facultad para conocer cómo solicitar tu cita.",
            "Si la situación te rebasa, la Línea de la Vida atiende apoyo emocional.",
            "Si sientes que puedes hacerte daño, llama al <b>911</b> ahora.",
        ],
        "contactos": ["uaemex_psico", "uaemex_clinica", "uaemex_general", "linea_vida"],
        "fundamento": "Derecho a la protección de la salud (Art. 4° CPEUM).",
    },
    {
        "id": "privacidad_datos",
        "titulo": "Privacidad y datos personales",
        "emoji": "🔒",
        "boton": "Mis datos personales",
        "keywords": [
            ("datos personales", 4), ("privacidad", 3), ("aviso de privacidad", 4), ("arco", 2),
            ("mi informacion", 2), ("compartieron mis datos", 4), ("difundieron mis datos", 4),
            ("mi curp", 2), ("mi foto", 2), ("transparencia", 3), ("acceso a la informacion", 3),
        ],
        "intro": "Tus datos personales (nombre, domicilio, calificaciones, salud, imagen, etc.) están protegidos por la ley.",
        "derechos": [
            "Derechos <b>ARCO</b>: <b>A</b>cceder a tus datos, <b>R</b>ectificarlos, <b>C</b>ancelarlos y <b>O</b>ponerte a su uso.",
            "Conocer el <b>aviso de privacidad</b> de quien los recaba y para qué los usa.",
            "Acceder a información pública de las instituciones (transparencia).",
        ],
        "pasos": [
            "Solicita por escrito al responsable (por ejemplo, la Unidad de Transparencia de la institución) el ejercicio de tu derecho.",
            "Si no responden o la respuesta es insuficiente, puedes acudir al órgano garante de transparencia y datos personales del Estado de México.",
        ],
                "contactos": ["infoem"],
        "fundamento": "CPEUM Art. 6° y 16; legislación vigente de protección de datos personales en posesión de sujetos obligados (verifica la ley estatal aplicable).",
    },
    {
        "id": "privacidad_bot",
        "titulo": "¿Qué datos guarda este asistente?",
        "emoji": "🔐",
        "boton": "Privacidad de este chat",
        "relacionados": ["privacidad_datos"],
        "keywords": [
            ("que datos guardas", 9), ("que datos guarda", 9), ("guardas mis mensajes", 9), ("guardan mis mensajes", 9),
            ("guardas mis datos", 9), ("guardan mis datos", 9), ("aviso de privacidad del chat", 9),
            ("privacidad de este chat", 9), ("es privado este chat", 9), ("es seguro este chat", 8),
            ("es confidencial", 6), ("que haces con mis datos", 9), ("usan mis datos", 8),
        ],
        "intro": (
            "<b>No guardo tus mensajes.</b> Lo que escribes se procesa en la memoria del servidor solo para elegir una respuesta. "
            "No te pido nombre, correo ni cuenta, no uso cookies de seguimiento y <b>no envío tus mensajes a terceros</b> ni a ninguna IA externa."
            "<div class='mt-2'>El servicio de alojamiento puede registrar datos técnicos de conexión (como la IP). "
            "Por eso, <b>evita escribir datos que te identifiquen</b> (nombre completo, matrícula, teléfono).</div>"
            "<div class='mt-2'>Consulta el <a href='/privacidad' class='text-emerald-700 underline font-semibold'>aviso de privacidad completo</a>, "
            "que incluye cómo ejercer tus derechos ARCO.</div>"
        ),
        "fundamento": "Aviso de privacidad del proyecto; CPEUM Art. 6° y 16.",
    },
    {
        "id": "uaemex_servicios",
        "titulo": "Servicios y contactos – Facultad de Ingeniería UAEMéx",
        "emoji": "🏫",
        "boton": "Contactos de la Facultad",
        "keywords": [
            ("ingenieria", 3), ("uaemex", 3), ("uaem", 3), ("universidad", 2), ("facultad", 1), ("contacto", 2),
            ("telefono", 2), ("directorio", 3), ("donde acudo", 2), ("a quien acudo", 2),
        ],
        "intro": "Estos son los servicios y contactos de la comunidad universitaria que pueden orientarte:",
        "pasos": [
            "Atención psicológica y salud mental.",
            "Defensoría de los Derechos Universitarios, para quejas por afectación de tus derechos.",
            "Portal oficial de la Facultad para trámites y avisos.",
        ],
        "contactos": ["uaemex_psico", "uaemex_clinica", "defensoria_uaemex", "uaemex_portal", "uaemex_general"],
        "fundamento": "Información pública de la UAEMéx.",
    },
    # ------------------------------------------------------------------ CONCEPTOS
    {
        "id": "que_son_dh",
        "titulo": "¿Qué son los derechos humanos?",
        "emoji": "📖",
        "boton": "¿Qué son los derechos humanos?",
        "relacionados": ["lista_dh", "derechos_generales", "derechos_estudiante"],
        "keywords": [
            ("que son los derechos humanos", 6), ("que son los derechos", 5), ("que son derechos humanos", 6),
            ("que significa derechos humanos", 6), ("que son mis derechos", 5),
            ("que es un derecho humano", 6), ("que es derecho humano", 6),
            ("para que sirven los derechos", 6), ("para que sirven los derechos humanos", 6),
            ("importancia de los derechos humanos", 5), ("definicion de derechos humanos", 6),
            ("concepto de derechos humanos", 6), ("quien creo los derechos humanos", 6),
            ("origen de los derechos humanos", 6), ("historia de los derechos humanos", 6),
            ("definicion", 2), ("concepto", 2),
        ],
        "intro": (
            "Los <b>derechos humanos</b> son los derechos que tiene toda persona por el simple hecho de serlo, "
            "sin importar su origen, género, edad, religión, condición social u otra característica. "
            "Protegen tu dignidad, tu libertad y tu posibilidad de vivir y desarrollarte plenamente."
            "<div class='mt-3 font-semibold'>Características</div>"
            "<ul class='list-disc pl-5 space-y-1'>"
            "<li><b>Universales:</b> son para todas las personas.</li>"
            "<li><b>Inalienables:</b> no se pueden quitar ni renunciar a ellos.</li>"
            "<li><b>Interdependientes e indivisibles:</b> están conectados; no se puede respetar unos y violar otros.</li>"
            "<li><b>Progresivos:</b> el Estado no puede retroceder en su protección.</li>"
            "</ul>"
            "<div class='mt-3 font-semibold'>De dónde vienen</div>"
            "<ul class='list-disc pl-5 space-y-1'>"
            "<li>A nivel mundial, la <b>Declaración Universal de los Derechos Humanos</b> (ONU, 1948).</li>"
            "<li>En México, el <b>Artículo 1° de la Constitución</b>, reforzado por la reforma de derechos humanos de 2011: "
            "todas las autoridades deben promoverlos, respetarlos, protegerlos y garantizarlos.</li>"
            "</ul>"
        ),
        "fundamento": "CPEUM Art. 1°; Declaración Universal de los Derechos Humanos (ONU, 1948).",
    },
    {
        "id": "glosario_instituciones",
        "titulo": "Qué es cada instancia y cómo funciona una queja",
        "emoji": "🏛️",
        "boton": "¿Qué es la CODHEM / una queja?",
        "relacionados": ["derechos_generales", "donde_ayuda"],
        "keywords": [
            ("que es la codhem", 6), ("que es codhem", 6), ("que hace la codhem", 6), ("que es la cndh", 6),
            ("que es la ceavem", 6), ("que es la defensoria", 6), ("que es una queja", 6),
            ("como presento una queja", 5), ("como pongo una queja", 5), ("como hago una queja", 5),
            ("que es un derecho universitario", 6), ("que son los derechos universitarios", 6),
            ("que es el ombudsman", 6), ("codhem", 3), ("cndh", 3), ("ceavem", 3), ("defensoria", 3), ("queja", 1),
        ],
        "intro": (
            "Quién es quién cuando quieres hacer valer tus derechos:"
            "<ul class='list-disc pl-5 space-y-1 mt-2'>"
            "<li><b>CODHEM:</b> organismo público de derechos humanos del Estado de México. Recibe quejas por presuntas "
            "violaciones cometidas por autoridades o servidores públicos estatales y municipales. Es gratuito.</li>"
            "<li><b>CNDH:</b> su equivalente a nivel nacional, para autoridades federales.</li>"
            "<li><b>Defensoría de los Derechos Universitarios:</b> instancia dentro de la universidad que atiende quejas "
            "por afectación a los derechos que la legislación universitaria reconoce a estudiantes y personal.</li>"
            "<li><b>CEAVEM:</b> atiende a víctimas de delitos y de violaciones a derechos humanos (asesoría jurídica, "
            "atención psicológica y otras medidas de ayuda).</li>"
            "<li><b>Fiscalía / Ministerio Público:</b> es donde se denuncian los <i>delitos</i>.</li>"
            "<li><b>Queja:</b> es contar por escrito (o en línea) los hechos que consideras que violaron tus derechos para "
            "que el organismo los investigue. No necesitas abogado, y conviene presentarla pronto porque suele tener plazo.</li>"
            "</ul>"
        ),
        "contactos": ["codhem", "cndh", "ceavem", "defensoria_uaemex"],
        "fundamento": "CPEUM Art. 102 apartado B; Ley General de Víctimas.",
    },
    # ================================================================== AMPLIACIÓN DEL TEMARIO
    # ------------------------------------------------------------------ URGENTE: MENORES
    {
        "id": "emergencia_menores",
        "titulo": "Si una niña, niño o adolescente está siendo violentado",
        "emoji": "🚸",
        "boton": "Menor en peligro o violentado",
        "urgente": True,
        "urgente_min": 6,  # exige más señales para no saltar en preguntas informativas
        "relacionados": ["proteccion_menores", "caso_menor", "donde_ayuda"],
        "keywords": [
            ("maltrato infantil", 6), ("abuso infantil", 6), ("violencia infantil", 6),
            ("abuso sexual infantil", 6), ("menor de edad", 3), ("menores de edad", 3),
            ("numeros de emergencia", 3),
            ("nino", 2), ("nina", 2), ("adolescente", 2), ("menor", 1),
            ("hijo", 1), ("hija", 1), ("sobrino", 1), ("sobrina", 1),
            ("hermanito", 2), ("hermanita", 2), ("soy menor", 3),
            ("violent", 3), ("maltrat", 3), ("abus", 3), ("golpe", 3), ("pega", 3),
            ("lastim", 3), ("agred", 3), ("tocamient", 3), ("secuestr", 3),
            ("desaparec", 3), ("abandon", 3), ("amenaz", 2),
        ],
        "intro": (
            "Ante cualquier sospecha de que una niña, niño o adolescente es maltratado, abusado o está en riesgo, "
            "<b>actuar rápido importa</b>. En el Estado de México la ley obliga a <b>cualquier persona</b> que sepa de un "
            "caso a avisar de inmediato a las autoridades. Se entiende por <b>maltrato</b> toda acción u omisión "
            "intencional (incluido el trato negligente) que afecta los derechos o el bienestar de una niña, niño o "
            "adolescente, o daña su salud o su desarrollo, ejercida por personas o por instituciones."
        ),
        "pasos_titulo": "Qué hacer ahora",
        "pasos": [
            "<b>Peligro inmediato</b> (golpes en curso, agresión sexual, alguien lo retiene o se lo llevan): llama al <b>911</b>.",
            "Ponle a salvo: aléjalo del agresor solo si puedes hacerlo <b>sin ponerte en riesgo</b>, y llévalo con adultos de confianza.",
            "<b>Escúchalo con calma</b>: créele, dile que no es su culpa y que hizo bien en contarlo. No lo presiones ni le "
            "hagas repetir la historia varias veces, y no confrontes tú al agresor.",
            "Si hay lesiones o agresión sexual, busca <b>atención médica</b> cuanto antes y, si puedes, evita que se bañe o "
            "cambie de ropa hasta que lo valore personal médico o el Ministerio Público.",
            "<b>Avisa a las autoridades:</b> denuncia ante el Ministerio Público (Fiscalía), por teléfono de forma anónima al <b>089</b> "
            "y da aviso a la <b>Procuraduría de Protección de Niñas, Niños y Adolescentes</b> (DIF de tu municipio o DIFEM). "
            "Si ocurrió en una escuela, informa también a la dirección.",
            "<b>Si el menor eres tú:</b> si estás en peligro llama al 911; cuéntalo hoy a un adulto de confianza "
            "(familiar, docente, orientador/a). No es tu culpa. También puedes llamar a la Línea de la Vida para que te escuchen.",
        ],
        "contactos": ["911", "089", "fgjem", "procuraduria_nna", "sin_violencia", "linea_vida", "codhem"],
        "fundamento": "Ley de los Derechos de Niñas, Niños y Adolescentes del Estado de México (Arts. 9 y 26); Ley General de Víctimas; CPEUM Art. 4°.",
    },
    # ------------------------------------------------------------------ MENORES (INFORMATIVO)
    {
        "id": "proteccion_menores",
        "titulo": "Protección de niñas, niños y adolescentes",
        "emoji": "🧒",
        "boton": "Protección de menores de edad",
        "relacionados": ["emergencia_menores", "caso_menor", "derechos_estudiante"],
        "keywords": [
            ("proteccion de menores", 8), ("proteccion a menores", 8), ("proteccion de la ninez", 8),
            ("proteccion de ninos", 8), ("derechos de los ninos", 8), ("derechos de las ninas", 8),
            ("derechos de ninas ninos", 8), ("derechos de los menores", 8), ("derechos del nino", 8),
            ("derechos de los adolescentes", 8), ("interes superior", 6), ("procuraduria de proteccion", 6),
            ("menores de edad", 4), ("menor de edad", 3), ("ninez", 4), ("adolescente", 2),
            ("acoso escolar", 4), ("violencia escolar", 4), ("nino", 2), ("nina", 2), ("bullying", 3),
        ],
        "intro": (
            "Las <b>niñas y niños</b> (menores de 12 años) y los <b>adolescentes</b> (de 12 años cumplidos a menos de 18) "
            "tienen derechos propios y una protección reforzada. En el Estado de México los reconoce la <b>Ley de los Derechos "
            "de Niñas, Niños y Adolescentes del Estado de México</b>, que se apoya en la Ley General. Su principio central es el "
            "<b>interés superior de la niñez</b>: en toda decisión que los afecte debe pesar primero lo que más los beneficia."
        ),
        "derechos_titulo": "Algunos de sus derechos",
        "derechos": [
            "<b>Vida, supervivencia y desarrollo</b>, y a vivir en familia.",
            "<b>Una vida libre de violencia</b> y a que se resguarde su integridad personal (Art. 26).",
            "<b>Igualdad y no discriminación.</b>",
            "<b>Educación</b>, en un ambiente libre de violencia y de discriminación; las autoridades deben prevenir y atender "
            "el acoso y la violencia escolar. Ninguna institución puede negar el ingreso o la permanencia a una adolescente embarazada o lactante.",
            "<b>Salud, alimentación nutritiva</b> y bienestar para su sano desarrollo.",
            "<b>Libertad de expresión, de pensamiento, conciencia y religión</b>, y acceso a la información.",
            "<b>Intimidad</b> (privacidad) y <b>participación</b>: a opinar sobre los asuntos que les afectan.",
            "<b>Seguridad jurídica y debido proceso</b>, y a la inclusión si tienen alguna discapacidad.",
            "Acceso a las <b>tecnologías de la información</b> (con protección frente a riesgos en línea).",
        ],
        "pasos_titulo": "Qué debes saber y hacer",
        "pasos": [
            "<b>Es obligación de toda persona</b> que sepa que a una niña, niño o adolescente le están violando sus derechos "
            "avisar de inmediato a las autoridades competentes (Art. 9). No es “meterse”: es un deber legal.",
            "La <b>Procuraduría de Protección</b> (DIF municipal o estatal) puede dictar medidas de protección y restituir "
            "derechos; si hay un delito interviene también el Ministerio Público.",
            "Escuelas y autoridades educativas deben tener <b>protocolos</b> contra el acoso y la violencia escolar.",
            "Si eres menor de edad y alguien te lastima, te acosa o te presiona: busca a un adulto de confianza y cuéntalo. "
            "Si estás en peligro, llama al <b>911</b>.",
            "Si necesitas actuar ahora por un menor en riesgo, pulsa “Menor en peligro o violentado”.",
        ],
        "contactos": ["911", "procuraduria_nna", "fgjem", "codhem", "sin_violencia"],
        "fundamento": "Ley de los Derechos de Niñas, Niños y Adolescentes del Estado de México (Arts. 9, 10, 26, 28 a 30); Ley General de los Derechos de NNA; CPEUM Art. 4°.",
    },
    # ------------------------------------------------------------------ DERECHOS: LISTA COMPLETA
    {
        "id": "lista_dh",
        "titulo": "Los derechos humanos, explicados",
        "emoji": "📜",
        "boton": "Lista de derechos humanos",
        "relacionados": ["que_son_dh", "derechos_estudiante", "casos_practicos"],
        "keywords": [
            ("cuales son los derechos humanos", 9), ("lista de derechos", 8), ("lista de los derechos", 8),
            ("derechos humanos fundamentales", 8), ("declaracion universal", 7), ("dudh", 7),
            ("30 articulos", 7), ("treinta articulos", 7), ("tipos de derechos", 8),
            ("clasificacion de los derechos", 8), ("generaciones de derechos", 8),
            ("derechos civiles", 4), ("derechos politicos", 4), ("derechos sociales", 4),
            ("explicame los derechos", 7), ("informacion sobre los derechos humanos", 8),
        ],
        "intro": (
            "La <b>Declaración Universal de los Derechos Humanos</b> (ONU, 10 de diciembre de 1948) tiene <b>30 artículos</b> y es "
            "la base de los derechos humanos en el mundo. En México, el <b>Art. 1° de la Constitución</b> los reconoce y obliga a "
            "todas las autoridades a promoverlos, respetarlos, protegerlos y garantizarlos. Se suelen agrupar en <i>civiles y políticos</i>, "
            "<i>económicos, sociales y culturales</i> y <i>colectivos</i> (paz, medio ambiente sano, desarrollo)."
        ),
        "derechos_titulo": "Resumen de la Declaración Universal",
        "derechos": [
            "<b>Dignidad e igualdad (Arts. 1, 2 y 7):</b> todas las personas nacen libres e iguales en dignidad y derechos, sin "
            "distinción de raza, color, sexo, idioma, religión, opinión, origen, posición económica u otra condición.",
            "<b>Vida, libertad y seguridad (Arts. 3 a 6):</b> derecho a la vida, la libertad y la seguridad personal; prohibición de la "
            "esclavitud, la tortura y los tratos crueles, inhumanos o degradantes; reconocimiento como persona ante la ley.",
            "<b>Justicia (Arts. 8 a 11):</b> recurso efectivo ante los tribunales, nadie puede ser detenido arbitrariamente, juicio "
            "justo e imparcial y presunción de inocencia.",
            "<b>Vida privada y movimiento (Arts. 12 a 15):</b> protección de tu vida privada, familia, domicilio y correspondencia; "
            "libre circulación; asilo; derecho a una nacionalidad.",
            "<b>Familia y propiedad (Arts. 16 y 17):</b> casarte y formar una familia con libre consentimiento; tener propiedad.",
            "<b>Libertades (Arts. 18 a 20):</b> pensamiento, conciencia y religión; opinión y expresión; reunión y asociación pacíficas.",
            "<b>Participación política (Art. 21):</b> participar en el gobierno de tu país y elegir en elecciones libres.",
            "<b>Derechos económicos, sociales y culturales (Arts. 22 a 27):</b> seguridad social, trabajo digno, descanso, un nivel de vida "
            "adecuado (alimentación, vivienda, salud), educación y participación en la vida cultural.",
            "<b>Orden y deberes (Arts. 28 a 30):</b> un orden social donde estos derechos se cumplan, deberes hacia la comunidad, y "
            "ningún derecho puede usarse para destruir los de otras personas.",
        ],
        "fundamento": "Declaración Universal de los Derechos Humanos (ONU, 1948), Arts. 1 a 30; CPEUM Art. 1°.",
    },
    # ------------------------------------------------------------------ DISCRIMINACIÓN: CÓMO SABER
    {
        "id": "discriminacion_como_saber",
        "titulo": "¿Cómo saber si me discriminan?",
        "emoji": "🔎",
        "boton": "¿Cómo sé si me discriminan?",
        "relacionados": ["discriminacion", "caso_discriminacion", "donde_ayuda"],
        "keywords": [
            ("como saber si me discriminan", 9), ("como se si me discriminan", 9),
            ("como saber si es discriminacion", 9), ("como saber si hay discriminacion", 9),
            ("como identificar la discriminacion", 9), ("es discriminacion", 6), ("que es discriminacion", 8),
            ("que es la discriminacion", 8), ("tipos de discriminacion", 8), ("senales de discriminacion", 8),
            ("ejemplos de discriminacion", 8), ("me estan discriminando", 5), ("estoy siendo discriminad", 6),
        ],
        "intro": (
            "<b>Discriminar</b> es dar un trato distinto, excluir o negar algo a una persona <b>por una característica suya</b>, "
            "de manera que se afecten su dignidad o el ejercicio de sus derechos. Para saber si es tu caso, hazte estas tres preguntas:"
        ),
        "derechos_titulo": "Las 3 preguntas clave",
        "derechos": [
            "<b>¿Me trataron distinto?</b> Me negaron algo (inscripción, beca, servicio, participación), me excluyeron, me humillaron "
            "o recibí peores condiciones que otras personas en una situación parecida.",
            "<b>¿Fue por una característica mía?</b> La Constitución menciona: origen étnico o nacional, género, edad, discapacidades, "
            "condición social, condiciones de salud, religión, opiniones, preferencias sexuales, estado civil, o cualquier otra que atente contra la dignidad humana.",
            "<b>¿Afectó mi dignidad o mis derechos?</b> Por ejemplo, mi acceso a la educación, al trabajo, a la salud o a un trato digno.",
        ],
        "pasos_titulo": "Señales, ejemplos y matices",
        "pasos": [
            "<b>Ejemplos:</b> te niegan una beca o inscripción por tu origen o religión; burlas constantes por tu orientación sexual, tu forma de hablar o tu aspecto; "
            "no te dan <i>ajustes razonables</i> pese a tener una discapacidad; te excluyen de un equipo o proyecto por ser mujer; te tratan peor por tu condición económica.",
            "<b>Pistas:</b> comentarios que mencionan tu característica, un patrón (solo a ti o a tu grupo), decisiones sin explicación razonable, o reglas que parecen neutras pero te perjudican de manera desproporcionada.",
            "<b>Matiz importante:</b> una calificación baja o un desacuerdo con un docente <b>no es discriminación por sí solo</b>; lo es cuando la causa es una "
            "característica personal o hay un trato desigual sin justificación razonable. Si dudas, documenta y consulta.",
            "<b>Siguiente paso:</b> anota fecha, lugar, quién, qué dijo o hizo y testigos; guarda mensajes y capturas; pide por escrito el motivo de la decisión. "
            "Luego puedes acudir a la Defensoría universitaria o presentar una queja en la CODHEM.",
        ],
        "contactos": ["codhem", "defensoria_uaemex", "conapred", "cndh"],
        "fundamento": "CPEUM Art. 1° (último párrafo); Ley Federal para Prevenir y Eliminar la Discriminación; Declaración Universal de los Derechos Humanos, Arts. 1, 2 y 7.",
    },
    # ------------------------------------------------------------------ VIOLENCIA DE UN DOCENTE
    {
        "id": "violencia_docente",
        "titulo": "Si un profesor o profesora te violenta",
        "emoji": "🧑‍🏫",
        "boton": "Violencia de un profesor",
        "relacionados": ["acoso_hostigamiento", "caso_humillacion", "donde_ayuda"],
        "keywords": [
            ("violencia docente", 8), ("violencia de un profesor", 8), ("violencia de un maestro", 8),
            ("me siento violentada", 7), ("me siento violentado", 7), ("violentada por", 6), ("violentado por", 6),
            ("me violent", 4), ("me humilla", 3), ("me grita", 3), ("me insulta", 3), ("se burla de mi", 3),
            ("me ridiculiza", 3), ("amenaza con reprobar", 6), ("me amenaza", 2), ("humilla", 2), ("grita", 2),
            ("profesor", 1), ("profesora", 1), ("maestro", 1), ("maestra", 1), ("docente", 1),
            ("abuso de poder", 3), ("represalia", 3),
        ],
        "intro": (
            "Un docente tiene autoridad académica, pero <b>nunca derecho a humillarte, amenazarte, discriminarte o agredirte</b>. "
            "Lo que sientes importa y puedes actuar, aunque dependas de su calificación."
        ),
        "derechos_titulo": "Formas en que puede aparecer",
        "derechos": [
            "<b>Verbal o psicológica:</b> gritos, insultos, burlas, humillarte frente al grupo, amenazas con reprobarte o con represalias.",
            "<b>Abuso de poder académico:</b> calificar como castigo o por simpatía, negarte una revisión, condicionar tu evaluación a favores.",
            "<b>Discriminatoria:</b> trato distinto por tu género, origen, discapacidad, religión, condición económica u otra característica.",
            "<b>Sexual:</b> insinuaciones, tocamientos o condicionar calificaciones a cambio de salir o de favores. Eso es hostigamiento o acoso sexual (pulsa el tema relacionado).",
            "<b>Física</b> o por <b>medios digitales</b> (mensajes, fotos, redes).",
        ],
        "pasos": [
            "<b>Tu seguridad primero:</b> si hay agresión física o sexual o amenaza de daño, sal del lugar, busca a alguien y llama al <b>911</b>.",
            "<b>Documenta:</b> fecha, hora, lugar, qué dijo o hizo, quién lo vio, capturas, correos y mensajes. Escríbelo cuanto antes, mientras lo recuerdas.",
            "<b>No lo cargues sola/o:</b> cuéntalo a alguien de confianza; el servicio de atención psicológica de la Facultad puede acompañarte.",
            "Preséntalo <b>por escrito</b> y con acuse ante la coordinación o la dirección de la Facultad. Si no responden o el problema es con ellas, acude a la <b>Defensoría de los Derechos Universitarios</b>.",
            "Si es de tipo <b>sexual</b>, acude a la Línea Sin Violencia y al Ministerio Público; si es <b>discriminación o abuso de autoridad</b>, puedes consultar a la CODHEM.",
            "Tienes derecho a <b>no sufrir represalias académicas</b> por denunciar. Si ocurren, repórtalas también por escrito.",
            "Si eres <b>menor de 18 años</b>, además te protege la Ley de los Derechos de Niñas, Niños y Adolescentes: la violencia escolar debe atenderse y las personas adultas tienen el deber de avisar.",
        ],
        "contactos": ["defensoria_uaemex", "uaemex_psico", "sin_violencia", "codhem", "fgjem", "911"],
        "fundamento": "CPEUM Arts. 1° y 3°; Ley General de Acceso de las Mujeres a una Vida Libre de Violencia (violencia en el ámbito docente); Legislación Universitaria de la UAEMéx.",
    },
    # ------------------------------------------------------------------ DIRECTORIO: DÓNDE PEDIR AYUDA
    {
        "id": "donde_ayuda",
        "titulo": "¿A dónde puedo acudir por ayuda?",
        "emoji": "🧭",
        "boton": "¿Dónde pido ayuda?",
        "relacionados": ["emergencia_menores", "violencia_docente", "glosario_instituciones"],
        "keywords": [
            ("donde puedo acudir", 8), ("donde acudir", 8), ("a donde acudo", 6), ("a donde puedo ir", 7),
            ("donde pido ayuda", 8), ("donde puedo pedir ayuda", 8), ("quien me puede ayudar", 8),
            ("quien me ayuda", 7), ("necesito ayuda", 5), ("pedir ayuda", 6), ("numeros de ayuda", 6),
            ("telefonos de ayuda", 6), ("telefonos de emergencia", 6), ("lineas de ayuda", 6),
            ("a quien acudo", 6), ("con quien hablo", 4), ("a quien le cuento", 5),
        ],
        "intro": (
            "Depende de lo que te pasó. Esta es una guía rápida; si hay <b>riesgo inmediato, llama primero al 911</b>."
        ),
        "derechos_titulo": "Según tu situación",
        "derechos": [
            "<b>Emergencia o peligro ahora:</b> 911 (24 h). Para denunciar de forma anónima: 089.",
            "<b>Un delito</b> (robo, amenazas, lesiones, violencia sexual, ciberdelitos): Ministerio Público de la Fiscalía; la CEAVEM te acompaña como víctima.",
            "<b>Violencia en pareja o familia:</b> Línea Sin Violencia (mujeres, hijas e hijos) o Hombre a Hombre.",
            "<b>Una autoridad violó tus derechos</b> (policía, servidor público): CODHEM (gratuita, atiende 24 h) o CNDH si es autoridad federal.",
            "<b>Problema dentro de la Facultad</b> (docentes, evaluaciones, sanciones, discriminación, acoso): coordinación o dirección por escrito y Defensoría de los Derechos Universitarios.",
            "<b>Niña, niño o adolescente en riesgo:</b> 911, Fiscalía y Procuraduría de Protección (DIF).",
            "<b>Apoyo emocional:</b> Línea de la Vida y atención psicológica de la Facultad.",
            "<b>Trata de personas:</b> líneas contra la trata.",
        ],
        "pasos": [
            "Si no sabes por dónde empezar, la <b>CODHEM</b> o la <b>Línea de la Vida</b> pueden orientarte.",
            "Guarda siempre las pruebas (capturas, mensajes, fotos, nombres de testigos) antes de acudir.",
            "Cuéntame tu situación con tus palabras y te doy pasos más concretos.",
        ],
        "contactos": ["911", "089", "codhem", "fgjem", "ceavem", "sin_violencia", "hombre_a_hombre",
                      "linea_vida", "procuraduria_nna", "trata_edomex", "defensoria_uaemex", "uaemex_psico", "cndh"],
        "fundamento": "Directorio de instituciones públicas del Estado de México y de la UAEMéx; verifica los teléfonos antes de usarlos, pueden cambiar.",
    },
    # ------------------------------------------------------------------ LEY OLIMPIA
    {
        "id": "ley_olimpia",
        "titulo": "Ley Olimpia: qué es y qué sanciona",
        "emoji": "⚖️",
        "boton": "¿Qué es la Ley Olimpia?",
        "relacionados": ["violencia_digital", "caso_foto_intima"],
        "keywords": [
            ("que es la ley olimpia", 9), ("que es ley olimpia", 9), ("origen de la ley olimpia", 9),
            ("quien es olimpia", 8), ("sanciones ley olimpia", 9), ("sancion de la ley olimpia", 9),
            ("ley olimpia", 5), ("violencia digital", 5), ("violencia mediatica", 6),
            ("intimidad sexual", 6), ("que es el ciberacoso", 8), ("que es ciberacoso", 8),
            ("ciberhostigamiento", 6), ("belem do para", 6), ("cedaw", 6),
        ],
        "intro": (
            "La <b>Ley Olimpia</b> no es una ley como tal: es un <b>conjunto de reformas</b> legislativas (penales y administrativas) "
            "para reconocer la <b>violencia digital</b> y sancionar los delitos que violan la <b>intimidad sexual</b> por medios digitales. "
            "Surgió a raíz de la difusión de un video íntimo no autorizado de una mujer en Puebla; la reforma se impulsó para tipificarlo y se "
            "replicó en las entidades federativas."
        ),
        "derechos_titulo": "Conductas que atentan contra la intimidad sexual",
        "derechos": [
            "<b>Grabar, fotografiar o elaborar</b> videos, audios o imágenes de contenido sexual íntimo, <b>reales o simulados</b>, sin consentimiento o mediante engaño.",
            "<b>Exponer, distribuir, difundir, exhibir, reproducir, transmitir, comercializar, ofertar, intercambiar o compartir</b> ese contenido, "
            "a sabiendas de que no hay consentimiento, por mensajes, correo, redes sociales o cualquier medio tecnológico.",
            "El consentimiento para que <b>una persona</b> reciba una imagen no es consentimiento para que se difunda a otras.",
            "La ley incluye también contenido <b>simulado</b> (por ejemplo, montajes), no solo el real.",
        ],
        "pasos_titulo": "Cómo se entiende y qué se sanciona",
        "pasos": [
            "<b>Violencia digital</b> (Ley General de Acceso de las Mujeres a una Vida Libre de Violencia, Art. 20 Quáter): acción dolosa mediante tecnologías "
            "de la información y la comunicación por la que se expone o difunde contenido íntimo sexual, real o simulado, sin consentimiento y que causa daño "
            "psicológico, emocional o a la imagen propia; incluye actos dolosos que dañen la intimidad, privacidad o dignidad de las mujeres por esos medios.",
            "<b>Violencia mediática</b> (Art. 20 Quinquies): actos en cualquier medio de comunicación que promuevan estereotipos sexistas, hagan apología de la "
            "violencia contra mujeres y niñas o difundan discurso de odio sexista.",
            "<b>Ciberacoso:</b> uso intencional de tecnologías para humillar, amenazar, ofender o insultar a una persona. A diferencia del ciberhostigamiento "
            "(un patrón de conductas), puede bastar un solo incidente.",
            "<b>Sanciones</b> (según la ficha técnica de tu material; consulta siempre el texto vigente): a nivel federal, de 3 a 6 años de prisión y multa. "
            "En el Estado de México (Código Penal, Arts. 211 Ter y 211 Quater, publicados en septiembre de 2019), entre 1 y 7 años de prisión según el supuesto, con multa.",
            "<b>Estándares internacionales:</b> la CEDAW y la Convención de Belém do Pará obligan al Estado a prevenir, sancionar y reparar la violencia contra las mujeres, incluida la digital.",
            "<b>Obligación reforzada de las autoridades:</b> dictar medidas de protección inmediatas, valorar las pruebas digitales con perspectiva de género y buscar la reparación integral del daño.",
            "Si te pasó a ti, pulsa “Ciberacoso o fotos íntimas” para ver qué hacer paso a paso.",
        ],
        "contactos": ["fgjem", "sin_violencia", "ceavem"],
        "fundamento": "Ley General de Acceso de las Mujeres a una Vida Libre de Violencia (Cap. IV Ter, Arts. 20 Quáter y 20 Quinquies); Código Penal del Estado de México (Arts. 211 Ter y 211 Quater); ficha técnica Ley Olimpia; Módulo 3, Tema 9.",
    },
    # ------------------------------------------------------------------ IA Y DERECHOS HUMANOS
    # ------------------------------------------------------------------ CASOS PRÁCTICOS (SITUACIONES HIPOTÉTICAS)
    {
        "id": "casos_practicos",
        "titulo": "Casos prácticos (situaciones hipotéticas)",
        "emoji": "🧩",
        "boton": "Casos prácticos",
        "keywords": [
            ("caso practico", 8), ("casos practicos", 8), ("situacion hipotetica", 8), ("situaciones hipoteticas", 8),
            ("caso hipotetico", 8), ("casos hipoteticos", 8), ("dame un ejemplo", 6), ("pon un ejemplo", 6),
            ("ejemplos", 3), ("ejemplo", 2), ("que pasaria si", 5), ("practicar", 3),
        ],
        "relacionados": ["caso_hostigamiento", "caso_foto_intima", "caso_discriminacion", "caso_policia",
                         "caso_menor", "caso_humillacion"],
        "intro": (
            "Elige una <b>situación hipotética</b> para ver, paso a paso, qué derechos están en juego y qué se puede hacer. "
            "Son ejemplos inventados para practicar: los nombres y hechos son ficticios."
        ),
        "fundamento": "Casos elaborados con base en la legislación citada en cada respuesta.",
    },
    {
        "id": "caso_hostigamiento",
        "titulo": "Caso práctico: el profesor que condiciona la calificación",
        "emoji": "🧩",
        "boton": "Caso: profesor y calificación",
        "keywords": [],
        "relacionados": ["casos_practicos", "acoso_hostigamiento"],
        "intro": (
            "<i>Mariana cursa cuarto semestre. Su profesor le escribe mensajes diciéndole que “podría ayudarla con su calificación” "
            "si sale a cenar con él. Ella no quiere, pero teme reprobar.</i>"
        ),
        "derechos_titulo": "Derechos en juego",
        "derechos": [
            "<b>Hostigamiento sexual:</b> hay una relación de subordinación (docente–estudiante) y se condiciona un beneficio académico.",
            "Derecho a una educación <b>libre de violencia</b> y a no sufrir represalias por negarse o denunciar.",
            "Derecho a ser escuchada sin revictimización, y a asesoría jurídica y atención psicológica.",
        ],
        "pasos_titulo": "¿Qué se puede hacer?",
        "pasos": [
            "La calificación <b>no puede depender</b> de aceptar una invitación. Mariana no tiene obligación de responder bajo presión.",
            "<b>No borrar nada:</b> guardar capturas, fechas y números o cuentas; anotar si hubo testigos.",
            "Contarlo a una persona de confianza y, si lo desea, llamar a la <b>Línea Sin Violencia</b> para orientación jurídica y psicológica.",
            "Presentar queja por escrito ante las autoridades de la Facultad y la <b>Defensoría de los Derechos Universitarios</b>, pidiendo medidas para que no tenga que convivir con la persona señalada cuando proceda.",
            "Si decide denunciar penalmente, acudir al <b>Ministerio Público</b>; la CEAVEM puede acompañarla.",
        ],
        "contactos": ["sin_violencia", "defensoria_uaemex", "fgjem", "ceavem", "uaemex_psico"],
        "fundamento": "Ley General de Acceso de las Mujeres a una Vida Libre de Violencia (hostigamiento y acoso sexual); Ley General de Víctimas; Legislación Universitaria.",
    },
    {
        "id": "caso_foto_intima",
        "titulo": "Caso práctico: la foto íntima en el grupo de WhatsApp",
        "emoji": "🧩",
        "boton": "Caso: foto íntima en un grupo",
        "keywords": [],
        "relacionados": ["casos_practicos", "ley_olimpia", "violencia_digital"],
        "intro": (
            "<i>Carla envió una foto íntima a su pareja cuando eran novios. Al terminar, él la comparte en el grupo de WhatsApp de la carrera "
            "y varios compañeros la reenvían.</i>"
        ),
        "derechos_titulo": "Derechos en juego",
        "derechos": [
            "<b>Intimidad y vida privada</b>, y derecho a una vida libre de violencia digital.",
            "Derecho a que se <b>retire el contenido</b>, a medidas de protección y a la <b>reparación del daño</b>.",
            "Derecho a atención psicológica y asesoría jurídica, sin que la culpen por haber enviado la foto.",
        ],
        "pasos_titulo": "¿Qué se puede hacer?",
        "pasos": [
            "<b>Haber enviado la foto voluntariamente no autoriza a difundirla:</b> el consentimiento fue para una persona, no para el grupo. "
            "Quien la difundió puede cometer el delito de violación a la intimidad sexual (Ley Olimpia), y quienes la reenvían también pueden incurrir en la conducta de compartir a sabiendas de que no hay consentimiento.",
            "<b>Guardar evidencia sin borrar:</b> capturas con fecha, nombres de usuario, enlaces y el nombre del grupo; conservar el teléfono y los chats originales.",
            "<b>Reportar</b> el contenido en la plataforma para solicitar su retiro.",
            "<b>Denunciar</b> ante el Ministerio Público del Estado de México y pedir medidas de protección.",
            "Avisar a las autoridades de la Facultad y a la Defensoría: quienes reenvían también pueden ser sancionados conforme a la normatividad universitaria.",
            "Buscar apoyo emocional; no tiene que enfrentarlo sola.",
        ],
        "contactos": ["fgjem", "sin_violencia", "ceavem", "uaemex_psico", "defensoria_uaemex"],
        "fundamento": "Ley General de Acceso de las Mujeres a una Vida Libre de Violencia (Art. 20 Quáter); Código Penal del Estado de México (Arts. 211 Ter y 211 Quater).",
    },
    {
        "id": "caso_discriminacion",
        "titulo": "Caso práctico: burlas y exclusión por origen",
        "emoji": "🧩",
        "boton": "Caso: exclusión por origen",
        "keywords": [],
        "relacionados": ["casos_practicos", "discriminacion_como_saber", "discriminacion"],
        "intro": (
            "<i>Tonatiuh habla náhuatl. Sus compañeros se burlan de su acento y un docente le dice que un proyecto “no es nivel para él”. "
            "Además, le niegan la entrada a un taller sin explicación, mientras a otros estudiantes sí los dejan.</i>"
        ),
        "derechos_titulo": "Derechos en juego",
        "derechos": [
            "<b>Igualdad y no discriminación</b> por origen étnico o nacional (Art. 1° CPEUM).",
            "<b>Trato digno</b> y derecho a la educación en igualdad de condiciones.",
            "Derecho a conocer <b>el motivo</b> de una decisión que lo afecta.",
        ],
        "pasos_titulo": "¿Qué se puede hacer?",
        "pasos": [
            "Aplicar las tres preguntas: ¿hubo trato distinto?, ¿por una característica suya?, ¿afectó sus derechos? Aquí las tres parecen cumplirse.",
            "Documentar el <b>patrón</b>: fechas, quién dijo qué, testigos y la negativa de entrada al taller.",
            "Pedir <b>por escrito</b> la razón de la negativa. Si no hay explicación razonable, es un indicio importante.",
            "Acudir a la Defensoría de los Derechos Universitarios y, si no se resuelve, presentar queja en la CODHEM (conviene hacerlo pronto: suele haber plazo).",
            "Un solo rechazo sin más datos no prueba discriminación; lo que la sugiere es el conjunto de comentarios, el patrón y la falta de justificación.",
        ],
        "contactos": ["defensoria_uaemex", "codhem", "conapred"],
        "fundamento": "CPEUM Art. 1° (último párrafo); Ley Federal para Prevenir y Eliminar la Discriminación.",
    },
    {
        "id": "caso_policia",
        "titulo": "Caso práctico: la patrulla y el “arreglo”",
        "emoji": "🧩",
        "boton": "Caso: patrulla pide dinero",
        "keywords": [],
        "relacionados": ["casos_practicos", "detencion_policia"],
        "intro": (
            "<i>Daniel sale de la Facultad a las 9 de la noche. Una patrulla lo detiene, lo revisa y un policía le dice que "
            "“se arregle” con dinero o se lo llevan.</i>"
        ),
        "derechos_titulo": "Derechos en juego",
        "derechos": [
            "Que le informen <b>quién lo detiene y por qué</b>.",
            "A <b>guardar silencio</b>, a un abogado/a y a avisar a un familiar.",
            "A no ser sometido a <b>extorsión, golpes ni malos tratos</b>, y a la presunción de inocencia.",
            "A ser puesto <b>sin demora</b> a disposición del Ministerio Público si hay una detención.",
        ],
        "pasos_titulo": "¿Qué se puede hacer?",
        "pasos": [
            "Mantener la calma y <b>no resistirse físicamente</b>.",
            "Preguntar nombre, corporación y número de patrulla o placa; anotarlos en cuanto sea posible.",
            "<b>No entregar dinero</b> ni firmar nada sin leerlo y sin abogado/a.",
            "Pedir que avisen a su familia o a una persona de confianza.",
            "Después: presentar <b>queja en la CODHEM</b> y denunciar ante el Ministerio Público, o hacerlo de forma anónima al 089.",
        ],
        "contactos": ["codhem", "fgjem", "089", "911"],
        "fundamento": "CPEUM Arts. 14, 16, 19, 20 y 21; Ley Nacional del Registro de Detenciones.",
    },
    {
        "id": "caso_menor",
        "titulo": "Caso práctico: el primo con moretones",
        "emoji": "🧩",
        "boton": "Caso: menor con moretones",
        "keywords": [],
        "relacionados": ["casos_practicos", "emergencia_menores", "proteccion_menores"],
        "intro": (
            "<i>Valeria cuida a su primo Emiliano, de 9 años, los fines de semana. Un día nota moretones en sus brazos y él, llorando, le dice que "
            "su papá le pega cuando se enoja y que no cuente nada.</i>"
        ),
        "derechos_titulo": "Derechos en juego",
        "derechos": [
            "Derecho de Emiliano a una <b>vida libre de violencia</b> y a que se resguarde su integridad (Art. 26).",
            "<b>Interés superior de la niñez:</b> su protección pesa más que el “secreto” o que evitar un conflicto familiar.",
            "Deber de <b>toda persona</b> de avisar a las autoridades cuando conoce un caso así (Art. 9).",
        ],
        "pasos_titulo": "¿Qué se puede hacer?",
        "pasos": [
            "Mantener la calma, <b>creerle</b> y decirle que no es su culpa. <b>No prometerle guardar el secreto</b>: explicarle que hay adultos que pueden protegerlo.",
            "No confrontar al papá ni interrogar a Emiliano varias veces; eso puede ponerlo en más riesgo.",
            "Si hay peligro inmediato, llamar al <b>911</b>; si hay lesiones, buscar atención médica.",
            "<b>Avisar a las autoridades:</b> Ministerio Público, Procuraduría de Protección (DIF) o el 089 de forma anónima. No es “meterse”: es un deber legal.",
            "La Procuraduría valora el riesgo y puede dictar <b>medidas de protección</b> para Emiliano.",
        ],
        "contactos": ["911", "089", "fgjem", "procuraduria_nna", "sin_violencia"],
        "fundamento": "Ley de los Derechos de Niñas, Niños y Adolescentes del Estado de México (Arts. 9 y 26); Ley General de Víctimas.",
    },
    {
        "id": "caso_humillacion",
        "titulo": "Caso práctico: la revisión de examen y la humillación",
        "emoji": "🧩",
        "boton": "Caso: examen y humillación",
        "keywords": [],
        "relacionados": ["casos_practicos", "violencia_docente", "derechos_estudiante"],
        "intro": (
            "<i>Pablo reprueba un parcial. Al pedir revisión, el profesor le responde frente al grupo: “si no entiendes, mejor deja la carrera” "
            "y se niega a mostrarle su examen.</i>"
        ),
        "derechos_titulo": "Derechos en juego",
        "derechos": [
            "<b>Trato digno</b>: un docente puede evaluar, pero no humillar.",
            "Derecho a conocer los <b>criterios de evaluación</b> y a pedir <b>revisión</b> conforme a la normatividad universitaria.",
            "Derecho a no sufrir <b>represalias</b> por pedir revisión.",
        ],
        "pasos_titulo": "¿Qué se puede hacer?",
        "pasos": [
            "Pedir la revisión <b>por escrito</b>, con acuse, ante la coordinación correspondiente, citando la normatividad universitaria aplicable.",
            "Anotar fecha, frase exacta y compañeros que lo presenciaron; conservar el examen, la rúbrica o los criterios si los tiene.",
            "Si la humillación se repite o no hay respuesta, acudir a la <b>Defensoría de los Derechos Universitarios</b>: una calificación puede revisarse, pero el trato indigno también es motivo de queja.",
            "Si se siente rebasado, el servicio de atención psicológica de la Facultad puede acompañarlo.",
        ],
        "contactos": ["defensoria_uaemex", "uaemex_psico", "uaemex_portal"],
        "fundamento": "CPEUM Arts. 1° y 3°; Legislación Universitaria de la UAEMéx.",
    },
]

# Tema especial: fuentes (se arma aparte porque es una lista de enlaces)
SOURCES_KEYWORDS = [("fuentes", 3), ("leyes", 3), ("documentos", 2), ("referencias", 3),
                    ("bibliografia", 3), ("de donde sacas", 3), ("base legal", 3)]

GREETING_WORDS = ["hola", "buenas", "buenos dias", "buenas tardes", "buenas noches", "que tal", "hey", "saludos"]
THANKS_WORDS = ["gracias", "muchas gracias", "te agradezco"]

# Botones rápidos que se muestran al iniciar (ids de TOPICS)
MENU_IDS = ["derechos_generales", "derechos_estudiante", "discriminacion_como_saber", "violencia_docente",
            "acoso_hostigamiento", "proteccion_menores", "emergencia_menores", "donde_ayuda",
            "casos_practicos", "violencia_digital", "salud_mental", "emergencia"]
