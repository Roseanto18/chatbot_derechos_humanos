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
    "transparencia_mx": {
        "name": "Transparencia Mexiquense – Autoridad garante local de transparencia y datos personales (sustituyó al INFOEM)",
        "phone": "722 276 0091", "phone2": "722 275 6700", "phone3": "800 466 3786", "phone4": "070",
        "note": "Atiende acceso a la información y datos personales en posesión de instituciones públicas del Estado de México."
                "<br>📍 Módulo de Transparencia: Av. Primero de Mayo No. 1731 (esq. Robert Bosch), Planta Baja, "
                "Col. Zona Industrial, C.P. 50071, Toluca, Estado de México."
                "<br>🕘 Atención presencial: lunes a viernes, de 9:00 a 18:00 h."
                "<br>☎️ Línea gratuita 24/7: <b>800 HONESTO</b> (800 466 3786) y marcación rápida <b>070</b>.",
        "url": "http://portal.secogem.gob.mx/transparencia-datos-abiertos"},
    "profedet": {
        "name": "PROFEDET – Procuraduría Federal de la Defensa del Trabajo",
        "phone": "800 717 2942",
        "phone2": "800 555 0199",
        "note": "Asesoría y representación gratuitas en asuntos laborales. WhatsApp 55 1484 8737; correo orientacionprofedet@stps.gob.mx; Atención Ciudadana 079. Sede: Eje 4 Norte No. 311, Col. Santo Tomás, Azcapotzalco, CDMX.",
        "url": "https://www.gob.mx/profedet"},
    "sabg": {
        "name": "Secretaría Anticorrupción y Buen Gobierno (autoridad en datos personales, sector privado)",
        "note": "Ante ella se presenta la solicitud de protección de datos si un particular no atiende tus derechos ARCO (LFPDPPP 2025).",
        "url": "https://www.gob.mx/buengobierno"},
    "ipn_violentometro": {
        "name": "Violentómetro – Unidad Politécnica de Gestión con Perspectiva de Género (IPN)",
        "url": "https://www.ipn.mx/genero/"},
    "ipn_violentometro_laboral": {
        "name": "Violentómetro laboral (IPN)",
        "url": "https://www.ipn.mx/genero/materiales/violentometro-laboral.pdf"},
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
    {"name": "Ley General de Acceso de las Mujeres a una Vida Libre de Violencias",
     "url": "https://www.diputados.gob.mx/LeyesBiblio/pdf/LGAMVLV.pdf"},
    {"name": "Ley de Acceso de las Mujeres a una Vida Libre de Violencia del Estado de México",
     "url": "https://legislacion.edomex.gob.mx/"},
    {"name": "Código Civil del Estado de México (violencia familiar, Arts. 4.396 y ss.)",
     "url": "https://legislacion.edomex.gob.mx/"},
    {"name": "NOM-035-STPS-2018 (factores de riesgo psicosocial y violencia laboral)",
     "url": "https://www.gob.mx/stps"},
    {"name": "Convenio 190 de la OIT sobre la violencia y el acoso (2019)",
     "url": "https://normlex.ilo.org/dyn/nrmlx_es/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C190"},
    {"name": "Ley Federal de Protección de Datos Personales en Posesión de los Particulares (2025)",
     "url": "https://www.diputados.gob.mx/LeyesBiblio/index.htm"},
    {"name": "Ley de Protección de Datos Personales en Posesión de Sujetos Obligados del Estado de México y Municipios (Gaceta del Gobierno, 1-oct-2026)",
     "url": "https://legislacion.edomex.gob.mx/"},
    {"name": "Recomendación sobre la Ética de la Inteligencia Artificial (UNESCO, 2021)",
     "url": "https://unesdoc.unesco.org/ark:/48223/pf0000380455_spa"},
    {"name": "NIST AI Risk Management Framework 1.0 (NIST AI 100-1, 2023)",
     "url": "https://doi.org/10.6028/NIST.AI.100-1"},
    {"name": "Reglamento (UE) 2024/1689 – Ley de IA de la Unión Europea",
     "url": "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"},
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
            ("sexual", 2), ("me toco", 3), ("me tocaron", 3), ("me tocan", 3), ("me toca sin", 4), ("me estan tocando", 4), ("me incomoda", 2), ("mensajes sexuales", 4), ("propuestas sexuales", 4),
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
        "fundamento": "Ley General de Acceso de las Mujeres a una Vida Libre de Violencias; Ley General de Víctimas.",
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
        "fundamento": "Ley General de Acceso de las Mujeres a una Vida Libre de Violencias; Ley General de Víctimas.",
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
            ("ciberacoso", 4), ("ciberbullying", 4), ("acosan en internet", 7), ("acoso en internet", 7), ("acoso en redes", 7), ("me acosan en redes", 7), ("acoso por whatsapp", 6), ("fotos intimas", 4), ("nudes", 3),
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
        "titulo": "Protección de datos personales",
        "emoji": "🔒",
        "boton": "Mis datos personales",
        "relacionados": ["datos_y_derechos_humanos", "caso_datos", "violencia_digital", "ia_derechos_humanos", "privacidad_bot",
                         "acceso_informacion", "transparencia_mexiquense"],
        "keywords": [
            ("datos personales", 6), ("proteccion de datos", 8), ("privacidad", 3), ("aviso de privacidad", 6), ("arco", 3),
            ("derechos arco", 9), ("mi informacion", 2), ("compartieron mis datos", 6), ("difundieron mis datos", 6),
            ("mi curp", 3), ("mi foto", 2), ("transparencia", 3), ("acceso a la informacion", 3),
            ("datos sensibles", 7), ("datos personales sensibles", 8), ("lfpdppp", 8), ("quien tiene mis datos", 7),
            ("me llaman para ofrecerme", 5), ("derecho a la privacidad", 7),
        ],
        "intro": (
            "Tus <b>datos personales</b> son cualquier información que te identifica o te hace identificable (nombre, CURP, domicilio, teléfono, calificaciones, imagen, voz). "
            "Los <b>sensibles</b> afectan tu esfera más íntima o pueden dar pie a discriminación: origen racial o étnico, estado de salud, información genética, creencias, "
            "opiniones políticas y preferencia sexual. El Art. 16 de la Constitución reconoce tu derecho a la protección de tus datos y a los derechos <b>ARCO</b>."
        ),
        "derechos_titulo": "Tus derechos",
        "derechos": [
            "<b>Acceso:</b> saber qué datos tuyos tiene alguien y para qué los usa. <b>Rectificación:</b> corregirlos si son inexactos. "
            "<b>Cancelación:</b> pedir que los eliminen (con las excepciones de la ley). <b>Oposición:</b> negarte a que se usen para ciertos fines.",
            "Conocer el <b>aviso de privacidad</b>: quién recaba tus datos, para qué y cómo ejercer tus derechos.",
            "Para <b>datos sensibles</b>, quien los trata necesita tu <b>consentimiento expreso y por escrito</b> (LFPDPPP Art. 8).",
            "Ejercer ARCO es <b>gratuito</b>; solo pueden cobrarte costos de reproducción o envío (LFPDPPP Art. 34). Ejercer un derecho no te impide ejercer otro (Art. 21).",
            "Plazos (LFPDPPP Art. 31): el responsable debe contestarte en <b>máximo 20 días</b> y, si procede, cumplir en los <b>15 días</b> siguientes; los plazos pueden ampliarse una sola vez por un periodo igual.",
            "<b>Instituciones públicas del Estado de México</b> (gobierno estatal y municipal, organismos autónomos): según la ley estatal vigente (Gaceta del Gobierno, 1-oct-2026), responden en <b>máximo 20 días</b> (ampliables una vez hasta 10) y, si procede, lo hacen efectivo en <b>15 días</b> más (Art. 47). Si no estás conforme, puedes presentar un <b>recurso de revisión</b> dentro de <b>15 días</b> ante <b>Transparencia Mexiquense</b> o ante la Unidad de Transparencia (Art. 88).",
        ],
        "pasos_titulo": "Cómo ejercerlos",
        "pasos": [
            "Presenta tu solicitud <b>por escrito</b> al responsable (la empresa, la escuela o la institución) indicando tus datos, qué derecho ejerces y qué datos te interesan, y <b>conserva el acuse</b>.",
            "Si <b>no responde</b> en el plazo o la respuesta es insuficiente, puedes presentar una <b>solicitud de protección de datos</b> ante la autoridad: dentro de 15 días tras la respuesta, o desde que venció el plazo si no contestó (LFPDPPP Art. 40). Para <b>particulares</b> (empresas, comercios, plataformas) la autoridad es la <b>Secretaría Anticorrupción y Buen Gobierno</b>.",
            "Si el responsable es una <b>institución pública</b> (por ejemplo, la universidad), aplica la ley para <b>sujetos obligados</b> y hay una Unidad de Transparencia; la solicitud debe llevar tu nombre, un medio para recibir notificaciones, un documento que acredite tu identidad y la descripción clara de los datos y del derecho que ejerces (Arts. 45 y 48 de la ley estatal de 2026). La autoridad garante local es <b>Transparencia Mexiquense</b>, que sustituyó al INFOEM.",
            "Si difundieron tus <b>fotos o videos íntimos</b>, no es solo un tema de datos: puede ser el delito de la Ley Olimpia. Consulta el tema de violencia digital y acude al Ministerio Público.",
            "<b>Cuida tus datos:</b> lee los avisos de privacidad, no compartas contraseñas, CURP ni documentos por chats, y pregunta para qué te piden cada dato.",
        ],
        "contactos": ["sabg", "transparencia_mx", "ceavem", "fgjem"],
        "fundamento": "CPEUM Art. 6° y 16; Ley Federal de Protección de Datos Personales en Posesión de los Particulares (nueva ley, DOF 20-03-2025; Arts. 8, 21 a 34 y 40); Ley General de Protección de Datos Personales en Posesión de Sujetos Obligados (2025); Ley de Protección de Datos Personales en Posesión de Sujetos Obligados del Estado de México y Municipios (Gaceta del Gobierno, 1-oct-2026; Arts. 45, 47, 48 y 88).",
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
        "relacionados": ["origen_dh", "lista_dh", "derechos_generales", "derechos_estudiante"],
        "keywords": [
            ("que son los derechos humanos", 12), ("que son los derechos", 8), ("que son derechos humanos", 12),
            ("que significa derechos humanos", 6), ("que son mis derechos", 5),
            ("que es un derecho humano", 6), ("que es derecho humano", 6),
            ("para que sirven los derechos", 6), ("para que sirven los derechos humanos", 6),
            ("importancia de los derechos humanos", 5), ("definicion de derechos humanos", 6),
            ("concepto de derechos humanos", 6),
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
        "fundamento": "CPEUM Arts. 1° y 3°; Ley General de Acceso de las Mujeres a una Vida Libre de Violencias (violencia en el ámbito docente); Legislación Universitaria de la UAEMéx.",
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
            "<b>Violencia digital</b> (Ley General de Acceso de las Mujeres a una Vida Libre de Violencias, Art. 20 Quáter): acción dolosa mediante tecnologías "
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
        "fundamento": "Ley General de Acceso de las Mujeres a una Vida Libre de Violencias (Cap. IV Ter, Arts. 20 Quáter y 20 Quinquies); Código Penal del Estado de México (Arts. 211 Ter y 211 Quater); ficha técnica Ley Olimpia; Módulo 3, Tema 9.",
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
                         "caso_menor", "caso_humillacion", "caso_laboral", "caso_noviazgo", "caso_datos", "caso_ia"],
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
        "fundamento": "Ley General de Acceso de las Mujeres a una Vida Libre de Violencias (hostigamiento y acoso sexual); Ley General de Víctimas; Legislación Universitaria.",
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
        "fundamento": "Ley General de Acceso de las Mujeres a una Vida Libre de Violencias (Art. 20 Quáter); Código Penal del Estado de México (Arts. 211 Ter y 211 Quater).",
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
    # ================================================================== AMPLIACIÓN v3
    # ------------------------------------------------------------------ MUJERES Y VIOLENCIA
    {
        "id": "violencia_mujeres",
        "titulo": "Violencia contra las mujeres: tipos y modalidades",
        "emoji": "💜",
        "boton": "Violencia contra las mujeres",
        "relacionados": ["violentometro", "acoso_hostigamiento", "abuso_laboral", "ley_olimpia", "violencia_pareja_familia", "caso_noviazgo"],
        "keywords": [
            ("violencia contra las mujeres", 9), ("violencia contra la mujer", 9), ("derechos de las mujeres", 8),
            ("derechos de la mujer", 8), ("tipos de violencia", 9), ("modalidades de violencia", 9),
            ("vida libre de violencia", 7), ("violencia psicologica", 6), ("violencia economica", 6),
            ("violencia patrimonial", 6), ("violencia politica", 6), ("violencia feminicida", 7),
            ("feminicidio", 5), ("alerta de genero", 8), ("interposita persona", 8), ("violencia vicaria", 9),
            ("violencia simbolica", 7), ("violencia mediatica", 7), ("violencia acida", 7),
            ("orden de proteccion", 6), ("ordenes de proteccion", 6), ("medidas de proteccion", 5),
            ("violencia institucional", 6), ("violencia en la comunidad", 6), ("mujeres", 2),
        ],
        "intro": (
            "Toda persona tiene derecho a <b>vivir una vida libre de violencias</b>, y el Estado tiene <b>deberes reforzados de protección</b> "
            "con las mujeres, adolescentes y niñas (Art. 4° de la Constitución). Se desarrolla en la <b>Ley General de Acceso de las Mujeres a una Vida Libre de Violencias</b> "
            "y, en el Estado de México, en la <b>Ley de Acceso de las Mujeres a una Vida Libre de Violencia del Estado de México</b>. "
            "Ambas distinguen <b>tipos</b> de violencia (qué es) y <b>modalidades</b> (dónde ocurre)."
        ),
        "derechos_titulo": "Tipos de violencia (Ley General Art. 6; Ley del Edomex Art. 7)",
        "derechos": [
            "<b>Psicológica:</b> cualquier acto u omisión que dañe tu estabilidad psicológica: insultos, humillaciones, devaluación, celotipia, comparaciones destructivas, rechazo, indiferencia, marginación, restricción a tu autodeterminación, amenazas y acecho.",
            "<b>Física:</b> daño no accidental con la fuerza física o con un arma u objeto, con o sin lesiones visibles.",
            "<b>Patrimonial:</b> transformar, sustraer, destruir o retener objetos, documentos personales, bienes, valores o recursos económicos.",
            "<b>Económica:</b> controlar o limitar tus ingresos, o pagarte un salario menor por igual trabajo dentro de un mismo centro laboral.",
            "<b>Sexual:</b> cualquier acto que degrada o daña tu cuerpo o tu sexualidad y atenta contra tu libertad, dignidad e integridad.",
            "<b>A través de interpósita persona</b> (Ley General) o <b>vicaria</b> (Ley del Edomex): usar a tus hijas e hijos, familiares o personas allegadas para dañarte; por ejemplo, amenazar con quitártelos u ocultarlos, usarlos para obtener información tuya o condicionar la pensión alimenticia.",
            "<b>Digital:</b> exponer o difundir imágenes, audios o videos íntimos, reales o simulados, sin tu consentimiento (Ley Olimpia), y otros actos dolosos por medios digitales que dañen tu intimidad o dignidad (Edomex Art. 7 fr. IX).",
            "<b>Simbólica, mediática y ácida o química</b> (Edomex Art. 7): mensajes e imágenes que naturalizan la subordinación o cosifican a las mujeres; y el uso de ácidos u otras sustancias para dañar o desfigurar.",
            "Y <b>cualquier otra forma análoga</b> que lesione tu dignidad, integridad o libertad.",
        ],
        "pasos_titulo": "Modalidades (dónde ocurre) y qué te protege",
        "pasos": [
            "<b>Familiar:</b> en la pareja o la familia, dentro o fuera del domicilio, también con parejas o exparejas (Ley Gral. Art. 7; Edomex Art. 8). El <b>Código Civil del Edomex</b> (Art. 4.396 y ss.) permite demandar por violencia familiar, prevé <b>medidas de protección de oficio</b> y que la patria potestad pueda limitarse a quien ejerce violencia (Art. 4.397 Quater).",
            "<b>Laboral y docente:</b> por quien tiene un vínculo laboral, docente o análogo contigo, sin importar jerarquía; incluye hostigamiento y acoso sexual (Ley Gral. Arts. 10 a 13; Edomex Arts. 9 a 14).",
            "<b>En el noviazgo</b> (Edomex Arts. 20 Ter a 20 Quinquies): ataques sexuales, físicos o psicológicos en una relación de noviazgo, actos sexuales no consentidos y controlar, vigilar o aislarte para humillarte son <b>violencia</b>.",
            "<b>En la comunidad</b> (Ley Gral. Art. 16; Edomex Art. 15): actos que te degradan, discriminan o excluyen en lo público; la ley general incluye el <b>acoso sexual en espacios públicos</b> (Art. 16 Bis).",
            "<b>Institucional:</b> servidoras y servidores públicos que discriminan, dilatan u obstaculizan el ejercicio de tus derechos o tu acceso a la justicia (Ley Gral. Art. 18).",
            "<b>Feminicida:</b> la forma extrema de violencia de género (Art. 21). Existe la <b>Alerta de Violencia de Género</b> para enfrentarla en un territorio.",
            "<b>Órdenes de protección:</b> son actos de <b>urgente aplicación</b>. En el Edomex duran hasta <b>60 días naturales</b>, prorrogables por 30 más o por el tiempo que dure la investigación, y deben expedirse <b>de inmediato o, a más tardar, dentro de las 4 horas</b> siguientes al conocimiento de los hechos (Edomex Art. 29). La autoridad debe informarte con claridad y sin desalentarte (Art. 31).",
            "La ley general pide <b>evitar la mediación o conciliación</b> en casos de violencia familiar, porque no hay igualdad entre la persona agresora y la víctima.",
            "Pregunta por el <b>Centro de Justicia para las Mujeres</b> más cercano: son espacios de atención integral para mujeres víctimas y sus hijas e hijos.",
        ],
        "contactos": ["911", "sin_violencia", "fgjem", "ceavem", "defensoria_uaemex", "codhem"],
        "fundamento": "CPEUM Art. 4°; Ley General de Acceso de las Mujeres a una Vida Libre de Violencias (última reforma DOF 15-01-2026); Ley de Acceso de las Mujeres a una Vida Libre de Violencia del Estado de México (última reforma 09-nov-2026 según el texto proporcionado); Código Civil del Estado de México, Arts. 4.396 a 4.397 Quinquies.",
    },
    # ------------------------------------------------------------------ VIOLENTÓMETRO
    {
        "id": "violentometro",
        "titulo": "El violentómetro",
        "emoji": "📏",
        "boton": "Violentómetro",
        "relacionados": ["violencia_mujeres", "caso_noviazgo", "violencia_pareja_familia", "ley_olimpia"],
        "keywords": [
            ("violentometro", 9), ("que es el violentometro", 10), ("como saber si mi pareja me violenta", 9),
            ("senales de violencia", 6), ("focos rojos", 5), ("banderas rojas", 5), ("red flags", 5),
            ("violencia en el noviazgo", 7), ("noviazgo violento", 7), ("es normal que mi pareja", 7),
            ("mi pareja me revisa el celular", 7), ("mi pareja es celosa", 6), ("mi pareja es celoso", 6),
            ("ley del hielo", 5), ("sextorsion", 3), ("stalkeo", 5),
        ],
        "intro": (
            "El <b>violentómetro</b> es una herramienta en forma de regla creada en 2009 por la <b>Unidad Politécnica de Gestión con Perspectiva de Género del IPN</b> "
            "(a partir de una encuesta a más de 14 mil estudiantes). Sirve para <b>reconocer señales de violencia</b> en una relación, "
            "de las más sutiles a las más graves, antes de que escalen. En 2021 el IPN lo actualizó para incluir violencia digital: "
            "difusión de contenido íntimo sin consentimiento, <i>stalkeo</i> y sextorsión."
        ),
        "derechos_titulo": "Cómo se organiza (con ejemplos)",
        "derechos": [
            "Ordena las conductas <b>de las más sutiles a las más graves</b>, con colores. Según la actualización del IPN de 2021 (reportada por la prensa): <b>verde</b> (celar, “ley del hielo”, mentir, chantajear), <b>amarillo</b> (controlar, manosear, golpear “jugando”), <b>anaranjado</b> (sextorsión) y <b>rojo</b> (abuso sexual, violar, mutilar, asesinar).",
            "La actualización añade conductas <b>digitales</b>, como el <i>stalkeo</i> (vigilar y perseguir en línea), la sextorsión y la difusión de contenido íntimo.",
            "El IPN también publicó un <b>violentómetro laboral</b>. Entre sus conductas aparecen: desacreditar el desempeño, críticas constantes y sin fundamento, exhibir errores en público, gritar, insultar o humillar, negar derechos laborales, despido injustificado, extorsión, propuestas sexuales directas o sutiles, exigir cierta ropa, piropos o comentarios ofensivos, manoseo, discriminación por embarazo, edad, discapacidad o apariencia, impedir la lactancia, hostigamiento y acoso.",
            "<i>Nota:</i> no reproduzco aquí la lista completa y numerada para no cometer errores; la versión oficial está en el sitio del IPN (enlace abajo).",
        ],
        "pasos_titulo": "Cómo usarlo",
        "pasos": [
            "Revisa tu relación (pareja, amistad, familia, escuela): ¿reconoces alguna conducta? <b>Ninguna señal es “normal” ni “parte del amor”.</b>",
            "La violencia suele <b>escalar con el tiempo</b>. Si ya hay conductas del nivel amarillo o más, no esperes a que pase a algo peor.",
            "Cuéntalo a alguien de confianza y <b>guarda evidencia</b> (mensajes, capturas, fechas).",
            "Si estás en el nivel rojo o sientes riesgo para tu vida, <b>llama al 911</b>. También puedes llamar a la Línea Sin Violencia o acudir al Ministerio Público.",
            "Si te reconoces en las conductas de la lista, también puedes pedir ayuda para cambiar: <b>Hombre a Hombre</b> orienta a hombres que desean cambiar conductas violentas.",
            "El violentómetro es <b>orientativo</b>: no es un diagnóstico ni sustituye la valoración de profesionales.",
        ],
        "contactos": ["ipn_violentometro", "ipn_violentometro_laboral", "sin_violencia", "911", "fgjem", "hombre_a_hombre", "uaemex_psico"],
        "fundamento": "Violentómetro del IPN (Unidad Politécnica de Gestión con Perspectiva de Género, 2009; actualización de 2021 según prensa) y Violentómetro laboral del IPN; Ley General de Acceso de las Mujeres a una Vida Libre de Violencias, Art. 6; Ley del Edomex, Arts. 20 Ter a 20 Quinquies (violencia en el noviazgo).",
    },
    # ------------------------------------------------------------------ ABUSO LABORAL
    {
        "id": "abuso_laboral",
        "titulo": "Abuso y violencia en el trabajo",
        "emoji": "💼",
        "boton": "Abuso laboral",
        "relacionados": ["acoso_hostigamiento", "violencia_mujeres", "caso_laboral", "donde_ayuda"],
        "keywords": [
            ("abuso laboral", 9), ("acoso laboral", 9), ("hostigamiento laboral", 9), ("violencia laboral", 9),
            ("mobbing", 8), ("derechos laborales", 8), ("derechos del trabajador", 8), ("derechos de los trabajadores", 8),
            ("explotacion laboral", 7), ("trabajo digno", 5), ("mi jefe", 3), ("mi jefa", 3), ("mi patron", 3), ("mi jefe me", 2), ("mi jefa me", 2), ("jefe me grita", 4), ("jefa me grita", 4), ("jefe me humilla", 4), ("jefa me humilla", 4), ("jefe me insulta", 4), ("jefe me amenaza", 4), ("jefe me maltrata", 4), ("mi patron me", 2), ("mi patrona me", 2),
            ("en mi trabajo", 3), ("practicas profesionales", 4), ("servicio social", 3), ("no me pagan", 5),
            ("me despidieron", 4), ("despido injustificado", 6), ("horas extra", 3), ("me obligan a renunciar", 6),
            ("salario", 2), ("profedet", 6), ("nom 035", 8), ("riesgo psicosocial", 8), ("convenio 190", 9),
        ],
        "intro": (
            "El <b>abuso laboral</b> es cualquier conducta abusiva en el trabajo que daña tu dignidad, salud, libertad o seguridad: "
            "humillaciones, amenazas, explotación, discriminación, acoso u hostigamiento. El Art. 123 de la Constitución reconoce que "
            "<b>toda persona tiene derecho al trabajo digno y socialmente útil</b>. A nivel internacional, el <b>Convenio 190 de la OIT</b> (ratificado por México en 2022 y en vigor desde 2023) reconoce el derecho de toda persona "
            "a <b>un mundo del trabajo libre de violencia y acoso</b> (Art. 4)."
        ),
        "derechos_titulo": "Qué se considera violencia en el trabajo",
        "derechos": [
            "<b>Definición internacional (C190, Art. 1):</b> comportamientos y prácticas inaceptables, o amenazas de ellos, <b>una sola vez o de manera repetida</b>, que causen o puedan causar daño físico, psicológico, sexual o económico, incluida la violencia y el acoso por razón de género.",
            "<b>Violencia laboral</b> (Ley General de Acceso de las Mujeres, Arts. 10 y 11): la ejerce quien tiene un vínculo laboral, docente o análogo contigo, <b>aunque no sea tu jefe</b>; puede ser un solo hecho o una serie cuya suma produce el daño. Ejemplos: negarte ilegalmente la contratación o el respeto a tu permanencia o condiciones de trabajo, descalificar tu trabajo, amenazas, intimidación, humillaciones, explotación, impedir la lactancia y toda discriminación por género.",
            "<b>En el Edomex</b> (Art. 10 de la ley estatal), además: exigir <b>pruebas de embarazo</b> para contratarte o conservar tu empleo, imponer requisitos sexistas en la forma de vestir y excluirte de cargos por razón de género.",
            "<b>Violencia económica:</b> pagarte menos que a otra persona por igual trabajo en el mismo centro laboral.",
            "<b>Hostigamiento sexual:</b> abuso de poder en una relación de <b>subordinación</b> (laboral o escolar), con conductas de connotación lasciva. <b>Acoso sexual:</b> no hay subordinación, pero sí abuso de poder que te deja en indefensión o riesgo; puede ocurrir en uno o varios eventos.",
            "<b>NOM-035-STPS-2018:</b> define la violencia laboral como actos de <b>hostigamiento, acoso o malos tratos</b> contra el trabajador que pueden dañar su integridad o salud, y obliga al patrón a tener una <b>política de prevención</b> por escrito, <b>mecanismos para presentar quejas</b> y a informarte de ellos (numerales 4.12, 5.1 y 5.7).",
            "<b>Los centros de trabajo y las escuelas</b> deben tener procedimientos claros para sancionar el hostigamiento y el acoso sexual, <b>no hacer público tu nombre</b>, darte atención psicológica y legal gratuita y sancionar a superiores que no den curso a una queja (Edomex Art. 14).",
            "Estas leyes de género protegen a las mujeres; <b>todas las personas</b> están protegidas por la Constitución, la Ley Federal del Trabajo y el Convenio 190.",
        ],
        "pasos_titulo": "Qué puedes hacer",
        "pasos": [
            "<b>Documenta:</b> fechas, qué se dijo o hizo, testigos, mensajes, correos, contrato, recibos de pago y horarios.",
            "<b>No renuncies ni firmes</b> finiquitos o documentos bajo presión sin entender qué dicen y sin asesoría.",
            "Usa los <b>canales internos</b> (recursos humanos, protocolo o comité) <b>por escrito</b> y conserva el acuse. Pide que te informen el <b>mecanismo de quejas</b> de la NOM-035.",
            "Pide <b>orientación gratuita</b> a la PROFEDET (defensa del trabajo). Si la conducta viene de una autoridad o servidor público, consulta a la CODHEM. Si hay un delito (acoso sexual, amenazas, lesiones), acude al Ministerio Público.",
            "El C190 pide protección frente a <b>represalias</b> para quien denuncia y la posibilidad de alejarte de una situación de peligro grave e inminente sin sufrir consecuencias indebidas (Art. 10). <b>Guarda constancia</b> si crees que te están castigando por quejarte.",
            "<b>Prácticas profesionales, servicio social o becas:</b> ser practicante no te quita tus derechos humanos. Avisa también a la Facultad (coordinación o Defensoría) para que te oriente.",
        ],
        "contactos": ["profedet", "ipn_violentometro_laboral", "codhem", "fgjem", "sin_violencia", "defensoria_uaemex", "911"],
        "fundamento": "CPEUM Art. 123; Convenio 190 de la OIT (Arts. 1, 4 y 10); NOM-035-STPS-2018 (DOF 23-oct-2018); Ley General de Acceso de las Mujeres a una Vida Libre de Violencias (Arts. 6, 10, 11 y 13); Ley de Acceso de las Mujeres a una Vida Libre de Violencia del Edomex (Arts. 9 a 14).",
    },
    # ------------------------------------------------------------------ PERSONA VS ANIMAL
    {
        "id": "persona_vs_animal",
        "titulo": "Derechos de una persona y protección de los animales",
        "emoji": "🐾",
        "boton": "Personas y animales",
        "relacionados": ["que_son_dh", "lista_dh", "estudiante_vs_ciudadano"],
        "keywords": [
            ("mismos que los de un animal", 13), ("mismos derechos que un animal", 13), ("mismos que un animal", 12), ("mismos derechos que los animales", 13), ("los de un animal", 10), ("derechos que un animal", 10), ("igual que un animal", 9), ("derechos de una persona", 9), ("derechos de un animal", 9), ("derechos de los animales", 9),
            ("derechos de las personas y los animales", 10), ("personas y animales", 9), ("persona y un animal", 9),
            ("persona y animal", 8), ("diferencia entre una persona y un animal", 10),
            ("derechos humanos y derechos de los animales", 12), ("derechos humanos y animales", 11),
            ("derechos humanos y los animales", 11), ("diferencia entre derechos humanos y derechos de los animales", 14),
            ("derechos humanos y derechos animales", 12), ("derechos animales", 8), ("bienestar animal", 8),
            ("protección animal", 7), ("proteccion animal", 7),
            ("maltrato animal", 8), ("mascota", 5), ("animales", 4), ("animal", 4),
        ],
        "intro": (
            "<b>No son los mismos, aunque se relacionan.</b> Los <b>derechos humanos</b> pertenecen a las <b>personas</b> por su dignidad; los <b>animales</b> están <b>protegidos por la Constitución</b> mediante la prohibición de su maltrato y "
            "<b>deberes de cuidado</b> que recaen en las personas y en el Estado. La Declaración Universal habla de “todos los seres humanos” y de “toda persona”, y <b>no menciona a los animales</b>. "
            "En México, la Constitución prohíbe el maltrato animal y habla de “protección”, no de “derechos humanos de los animales”."
            "<table class='mt-3 text-xs border-collapse w-full'>"
            "<tr class='bg-emerald-50'><th class='border border-slate-300 p-1 text-left'>Aspecto</th><th class='border border-slate-300 p-1 text-left'>Derechos humanos (personas)</th><th class='border border-slate-300 p-1 text-left'>Protección de los animales</th></tr>"
            "<tr><td class='border border-slate-300 p-1 align-top font-semibold'>Fundamento</td><td class='border border-slate-300 p-1 align-top'><b>Dignidad</b> de la persona (DUDH Arts. 1 y 2; CPEUM Art. 1°)</td><td class='border border-slate-300 p-1 align-top'>La <b>prohibición del maltrato</b> y el deber del Estado de garantizar su protección, trato adecuado, conservación y cuidado (CPEUM Art. 4°, párrafo sexto)</td></tr>"
            "<tr><td class='border border-slate-300 p-1 align-top font-semibold'>Quién es titular</td><td class='border border-slate-300 p-1 align-top'>Toda persona: puede <b>tener y ejercer</b> derechos y asumir obligaciones (personalidad jurídica, DUDH Art. 6)</td><td class='border border-slate-300 p-1 align-top'>El animal es <b>objeto de protección</b>; no ejerce derechos por sí mismo ni tiene obligaciones. Quien responde es la persona responsable</td></tr>"
            "<tr><td class='border border-slate-300 p-1 align-top font-semibold'>Norma principal</td><td class='border border-slate-300 p-1 align-top'>Constitución, tratados internacionales y Declaración Universal</td><td class='border border-slate-300 p-1 align-top'>Art. 4° constitucional (párrafo sexto), en los términos que señalen las leyes</td></tr>"
            "<tr><td class='border border-slate-300 p-1 align-top font-semibold'>Quién puede exigirlo</td><td class='border border-slate-300 p-1 align-top'>La propia persona, con acceso a recurso efectivo (DUDH Art. 8) y a las instituciones de derechos humanos</td><td class='border border-slate-300 p-1 align-top'>Las personas y las autoridades, mediante denuncia, sanciones administrativas o penales</td></tr>"
            "<tr><td class='border border-slate-300 p-1 align-top font-semibold'>Si se vulnera</td><td class='border border-slate-300 p-1 align-top'>Queja ante la CODHEM o la CNDH, amparo, reparación del daño</td><td class='border border-slate-300 p-1 align-top'>Denuncia por maltrato ante la autoridad local; sanciones previstas por la ley aplicable</td></tr>"
            "</table>"
        ),
        "derechos_titulo": "Derechos humanos: para las personas",
        "derechos": [
            "<b>Dignidad e igualdad:</b> “todos los seres humanos nacen libres e iguales en dignidad y derechos”, dotados de razón y conciencia (DUDH, Art. 1). Los tienen sin distinción de raza, sexo, idioma, religión, origen o condición (DUDH, Art. 2).",
            "<b>Reconocimiento como persona ante la ley</b> (DUDH, Art. 6), igualdad ante la ley (Art. 7) y <b>recurso efectivo</b> ante los tribunales contra actos que violen sus derechos (Art. 8).",
            "<b>En México (CPEUM, Art. 1°):</b> todas las personas gozan de los derechos humanos reconocidos en la Constitución y en los tratados internacionales, y está prohibida la discriminación. Las autoridades deben promover, respetar, proteger y garantizar esos derechos.",
            "<b>Derechos y deberes:</b> la persona también tiene deberes hacia la comunidad, y sus derechos solo pueden limitarse por ley para proteger los derechos de los demás, el orden público y el bienestar general (DUDH, Art. 29). El animal no tiene deberes jurídicos.",
            "En el Código Civil del Estado de México, la <b>persona física</b> tiene <b>capacidad de goce y de ejercicio</b> (Art. 2.1; los menores o incapaces actúan por medio de representantes, Art. 2.2) y <b>derechos de la personalidad</b> (honor, vida privada, imagen, integridad) que son inalienables, imprescriptibles e irrenunciables (Arts. 2.4 y 2.5).",
        ],
        "pasos_titulo": "Animales: protección y deberes de cuidado",
        "pasos": [
            "<b>Constitución, Art. 4° (párrafo sexto, adición del 2-dic-2024):</b> queda prohibido el maltrato a los animales y el Estado debe garantizar su protección, trato adecuado, conservación y cuidado, “en los términos que señalen las leyes”. El Art. 73 (fracc. XXIX-G) permite una ley que reparta las competencias de la Federación, los estados y los municipios en protección y bienestar animal, y el Art. 3° incluye la protección de los animales en los contenidos educativos.",
            "<b>Diferencia clave:</b> los derechos humanos se fundan en la <i>dignidad de la persona</i> y las personas los ejercen y los exigen; la protección animal se fundamenta en la <i>prohibición constitucional del maltrato</i> y se exige mediante los <i>deberes</i> de cuidado de personas y autoridades.",
            "<b>Lo que comparten:</b> ambos están protegidos contra el maltrato y la crueldad, y el medio ambiente sano es un derecho humano (Art. 4°) que se relaciona con la conservación de la fauna.",
            "<i>Matiz:</i> que los animales sean “sujetos de derechos” es un debate doctrinal; el texto constitucional habla de protección, trato adecuado y cuidado, no de derechos humanos. Cuando una actividad humana choca con la protección animal, la Constitución remite a “los términos que señalen las leyes” y la solución depende de la ley aplicable y de las autoridades competentes.",
        ],
        "contactos": ["codhem", "cndh"],
        "fundamento": "CPEUM Arts. 1°, 3°, 4° (párrafo sexto, DOF 02-12-2024) y 73 fracc. XXIX-G, con el Decreto de 2-dic-2024 (transitorio segundo); Declaración Universal de los Derechos Humanos (ONU, 1948), Arts. 1, 2, 6, 7, 8 y 29; Código Civil del Estado de México (Arts. 2.1, 2.2, 2.4 y 2.5, sobre las personas; última reforma 16-jun-2026).",
    },
    # ------------------------------------------------------------------ IA Y DERECHOS HUMANOS (Unidades 4 y 5)
    {
        "id": "ia_derechos_humanos",
        "titulo": "Inteligencia artificial y derechos humanos",
        "emoji": "🤖",
        "boton": "IA y derechos humanos",
        "relacionados": ["ia_plan_nacional", "ia_chapultepec", "ia_requisitos", "ia_detectar_vulneracion", "ia_sesgos", "ia_libertad_expresion", "ia_responsabilidad", "ia_unesco", "datos_y_derechos_humanos", "ia_eeuu_vs_ue", "caso_ia"],
        "keywords": [
            ("ia y derechos humanos", 9), ("derechos humanos y la ia", 9), ("derechos humanos e inteligencia artificial", 9),
            ("derechos humanos y la inteligencia artificial", 9), ("inteligencia artificial", 4), ("chatgpt", 4),
            ("algoritmo", 3), ("sesgo algoritmico", 5), ("sesgos algoritmicos", 5), ("reconocimiento facial", 4),
            ("deepfake", 4), ("contenido generado por ia", 6), ("ia generativa", 5), ("unesco", 3),
            ("principios de chapultepec", 9), ("chapultepec", 6), ("ia$", 3), ("discriminacion algoritmica", 6),
        ],
        "intro": (
            "La <b>inteligencia artificial (IA)</b> puede ampliar derechos, pero también vulnerarlos cuando decide o influye en algo importante para ti "
            "(becas, admisión, empleo, vigilancia) sin controles. La declaración de ética de IA de México, los <b>Principios de Chapultepec</b> "
            "(Secihti y ATDT, 29 de enero de 2026), lo resume así: <b>la IA debe ampliar derechos, nunca reducirlos</b>."
        ),
        "derechos_titulo": "Derechos que puede afectar",
        "derechos": [
            "<b>Privacidad y datos personales</b> (Arts. 6° y 16): la IA se construye con datos; hay que cuidar su calidad, representatividad, seguridad y el respeto a la privacidad.",
            "<b>No discriminación y sesgos algorítmicos</b> (Art. 1°): si los datos o criterios reproducen desigualdades de género, origen étnico, condición social o discapacidad, "
            "el sistema puede excluir; por eso se debe revisar de forma continua y corregir.",
            "<b>Libertad de expresión e información:</b> los contenidos generados por IA pueden engañar o desinformar; se debe evitar su uso deliberado para ello. "
            "La UE exige marcar el contenido sintético (AI Act, Art. 50), y si es íntimo sexual puede entrar en la Ley Olimpia (contenido “simulado”).",
            "<b>Explicación y transparencia:</b> “si una decisión no puede explicarse, no debe automatizarse”: las personas deben poder saber cuándo una decisión fue apoyada por un sistema automatizado y entender cómo se llegó a ella.",
            "<b>Rendición de cuentas:</b> toda decisión apoyada por IA debe tener <b>responsables humanos</b>; no queda “en manos de la máquina”.",
            "<b>Diversidad cultural y lingüística:</b> la IA no puede ser ajena a las lenguas y culturas del país.",
        ],
        "pasos_titulo": "Dónde está regulado y qué puedes hacer",
        "pasos": [
            "<b>Principios éticos internacionales:</b> la Recomendación de la UNESCO sobre la ética de la IA, los principios de la OCDE y el modelo de la Unión Europea.",
            "<b>México:</b> los Principios de Chapultepec son <b>orientadores, no vinculantes</b>. Hasta donde se pudo verificar (nov. 2026) no hay una ley general de IA; "
            "se aplican normas generales: Constitución, leyes de datos personales de 2025, Ley General de Acceso de las Mujeres a una Vida Libre de Violencias y Ley Olimpia, entre otras. Verifica si hubo reformas recientes.",
            "Si una decisión automatizada te perjudica: pide <b>por escrito</b> información sobre el sistema, los datos usados y los criterios, y que <b>una persona</b> revise tu caso.",
            "Ejerce tus derechos <b>ARCO</b> para saber qué datos tuyos se usaron. Si crees que hubo discriminación, acude a la Defensoría universitaria o a la CODHEM.",
            "<i>Transparencia:</i> este asistente opera con una <b>arquitectura híbrida</b>: prioriza fichas normativas verificadas por reglas locales y, solo ante preguntas abiertas, utiliza recuperación local (Mini-RAG) junto con modelos de lenguaje vía <b>Groq</b> etiquetando explícitamente la respuesta.",
        ],
        "contactos": ["codhem", "defensoria_uaemex", "sabg"],
        "fundamento": "CPEUM Arts. 1°, 6° y 16; Principios de Chapultepec (Secihti-ATDT, 29-ene-2026); Recomendación de la UNESCO sobre la ética de la IA; Programa de Normatividad de la IA, Unidad 4 (4.1).",
    },
    {
        "id": "ia_requisitos",
        "titulo": "¿Qué debe cumplir un sistema de IA para no vulnerar derechos humanos?",
        "emoji": "✅",
        "boton": "Requisitos de una IA responsable",
        "relacionados": ["ia_detectar_vulneracion", "ia_alto_riesgo", "ia_unesco", "ia_nist_rmf", "ia_cumplimiento", "ia_eeuu_vs_ue"],
        "keywords": [
            ("sistemas de ia que deben cumplir", 10), ("que deben cumplir los sistemas de ia", 10),
            ("que debe cumplir un sistema de ia", 10), ("que debe cumplir una ia", 10), ("para no vulnerar derechos humanos", 8),
            ("no vulnerar derechos", 6), ("vulnerar derechos humanos", 6), ("requisitos de la ia", 8),
            ("requisitos de los sistemas de ia", 9), ("requisitos de un sistema de ia", 9), ("ia confiable", 7), ("ia etica", 6),
            ("ia responsable", 5), ("como debe ser una ia", 7), ("principios eticos de la ia", 8),
            ("que deben seguir los modelos de ia", 14), ("que deben seguir los sistemas de ia", 14), ("que debe seguir una ia", 13), ("que deben cumplir los modelos de ia", 14),
            ("que deben respetar los modelos de ia", 14), ("que deben respetar los sistemas de ia", 14), ("modelos de ia para no vulnerar", 13), ("modelos de ia", 6),
            ("para no vulnerar los derechos", 10), ("no vulnerar los derechos humanos", 9), ("como evitar que la ia vulnere", 11), ("reglas para la ia", 8), ("normas que debe seguir la ia", 11),
        ],
        "intro": (
            "No existe una lista universal única, pero los marcos principales (el <b>Reglamento de IA de la Unión Europea</b>, los "
            "<b>Principios de Chapultepec</b> de México y los principios éticos de UNESCO y OCDE) coinciden en estos requisitos. "
            "Son la base de lo que revisas en las Unidades 4 y 5 de tu materia."
        ),
        "derechos_titulo": "Requisitos (resumen)",
        "derechos": [
            "<b>Gestión de riesgos</b> durante todo el ciclo de vida del sistema (AI Act, Art. 9).",
            "<b>Datos de calidad y sin sesgos:</b> gobernanza de datos y conjuntos de entrenamiento, validación y prueba pertinentes y representativos (Art. 10).",
            "<b>Documentación técnica y registro de eventos</b> para poder reconstruir cómo se produjo una decisión (Arts. 11 y 12).",
            "<b>Transparencia:</b> informar cuándo interactúas con una IA y marcar el contenido sintético (Art. 50); dar instrucciones claras a quien la usa (Art. 13).",
            "<b>Supervisión humana efectiva</b>, para prevenir o reducir riesgos a la salud, la seguridad o los derechos fundamentales (Art. 14).",
            "<b>Precisión, solidez y ciberseguridad</b> (Art. 15).",
            "<b>Evaluación de impacto en derechos fundamentales</b> antes de desplegar ciertos sistemas de alto riesgo, cuando los usan organismos públicos o entidades que prestan servicios públicos (Art. 27). "
            "Coincide con el principio mexicano: “antes de automatizar, hay que comprender a quién y a qué afecta”.",
            "<b>Derecho a explicación</b> de decisiones individuales apoyadas en sistemas de alto riesgo (Art. 86) y vías para reclamar.",
            "<b>Según la UNESCO (2021):</b> proporcionalidad (no usar IA si no es necesaria ni proporcional), no usarla para calificación social ni vigilancia masiva, decisión humana final en casos irreversibles o de vida o muerte, recurso efectivo contra la discriminación y responsabilidad siempre atribuible a personas (párrs. 26, 29 y 68).",
            "<b>Según el NIST (2023):</b> el sistema debe ser válido y fiable, seguro, protegido y resiliente, responsable y transparente, explicable e interpretable, con privacidad mejorada y justo con los sesgos nocivos gestionados.",
            "<b>Cero prácticas prohibidas</b> (Art. 5): manipulación subliminal o engañosa; explotar vulnerabilidades por edad, discapacidad o situación económica; puntuación social injustificada; "
            "predecir delitos solo por el perfil de una persona; crear bases faciales con extracción masiva de imágenes; inferir emociones en escuelas y trabajos; "
            "categorizar por biometría para deducir raza, opiniones políticas, religión u orientación sexual.",
        ],
        "pasos_titulo": "Qué implica para ti como ingeniero/a",
        "pasos": [
            "Documenta tus datos, decisiones de diseño y límites del sistema; prueba el modelo con grupos distintos para detectar sesgos.",
            "Diseña para que <b>una persona pueda revisar, corregir y detener</b> al sistema, y avisa a las personas usuarias que hay IA.",
            "Evalúa el impacto <b>antes</b> de desplegar y audita después (ver el tema de cumplimiento, Unidad 5).",
            "En la UE las sanciones por prácticas prohibidas llegan a <b>35 millones de euros o el 7 % del volumen de negocio mundial</b>; por otras infracciones, hasta 15 millones o el 3 % (Art. 99).",
            "Calendario: el Reglamento (UE) 2026/1744 (Digital Omnibus), publicado el 24-jul-2026, aplazó las obligaciones de alto riesgo del Anexo III al 2 de diciembre de 2027 y las del Anexo I al 2 de agosto de 2028.",
        ],
        "contactos": [],
        "fundamento": "Reglamento (UE) 2024/1689 (Arts. 5, 9 a 15, 27, 50, 86 y 99; texto DO 12-07-2024); Recomendación de la UNESCO sobre la ética de la IA (2021, párrs. 26, 29 y 68); NIST AI RMF 1.0 (2023, sección 3); Principios de Chapultepec; Programa de Normatividad de la IA, Unidades 4 y 5.",
    },
    {
        "id": "ia_alto_riesgo",
        "titulo": "IA de alto riesgo y prácticas prohibidas",
        "emoji": "🚦",
        "boton": "IA de alto riesgo",
        "relacionados": ["ia_requisitos", "ia_salud_finanzas", "ia_seguridad_educacion_empleo", "ia_generativa", "ia_vehiculos_robots", "ue_ai_act", "caso_ia"],
        "keywords": [
            ("ia de alto riesgo", 9), ("sistemas de alto riesgo", 9), ("algoritmos de alto riesgo", 9), ("alto riesgo", 5),
            ("practicas prohibidas", 8), ("ia prohibida", 8), ("ia en la educacion", 8), ("ia en educacion", 8),
            ("ia en el trabajo", 7), ("ia y empleo", 8), ("ia en educacion y empleo", 9), ("ia en seguridad publica", 8),
            ("vigilancia con ia", 7), ("puntuacion social", 7), ("social scoring", 7), ("emociones en la escuela", 6),
            ("ia en salud", 6), ("ia en el sector financiero", 7), ("scoring crediticio", 7),
        ],
        "intro": (
            "El <b>Reglamento de IA de la UE</b> clasifica la IA por <b>nivel de riesgo</b>: prácticas <b>prohibidas</b>, sistemas de <b>alto riesgo</b>, obligaciones de <b>transparencia</b> y riesgo mínimo. "
            "Los sistemas del <b>Anexo III</b> son los que más pueden afectar derechos."
        ),
        "derechos_titulo": "Alto riesgo (Anexo III): ejemplos",
        "derechos": [
            "<b>Educación y formación:</b> decidir el acceso o la admisión a centros educativos; evaluar resultados de aprendizaje; evaluar el nivel educativo al que podrás acceder; vigilar conductas prohibidas durante exámenes.",
            "<b>Empleo:</b> selección y contratación (filtrar solicitudes, evaluar candidatos); decisiones sobre condiciones, promoción o rescisión; asignar tareas según comportamiento o rasgos personales; supervisar y evaluar el rendimiento.",
            "<b>Servicios esenciales:</b> evaluar solvencia o calificación crediticia (fintech), prestaciones públicas y algunos seguros.",
            "También: biometría, infraestructuras críticas, aplicación de la ley, migración y fronteras, y administración de justicia.",
            "Su despliegue exige los requisitos del tema anterior: gestión de riesgos, datos sin sesgos, supervisión humana, transparencia y, en ciertos casos, evaluación de impacto en derechos fundamentales.",
        ],
        "pasos_titulo": "Prácticas prohibidas y otros casos críticos",
        "pasos": [
            "<b>Prohibido:</b> inferir emociones de personas en <b>centros educativos y lugares de trabajo</b> (salvo por razones médicas o de seguridad), puntuación social injustificada, manipulación, explotar vulnerabilidades y predecir delitos solo por el perfil (Art. 5).",
            "<b>Seguridad pública y vigilancia:</b> la identificación biométrica remota “en tiempo real” en espacios públicos con fines policiales está prohibida salvo excepciones estrictas (búsqueda de víctimas o desaparecidos, amenazas graves, delitos graves) y con autorización previa (Art. 5).",
            "<b>IA generativa:</b> debe avisar que interactúas con una IA y marcar el contenido sintético (audio, imagen, video o texto) para poder detectar deepfakes (Art. 50).",
            "<b>Reconocimiento de emociones y categorización biométrica</b> (cuando están permitidos): se debe informar a las personas expuestas (Art. 50).",
            "Aplicación en el tiempo: las obligaciones de alto riesgo del Anexo III se aplazaron al 2 de diciembre de 2027 y las del Anexo I al 2 de agosto de 2028 (Reglamento (UE) 2026/1744, publicado el 24-jul-2026).",
        ],
        "fundamento": "Reglamento (UE) 2024/1689 (Art. 5, Art. 6 y Anexo III, Art. 50); Programa de Normatividad de la IA, Unidad 4 (4.3 y 4.4).",
    },
    {
        "id": "ia_eeuu_vs_ue",
        "titulo": "Estados Unidos vs. Unión Europea: derechos humanos y tecnología",
        "emoji": "🌍",
        "boton": "EE. UU. vs. Unión Europea",
        "relacionados": ["ue_ai_act", "ue_modelo_rgpd", "eeuu_blueprint", "ia_nist_rmf", "ocde_gpai", "latam_ia"],
        "keywords": [
            ("estados unidos y union europea", 10), ("estados unidos y la union europea", 10),
            ("diferencia entre estados unidos", 10), ("ue y eeuu", 9), ("eeuu y ue", 9), ("europa y estados unidos", 9),
            ("estados unidos vs", 8), ("union europea vs", 8), ("estados unidos contra", 7), ("ai bill of rights", 8),
            ("carta de derechos de la ia", 8), ("blueprint", 6), ("nist", 5), ("modelo europeo", 6),
            ("modelo estadounidense", 6), ("comparar europa", 10), ("europa con eeuu", 10), ("europa con estados unidos", 10), ("eeuu", 5), ("europa", 4), ("estados unidos", 6), ("union europea", 6), ("comparativa", 4), ("ee uu", 5), ("regulacion de la ia en europa", 7), ("regulacion de la ia en estados unidos", 7),
        ],
        "intro": (
            "Ambos buscan una IA confiable, pero con <b>modelos distintos</b>: la UE <b>legisla de forma amplia y obligatoria</b> con enfoque en derechos fundamentales; "
            "EE. UU. combina <b>guías voluntarias, reglas sectoriales y leyes estatales</b>, con más peso en la innovación."
            "<table class='mt-3 text-xs border-collapse w-full'>"
            "<tr class='bg-emerald-50'><th class='border border-slate-300 p-1 text-left'>Aspecto</th><th class='border border-slate-300 p-1 text-left'>Unión Europea</th><th class='border border-slate-300 p-1 text-left'>Estados Unidos</th></tr>"
            "<tr><td class='border border-slate-300 p-1 align-top font-semibold'>Naturaleza</td><td class='border border-slate-300 p-1 align-top'>Ley horizontal <b>vinculante</b> (Reglamento 2024/1689)</td><td class='border border-slate-300 p-1 align-top'>Sin ley federal general; guías <b>voluntarias</b> y reglas por sector y por estado</td></tr>"
            "<tr><td class='border border-slate-300 p-1 align-top font-semibold'>Enfoque</td><td class='border border-slate-300 p-1 align-top'>Por <b>riesgo</b>: prohibido, alto riesgo, transparencia</td><td class='border border-slate-300 p-1 align-top'>Gestión de riesgos y principios; innovación y mercado</td></tr>"
            "<tr><td class='border border-slate-300 p-1 align-top font-semibold'>Derechos de las personas</td><td class='border border-slate-300 p-1 align-top'>Derecho a explicación (Art. 86); evaluación de impacto en derechos fundamentales (Art. 27)</td><td class='border border-slate-300 p-1 align-top'>Principios no vinculantes (Blueprint for an AI Bill of Rights, 2022)</td></tr>"
            "<tr><td class='border border-slate-300 p-1 align-top font-semibold'>Sanciones</td><td class='border border-slate-300 p-1 align-top'>Hasta 35 M€ o 7 % del volumen de negocio mundial</td><td class='border border-slate-300 p-1 align-top'>Depende de la ley sectorial o estatal aplicable</td></tr>"
            "<tr><td class='border border-slate-300 p-1 align-top font-semibold'>Datos personales</td><td class='border border-slate-300 p-1 align-top'>RGPD, ley general europea</td><td class='border border-slate-300 p-1 align-top'>Leyes sectoriales y estatales (sin ley federal general)</td></tr>"
            "<tr><td class='border border-slate-300 p-1 align-top font-semibold'>Gestión de riesgos</td><td class='border border-slate-300 p-1 align-top'>Obligatoria para IA de alto riesgo (Art. 9)</td><td class='border border-slate-300 p-1 align-top'>Marco <b>voluntario</b> NIST AI RMF: gobernar, mapear, medir y gestionar</td></tr>"
            "</table>"
        ),
        "derechos_titulo": "Unión Europea",
        "derechos": [
            "<b>Reglamento (UE) 2024/1689 (AI Act):</b> prohíbe prácticas incompatibles con los derechos fundamentales y exige requisitos estrictos a la IA de alto riesgo.",
            "Se complementa con el <b>RGPD</b> (datos personales) y con la <b>Ley de Servicios Digitales</b> y la <b>Ley de Mercados Digitales</b>.",
            "Aplicación escalonada: prohibiciones desde el 2 de febrero de 2025. En 2026 la UE aprobó el <b>Digital Omnibus</b> (Reglamento (UE) 2026/1744, publicado el 24-jul-2026), que aplazó las obligaciones de alto riesgo del Anexo III al 2 de diciembre de 2027 y las del Anexo I al 2 de agosto de 2028.",
        ],
        "pasos_titulo": "Estados Unidos",
        "pasos": [
            "Hasta donde se pudo verificar (nov. 2026), <b>no hay una ley federal general de IA</b>.",
            "<b>Blueprint for an AI Bill of Rights</b> (Oficina de Política Científica y Tecnológica, 2022): cinco principios <b>no vinculantes</b>: sistemas seguros y efectivos; protección contra la discriminación algorítmica; privacidad de datos; aviso y explicación; y alternativas humanas con respaldo.",
            "<b>NIST AI Risk Management Framework</b> (enero de 2023): marco <b>voluntario</b>, que busca preservar derechos, no sectorial y válido para cualquier caso de uso. Propone cuatro funciones (gobernar, mapear, medir y gestionar) y siete características de una IA confiable. No fija el nivel de riesgo aceptable ni sustituye la ley.",
            "La orden ejecutiva de 2023 sobre IA fue revocada en enero de 2025. En diciembre de 2025 otra orden ejecutiva buscó limitar las leyes estatales de IA, y estados como California, Texas y Colorado han aprobado reglas propias (según fuentes consultadas; verifica su estado).",
            "En la práctica se aplican leyes ya existentes (consumo, antidiscriminación, privacidad sectorial).",
            "<b>Punto de encuentro:</b> la Recomendación de la UNESCO (2021) funciona como referencia mundial voluntaria y coincide con ambos modelos en privacidad, no discriminación, supervisión humana, transparencia y rendición de cuentas.",
            "<b>Para México:</b> los Principios de Chapultepec se parecen más al enfoque de derechos de la UE, pero son orientadores, no vinculantes. En ambos modelos aparecen principios comunes: transparencia, no discriminación, supervisión humana y rendición de cuentas.",
        ],
        "contactos": [],
        "fundamento": "Reglamento (UE) 2024/1689; Reglamento (UE) 2026/1744 (Digital Omnibus, DOUE 24-jul-2026); Blueprint for an AI Bill of Rights (OSTP, 2022); NIST AI RMF 1.0 (NIST AI 100-1, enero de 2023); Recomendación de la UNESCO sobre la ética de la IA (2021); Programa de Normatividad de la IA, Unidad 3.",
    },
    {
        "id": "ia_cumplimiento",
        "titulo": "Cumplimiento y gestión de una IA responsable",
        "emoji": "🧰",
        "boton": "Cumplimiento y estándares de IA",
        "relacionados": ["ia_nist_rmf", "ia_unesco", "ia_requisitos", "ia_eeuu_vs_ue", "ia_derechos_humanos"],
        "keywords": [
            ("evaluacion de impacto algoritmico", 10), ("auditoria de algoritmos", 10), ("auditoria algoritmica", 10),
            ("iso iec 23894", 10), ("iso 23894", 10), ("marco de gestion de riesgos", 8),
            ("gobernanza de datos", 7), ("gobernanza de la ia", 8), ("certificacion de ia", 8), ("estandares de ia", 8),
            ("normas iso", 5), ("cumplimiento normativo", 5), ("politicas de ia", 7), ("contratos de ia", 7),
            ("aia$", 5), ("sc 42", 6),
        ],
        "intro": (
            "Cumplir no es solo leer la ley: las organizaciones usan <b>estándares, políticas y evaluaciones</b> para demostrar que su IA respeta los derechos. "
            "Esto corresponde a la <b>Unidad 5</b> de tu programa."
        ),
        "derechos_titulo": "Herramientas de cumplimiento",
        "derechos": [
            "<b>ISO/IEC 23894:</b> guía de gestión de riesgos para IA. <b>ISO/IEC JTC 1/SC 42:</b> comité que desarrolla estándares técnicos de inteligencia artificial.",
            "<b>NIST AI RMF</b> (2023): marco voluntario con cuatro funciones: <b>Gobernar, Mapear, Medir y Gestionar</b> (pregunta por “NIST AI RMF” para ver el detalle).",
            "<b>Evaluación del impacto ético (UNESCO):</b> los Estados deberían exigir evaluaciones que revelen el impacto en derechos humanos, derechos laborales, medio ambiente y personas vulnerables, con auditabilidad, trazabilidad y revisión externa (párrs. 50 a 53).",
            "<b>Políticas de IA responsable</b> y <b>gobernanza de datos y algoritmos</b>: roles y responsables, inventario de sistemas, controles y calidad de datos.",
            "<b>Evaluación de impacto algorítmico (AIA):</b> analizar <i>antes</i> de desplegar a quién afecta el sistema, qué riesgos hay para los derechos y qué medidas lo evitan.",
            "<b>Auditoría de algoritmos:</b> revisión (idealmente independiente) de sesgos, desempeño, seguridad y documentación.",
            "<b>Certificación y evaluación de conformidad</b>, por ejemplo la que exige el AI Act a los sistemas de alto riesgo.",
            "<b>Aspectos contractuales:</b> cláusulas de uso de IA, responsabilidades, protección de datos y acuerdos de nivel de servicio (SLA) con proveedores.",
            "<b>Tendencias:</b> IA general, derechos de autor en contenidos generados por IA, relación con la ciberseguridad y armonización internacional.",
        ],
        "pasos_titulo": "Ejemplo: cómo aplica a este chatbot",
        "pasos": [
            "<b>Transparencia:</b> se identifica como asistente automatizado y cita el fundamento de cada respuesta.",
            "<b>Explicabilidad:</b> funciona con reglas, así que siempre se puede rastrear por qué dio una respuesta.",
            "<b>Privacidad:</b> no guarda mensajes ni pide datos personales.",
            "<b>Exactitud:</b> solo responde con contenido curado; si no sabe, lo dice.",
            "<b>Supervisión humana:</b> deriva a personas e instituciones (911, CODHEM, Línea Sin Violencia, Defensoría).",
            "<b>Seguridad de personas vulnerables:</b> protocolo prioritario ante crisis emocional o peligro.",
        ],
        "fundamento": "Programa de Normatividad de la IA, Unidad 5; NIST AI Risk Management Framework 1.0 (2023); Recomendación de la UNESCO sobre la ética de la IA (2021, párrs. 50 a 53); ISO/IEC 23894; Reglamento (UE) 2024/1689.",
    },
    # ------------------------------------------------------------------ DATOS PERSONALES Y DERECHOS HUMANOS
    {
        "id": "datos_y_derechos_humanos",
        "titulo": "Protección de datos personales y derechos humanos",
        "emoji": "🛡️",
        "boton": "Datos personales y derechos humanos",
        "relacionados": ["privacidad_datos", "ia_derechos_humanos", "ia_unesco", "caso_datos"],
        "keywords": [
            ("proteccion de datos personales en relacion con los derechos humanos", 22),
            ("datos personales en relacion con los derechos humanos", 12),
            ("datos personales y derechos humanos", 12), ("datos personales y los derechos humanos", 12),
            ("proteccion de datos y derechos humanos", 12), ("privacidad y derechos humanos", 10),
            ("privacidad es un derecho humano", 10), ("privacidad como derecho humano", 10),
            ("datos personales como derecho humano", 10), ("relacion entre datos personales", 9),
            ("por que importa la proteccion de datos", 8), ("por que proteger mis datos", 8),
            ("derecho a la intimidad", 6), ("derecho a la privacidad y", 4), ("intimidad y datos", 5),
        ],
        "intro": (
            "Proteger tus <b>datos personales</b> no es solo un trámite: es una forma de proteger tu <b>dignidad, tu autonomía y tu libertad</b>. "
            "Lo que otros saben de ti (salud, ideas, ubicación, imagen) puede usarse para discriminarte, vigilarte o manipularte. "
            "Por eso la <b>privacidad</b> se considera un derecho humano y está ligada a muchos otros."
        ),
        "derechos_titulo": "Cómo se conecta con otros derechos humanos",
        "derechos": [
            "<b>Dignidad y autonomía:</b> la UNESCO dice que la privacidad es esencial para proteger la dignidad, la autonomía y la capacidad de actuar de las personas, y debe respetarse durante todo el ciclo de vida de un sistema de IA (Recomendación, párr. 32).",
            "<b>No discriminación (Art. 1° CPEUM):</b> los datos sensibles (salud, origen étnico, religión, opiniones políticas, datos biométricos o genéticos, antecedentes penales) pueden causar daños excepcionales si se divulgan, por lo que requieren seguridad total (UNESCO, párr. 74).",
            "<b>Libertad de expresión e información (Art. 6° CPEUM):</b> la vida privada y los datos personales se protegen “en los términos y con las excepciones que fijen las leyes” (Art. 6°, apartado A, fracc. II). No es un derecho absoluto: convive con el acceso a la información.",
            "<b>Derecho a defenderte:</b> si una decisión que te afecta se tomó con tus datos o con un algoritmo, debes poder saber por qué y pedir que una persona la revise (UNESCO, párr. 38; en la UE, Art. 86 del Reglamento de IA).",
            "<b>Niñas, niños y adolescentes:</b> se privilegia su interés superior y el consentimiento lo da quien ejerce la patria potestad o tutela, conforme a la ley estatal (Art. 8), y se considera también su opinión según su autonomía progresiva.",
        ],
        "pasos_titulo": "Reglas y garantías clave",
        "pasos": [
            "<b>Constitución, Art. 16, párrafo segundo:</b> toda persona tiene derecho a la protección de sus datos personales y al acceso, rectificación, cancelación y oposición (ARCO). La ley puede fijar excepciones por seguridad nacional, orden público, seguridad y salud públicas o para proteger derechos de terceros.",
            "<b>Límites con proporcionalidad:</b> cuando un derecho choca con otro (por ejemplo, privacidad y seguridad), cualquier limitación debe tener base legal y ser razonable, necesaria y proporcional (UNESCO, párr. 11).",
            "<b>Consentimiento válido:</b> libre, específico, informado e inequívoco, y con <b>aviso de privacidad</b> claro (ley estatal de 2026, Arts. 16 y 22 a 24). Los datos sensibles, por regla general, solo se tratan con consentimiento expreso (Art. 7).",
            "<b>Solo lo necesario:</b> el responsable debe tratar datos adecuados y relevantes, y protegerlos con medidas de seguridad. Si hay una vulneración que afecte de forma significativa tus derechos, debe avisarte, y avisar a la autoridad garante, <b>sin dilación alguna</b> en cuanto confirme que ocurrió (Art. 36 de la ley estatal de 2026).",
            "<b>Evaluación de impacto:</b> antes de poner en marcha sistemas o tecnologías que traten datos de forma intensiva o relevante (datos sensibles, transferencias), una institución pública debe evaluar el impacto en la protección de datos (ley estatal de 2026, Arts. 71 y 72). La UNESCO pide lo mismo para los sistemas algorítmicos, con enfoque de “privacidad desde el diseño” (párr. 34).",
            "<b>Con IA el riesgo crece:</b> la IA puede inferir información privada o identificar personas, y las técnicas de privacidad pueden restar precisión al modelo. El NIST lo reconoce como una disyuntiva que debe resolverse de forma transparente y justificada (AI RMF 1.0, secciones 3 y 3.6).",
            "<b>Tus derechos sobre tus datos:</b> la UNESCO recomienda poder acceder a tus datos personales en sistemas de IA y borrarlos, salvo excepciones legales, y protección reforzada cuando se usan con fines comerciales o se envían al extranjero (párr. 73). Para ejercer ARCO en México, consulta el tema “Mis datos personales”.",
        ],
        "contactos": ["sabg", "transparencia_mx", "codhem"],
        "fundamento": "CPEUM Arts. 1°, 6° (apartado A, fracc. II) y 16 (párr. segundo); Ley de Protección de Datos Personales en Posesión de Sujetos Obligados del Estado de México y Municipios (Gaceta del Gobierno, 1-oct-2026; Arts. 7, 8, 16, 22 a 24, 36, 71 y 72); Recomendación de la UNESCO sobre la ética de la IA (2021, párrs. 11, 32 a 34, 38, 73 y 74); NIST AI RMF 1.0 (2023, secciones 3 y 3.6).",
    },
    # ------------------------------------------------------------------ UNESCO
    {
        "id": "ia_unesco",
        "titulo": "Recomendación de la UNESCO sobre la ética de la IA",
        "emoji": "🌐",
        "boton": "Ética de la IA (UNESCO)",
        "relacionados": ["ia_requisitos", "datos_y_derechos_humanos", "ia_eeuu_vs_ue", "ia_cumplimiento"],
        "keywords": [
            ("recomendacion de la unesco", 10), ("recomendacion unesco", 10), ("etica de la inteligencia artificial", 8),
            ("etica de la ia", 8), ("principios de la unesco", 9), ("valores de la unesco", 9), ("unesco ia", 8), ("unesco$", 6), ("que dice la unesco", 10),
            ("unesco inteligencia artificial", 8), ("principios eticos de la unesco", 10), ("unesco y la ia", 8),
            ("decalogo de la unesco", 8), ("ambitos de accion politica", 8),
        ],
        "intro": (
            "La <b>Recomendación sobre la Ética de la Inteligencia Artificial</b> fue aprobada por la UNESCO el <b>23 de noviembre de 2021</b>. "
            "Es el primer marco ético mundial para la IA, centrado en la <b>dignidad humana y los derechos humanos</b>. "
            "Es <b>voluntaria</b>: recomienda que los Estados la apliquen con las medidas legislativas o de otra índole que correspondan; no es una ley que obligue por sí misma."
        ),
        "derechos_titulo": "4 valores y 10 principios",
        "derechos": [
            "<b>Valores:</b> (1) respeto, protección y promoción de los derechos humanos, las libertades fundamentales y la dignidad; (2) prosperidad del medio ambiente y los ecosistemas; (3) diversidad e inclusión; (4) vivir en sociedades pacíficas, justas e interconectadas.",
            "<b>Principios:</b> proporcionalidad e inocuidad; seguridad y protección; equidad y no discriminación; sostenibilidad; derecho a la intimidad y protección de datos; supervisión y decisión humanas; transparencia y explicabilidad; responsabilidad y rendición de cuentas; sensibilización y educación; y gobernanza y colaboración adaptativas y de múltiples partes interesadas.",
            "<b>Proporcionalidad:</b> usar IA solo si es adecuada y proporcional a un objetivo legítimo y sin violar derechos humanos; en decisiones irreversibles o de vida o muerte, la decisión final debe ser humana. Los sistemas de IA <b>no deberían usarse para calificación social ni vigilancia masiva</b> (párr. 26).",
            "<b>Equidad:</b> reducir al mínimo los resultados discriminatorios o sesgados y garantizar un <b>recurso efectivo</b> contra la discriminación algorítmica (párr. 29).",
            "<b>Responsabilidad:</b> la responsabilidad recae siempre en personas físicas o jurídicas; <b>no se debe otorgar personalidad jurídica a los sistemas de IA</b> (párr. 68).",
        ],
        "pasos_titulo": "Qué piden a los Estados (ámbitos de acción)",
        "pasos": [
            "<b>Evaluación del impacto ético</b> de los sistemas de IA, con análisis de riesgos para los derechos humanos, los derechos laborales y las personas vulnerables, y participación ciudadana (párrs. 50 a 53). Si un sistema llevaría a violar obligaciones de derechos humanos, se debe <b>prohibir su uso</b> (párr. 57).",
            "<b>Gobernanza ética:</b> mecanismos de supervisión, auditoría y reparación de daños; protección de denunciantes; y reglas de responsabilidad (párrs. 54 a 70).",
            "<b>Política de datos:</b> calidad de los datos de entrenamiento, protección de la privacidad, datos sensibles y control de las personas sobre sus datos (párrs. 71 a 77).",
            "<b>Transparencia ante las personas usuarias:</b> poder saber si interactúas con una persona o con un sistema de IA que imita rasgos humanos, rechazar esa interacción y pedir intervención humana (párr. 127).",
            "<b>Educación (párr. 104):</b> la IA debe apoyar el aprendizaje sin reducir las capacidades cognitivas ni recabar información sensible, y los datos del estudiantado no deben usarse de forma indebida ni con fines comerciales.",
            "<b>Otros ámbitos:</b> medio ambiente, género, cultura, comunicación e información, economía y trabajo, salud y bienestar social, y desarrollo y cooperación internacional.",
        ],
        "contactos": [],
        "fundamento": "Recomendación sobre la Ética de la Inteligencia Artificial, UNESCO (SHS/BIO/REC-AIETHICS/2021), párrs. 2, 11, 26, 29, 50 a 57, 68, 71 a 77, 104 y 127; Programa de Normatividad de la IA, Unidad 4.",
    },
    # ------------------------------------------------------------------ NIST
    {
        "id": "ia_nist_rmf",
        "titulo": "NIST AI RMF: marco de gestión de riesgos de la IA (EE. UU.)",
        "emoji": "🧭",
        "boton": "NIST AI RMF (EE. UU.)",
        "relacionados": ["ia_eeuu_vs_ue", "ia_cumplimiento", "ia_requisitos"],
        "keywords": [
            ("nist ai rmf", 12), ("ai rmf", 10), ("ai risk management framework", 12), ("nist ai 100", 10),
            ("marco de gestion de riesgos de ia del nist", 12), ("marco de gestion de riesgos del nist", 12),
            ("marco del nist", 9), ("nist", 6), ("gobernar mapear medir", 12), ("govern map measure manage", 12),
            ("caracteristicas de una ia confiable", 8), ("ia confiable segun nist", 10), ("riesgos de la ia segun nist", 10),
        ],
        "intro": (
            "El <b>AI Risk Management Framework (AI RMF 1.0)</b> es una guía del <b>NIST</b> (Instituto Nacional de Estándares y Tecnología de EE. UU.), publicada en <b>enero de 2023</b> como NIST AI 100-1. "
            "Es <b>voluntaria</b>, no sectorial y aplicable a cualquier caso de uso. Su meta es ayudar a las organizaciones a gestionar los riesgos de la IA y a promover sistemas <b>confiables y responsables</b>."
        ),
        "derechos_titulo": "7 características de una IA confiable",
        "derechos": [
            "<b>Válida y fiable:</b> funciona como se espera, con precisión y solidez; es la base de las demás.",
            "<b>Segura:</b> no pone en peligro la vida, la salud, los bienes ni el medio ambiente.",
            "<b>Protegida y resiliente:</b> resiste ataques y cambios inesperados, y se degrada de forma controlada.",
            "<b>Responsable y transparente:</b> se sabe quién responde y hay información suficiente sobre el sistema.",
            "<b>Explicable e interpretable:</b> se entiende cómo funciona y qué significa su resultado.",
            "<b>Con privacidad mejorada:</b> protege la autonomía, la identidad y la dignidad de las personas.",
            "<b>Justa, con sesgos nocivos gestionados:</b> considera la equidad y distingue tres tipos de sesgo: sistémico, computacional/estadístico y cognitivo humano.",
            "Ninguna característica basta por sí sola: hay <b>disyuntivas</b> (por ejemplo, entre precisión e interpretabilidad) y deben resolverse según el contexto y de forma transparente.",
        ],
        "pasos_titulo": "Las 4 funciones del núcleo (Core)",
        "pasos": [
            "<b>GOBERNAR (Govern):</b> crear una cultura de gestión de riesgos: políticas, roles y responsabilidades, capacitación, diversidad en los equipos, inventario de sistemas, manejo de terceros y retiro seguro de sistemas. Aplica a todo el ciclo de vida.",
            "<b>MAPEAR (Map):</b> entender el contexto: propósito, usuarios, posibles impactos en personas y sociedad, límites del sistema y riesgos de componentes de terceros. Con esto se decide si se diseña o despliega el sistema (decisión de “seguir o no seguir”).",
            "<b>MEDIR (Measure):</b> evaluar y vigilar los riesgos con métodos y métricas, pruebas antes y durante la operación, evaluación independiente y canales de retroalimentación de personas afectadas.",
            "<b>GESTIONAR (Manage):</b> priorizar los riesgos y responder (mitigar, transferir, evitar o aceptar), documentar los riesgos residuales, vigilar el sistema tras su despliegue y <b>desactivarlo</b> si se desvía de su uso previsto.",
            "<b>Riesgo inaceptable:</b> si hay impactos graves inminentes o daños ocurriendo, el NIST indica que el desarrollo y el despliegue deben detenerse de forma segura hasta poder manejar los riesgos.",
            "<b>Importante:</b> el AI RMF no fija cuánto riesgo es aceptable ni sustituye la ley; las organizaciones deben cumplir las normas aplicables. Contempla “perfiles” por sector o caso de uso.",
        ],
        "contactos": [],
        "fundamento": "NIST AI 100-1, Artificial Intelligence Risk Management Framework (AI RMF 1.0), enero de 2023: Resumen ejecutivo, secciones 1.2, 3 y 5 y Tablas 1 a 4 (https://doi.org/10.6028/NIST.AI.100-1).",
    },
    # ------------------------------------------------------------------ MENÚ DE TEMAS
    {
        "id": "mas_temas",
        "titulo": "Más temas",
        "emoji": "🗂️",
        "boton": "Ver más temas",
        "keywords": [
            ("mas temas", 8), ("otros temas", 8), ("temario", 6), ("que temas", 8), ("temas disponibles", 8), ("de que puedes hablar", 8),
            ("que sabes", 6), ("que puedes hacer", 6), ("menu", 5), ("ayuda con el chat", 5),
        ],
        "relacionados": ["unidad3_hub", "unidad4_hub", "origen_dh", "acoso_como_saber", "abuso_laboral_como_saber", "ia_detectar_vulneracion",
                         "lista_dh", "que_son_dh", "estudiante_vs_ciudadano", "persona_vs_animal",
                         "discriminacion_como_saber", "violencia_docente", "acoso_hostigamiento",
                         "emergencia_menores", "ley_olimpia", "ia_requisitos", "ia_eeuu_vs_ue",
                         "ia_alto_riesgo", "ia_cumplimiento", "ia_unesco", "ia_nist_rmf", "datos_y_derechos_humanos",
                         "ia_plan_nacional", "ia_chapultepec", "ia_plan_capacidades",
                         "acceso_informacion", "info_reservada_recurso", "transparencia_mexiquense",
                         "detencion_policia", "victima_delito",
                         "salud_mental", "privacidad_bot", "fuentes"],
        "intro": "Estos son otros temas que puedo explicarte. Elige uno o escríbeme tu pregunta con tus palabras:",
        "fundamento": "Índice de temas del asistente.",
    },
    # ------------------------------------------------------------------ MÁS CASOS PRÁCTICOS
    {
        "id": "caso_laboral",
        "titulo": "Caso práctico: las prácticas profesionales con maltrato",
        "emoji": "🧩",
        "boton": "Caso: prácticas con maltrato",
        "keywords": [],
        "relacionados": ["casos_practicos", "abuso_laboral"],
        "intro": (
            "<i>Diego hace sus prácticas profesionales en una empresa. Su encargada le grita frente al equipo, le asigna horas extra sin pago "
            "y le dice que, si se queja, “no le firma su liberación”.</i>"
        ),
        "derechos_titulo": "Derechos en juego",
        "derechos": [
            "<b>Trato digno:</b> ser practicante no le quita sus derechos humanos.",
            "Derecho a <b>condiciones justas</b> y a no sufrir amenazas ni humillaciones (violencia laboral).",
            "Derecho a <b>no sufrir represalias</b> por quejarse.",
        ],
        "pasos_titulo": "¿Qué se puede hacer?",
        "pasos": [
            "<b>Documentar:</b> fechas, frases, testigos, horarios reales y mensajes; guardar el convenio de prácticas.",
            "Avisar a la <b>coordinación de la Facultad</b> responsable de las prácticas, por escrito, para que oriente y revise la relación con la empresa.",
            "Usar el canal interno de la empresa (recursos humanos), también por escrito.",
            "Pedir orientación gratuita a la <b>PROFEDET</b> sobre horas extra y condiciones.",
            "Si hay amenazas, lesiones o acoso sexual, acudir al <b>Ministerio Público</b>.",
            "No firmar nada bajo presión sin leerlo.",
        ],
        "contactos": ["profedet", "defensoria_uaemex", "fgjem"],
        "fundamento": "CPEUM Arts. 1° y 123; Ley General de Acceso de las Mujeres a una Vida Libre de Violencias (Arts. 10 y 11); Ley Federal del Trabajo.",
    },
    {
        "id": "caso_noviazgo",
        "titulo": "Caso práctico: celos, control y un empujón “sin querer”",
        "emoji": "🧩",
        "boton": "Caso: celos y control en el noviazgo",
        "keywords": [],
        "relacionados": ["casos_practicos", "violentometro", "violencia_mujeres"],
        "intro": (
            "<i>Ana y Luis llevan ocho meses de novios. Él revisa su celular, le pide que no vea a ciertas amigas, la ignora por días cuando se enoja y, en una discusión, "
            "la empujó “sin querer”.</i>"
        ),
        "derechos_titulo": "Qué muestra el violentómetro",
        "derechos": [
            "<b>Primer nivel:</b> celar y la “ley del hielo” (ignorar).",
            "<b>Segundo nivel:</b> controlar o prohibir (revisar el celular, aislarla de sus amistades) y un empujón o jaloneo.",
            "La violencia psicológica y la física están reconocidas como violencia contra las mujeres (Art. 6): <b>no es “normal” ni “por amor”</b> y puede escalar.",
        ],
        "pasos_titulo": "¿Qué se puede hacer?",
        "pasos": [
            "Reconocer las señales y <b>no justificarlas</b>: un empujón ya es violencia física.",
            "Contarlo a una amistad o familiar de confianza y <b>guardar evidencia</b> (mensajes, capturas, fechas).",
            "Llamar a la <b>Línea Sin Violencia</b> para orientación jurídica y psicológica; el servicio de atención psicológica de la Facultad también puede acompañarla.",
            "Preparar un <b>plan de seguridad</b>: un lugar seguro al cual ir, documentos importantes a la mano y a quién llamar.",
            "Si hay riesgo inmediato, llamar al <b>911</b>. Puede solicitar <b>órdenes de protección</b> ante el Ministerio Público.",
            "Si Luis quiere cambiar sus conductas, puede pedir ayuda a <b>Hombre a Hombre</b>.",
        ],
        "contactos": ["sin_violencia", "911", "fgjem", "uaemex_psico", "hombre_a_hombre", "ipn_violentometro"],
        "fundamento": "Violentómetro del IPN; Ley General de Acceso de las Mujeres a una Vida Libre de Violencias (Arts. 6, 7 y 27 y siguientes).",
    },
    {
        "id": "caso_datos",
        "titulo": "Caso práctico: la lista pública con calificaciones y datos de salud",
        "emoji": "🧩",
        "boton": "Caso: lista pública de calificaciones",
        "keywords": [],
        "relacionados": ["casos_practicos", "privacidad_datos"],
        "intro": (
            "<i>Una coordinación publica en un grupo abierto de redes sociales una lista con nombres, matrículas y calificaciones de todo el grupo, "
            "e incluye quién reprobó y quién tiene un apoyo por una condición de salud.</i>"
        ),
        "derechos_titulo": "Derechos en juego",
        "derechos": [
            "<b>Protección de datos personales</b> (Art. 16 CPEUM): nombre, matrícula y calificaciones son datos personales.",
            "<b>Datos sensibles:</b> la condición de salud exige especial protección porque su uso indebido puede generar discriminación.",
            "Derecho a que el tratamiento se informe en un <b>aviso de privacidad</b> y se limite a lo necesario.",
            "Derechos <b>ARCO</b>, en especial <b>cancelación y oposición</b>.",
        ],
        "pasos_titulo": "¿Qué se puede hacer?",
        "pasos": [
            "Pedir <b>por escrito</b> el retiro inmediato de la lista y ejercer los derechos de oposición y cancelación ante la <b>Unidad de Transparencia</b> de la institución (el ejercicio de ARCO es gratuito).",
            "Pedir el <b>aviso de privacidad</b> y saber con qué fin se publicaron los datos.",
            "La institución debe responder en un plazo máximo de <b>20 días</b>. Si no responde o niega sin razón, se puede acudir a la autoridad en materia de datos personales (verifica cuál corresponde).",
            "Presentar queja ante la Defensoría de los Derechos Universitarios.",
            "Si el dato de salud generó burlas o exclusión, también puede haber <b>discriminación</b>.",
        ],
        "contactos": ["defensoria_uaemex", "sabg", "codhem"],
        "fundamento": "CPEUM Art. 16; Ley General de Protección de Datos Personales en Posesión de Sujetos Obligados (Arts. 3, 43 a 45; DOF 20-03-2025).",
    },
    {
        "id": "caso_ia",
        "titulo": "Caso práctico: el sistema de IA que rechaza becas",
        "emoji": "🧩",
        "boton": "Caso: IA y becas",
        "keywords": [],
        "relacionados": ["casos_practicos", "ia_derechos_humanos", "ia_alto_riesgo"],
        "intro": (
            "<i>Una universidad usa un sistema de IA para preseleccionar solicitudes de beca. Sofía descubre que casi nadie de su colonia ni de escuelas públicas es aceptado, "
            "y nadie sabe explicarle por qué el sistema la rechazó.</i>"
        ),
        "derechos_titulo": "Derechos y principios en juego",
        "derechos": [
            "<b>No discriminación y sesgo algorítmico:</b> si el sistema perjudica a un grupo por su origen o condición social, puede haber discriminación.",
            "<b>Explicación y transparencia:</b> “si una decisión no puede explicarse, no debe automatizarse”.",
            "<b>Supervisión y responsables humanos:</b> alguien debe responder por la decisión y poder corregirla.",
            "<b>Datos personales:</b> saber qué datos se usaron y para qué.",
            "En la UE, la IA que decide el <b>acceso a la educación</b> se considera de <b>alto riesgo</b> (Anexo III).",
        ],
        "pasos_titulo": "¿Qué se puede hacer?",
        "pasos": [
            "Pedir <b>por escrito</b> la convocatoria, los criterios y una explicación del resultado.",
            "Solicitar que <b>una persona</b> revise su caso.",
            "Ejercer sus derechos <b>ARCO</b> para conocer los datos que el sistema usó.",
            "Si hay indicios de discriminación, acudir a la Defensoría universitaria o a la CODHEM.",
            "Como referencia: México no tiene (hasta donde se pudo verificar) una ley general de IA; se aplican las normas generales de derechos humanos y datos personales, y los Principios de Chapultepec son orientadores.",
        ],
        "contactos": ["defensoria_uaemex", "codhem", "sabg"],
        "fundamento": "CPEUM Arts. 1°, 6° y 16; Principios de Chapultepec; Reglamento (UE) 2024/1689 (Anexo III, punto 3).",
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
            "casos_practicos", "violencia_digital", "salud_mental", "emergencia",
            "violencia_mujeres", "violentometro", "abuso_laboral", "ia_derechos_humanos",
            "unidad3_hub", "unidad4_hub", "acceso_informacion", "ia_plan_nacional", "mas_temas"]

# ---------------------------------------------------------------------------
# v5: preguntas frecuentes + Unidades 3 y 4 del temario (ver knowledge_unidades.py)
# ---------------------------------------------------------------------------
from knowledge_unidades import TOPICS_NUEVOS, CONTACTS_NUEVOS, SOURCES_NUEVAS  # noqa: E402

TOPICS.extend(TOPICS_NUEVOS)
CONTACTS.update(CONTACTS_NUEVOS)
SOURCES.extend(SOURCES_NUEVAS)

# ---------------------------------------------------------------------------
# v6: LGTAIP (acceso a la información), Transparencia Mexiquense y Plan Nacional de IA
# (ver knowledge_v6.py)
# ---------------------------------------------------------------------------
from knowledge_v6 import TOPICS_V6, CONTACTS_V6, SOURCES_V6  # noqa: E402

TOPICS.extend(TOPICS_V6)
CONTACTS.update(CONTACTS_V6)
SOURCES.extend(SOURCES_V6)

