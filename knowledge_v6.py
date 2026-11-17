"""
CONTENIDO NUEVO (v6): documentos que pasó la profesora.

  1) Ley General de Transparencia y Acceso a la Información Pública (LGTAIP)
     "Nueva Ley" publicada en el DOF el 20-03-2025  -> temas `acceso_informacion`,
     `info_reservada_recurso` y `transparencia_mexiquense`.
  2) Plan Nacional de Inteligencia Artificial (ATDT, abril de 2026)
     -> temas `ia_plan_nacional`, `ia_chapultepec` e `ia_plan_capacidades`.

Este archivo solo contiene DATOS; knowledge.py lo importa al final y agrega:
    TOPICS_V6 -> se suman a TOPICS        CONTACTS_V6 -> se suman a CONTACTS
    SOURCES_V6 -> se suman a SOURCES

Las palabras clave van SIN acentos y en minúsculas (ver models.py):
  - frase con espacios: debe aparecer completa;  - "palabra$": palabra exacta;  - "palabra": prefijo.

Todo dato que cambia con el tiempo lleva la nota "verifica".
"""

CONTACTS_V6 = {}

SOURCES_V6 = [
    {"name": "Ley de Transparencia y Acceso a la Información Pública del Estado de México y Municipios (Gaceta del Gobierno, 1-oct-2026)",
     "url": "https://legislacion.edomex.gob.mx/"},
    {"name": "Ley General de Transparencia y Acceso a la Información Pública (nueva ley, DOF 20-03-2025)",
     "url": "https://www.diputados.gob.mx/LeyesBiblio/pdf/LGTAIP.pdf"},
    {"name": "Transparencia Mexiquense – portal de transparencia y datos abiertos (Secretaría de la Contraloría del Edomex)",
     "url": "http://portal.secogem.gob.mx/transparencia-datos-abiertos"},
    {"name": "Plan Nacional de Inteligencia Artificial (Agencia de Transformación Digital y Telecomunicaciones, abril de 2026)",
     "url": "https://www.gob.mx/atdt"},
    {"name": "Principios de Chapultepec (SECIHTI y ATDT, 29 de enero de 2026)",
     "url": "https://secihti.mx/"},
]

TOPICS_V6 = [
    # ====================================================================== LGTAIP
    {
        "id": "acceso_informacion",
        "titulo": "Derecho de acceso a la información pública",
        "emoji": "🔎",
        "boton": "Pedir información pública",
        "relacionados": ["info_reservada_recurso", "transparencia_mexiquense", "privacidad_datos"],
        "keywords": [
            ("derecho de acceso a la informacion", 10), ("acceso a la informacion publica", 10), ("lgtaip", 10),
            ("ley general de transparencia", 11), ("solicitud de informacion", 8), ("solicitar informacion", 7),
            ("como pido informacion", 9), ("como puedo pedir informacion", 9), ("pedir informacion", 6),
            ("pedir informacion al gobierno", 9), ("informacion publica", 6), ("unidad de transparencia", 8),
            ("plataforma nacional de transparencia", 10), ("sujetos obligados", 7), ("sujeto obligado", 7),
            ("transparencia", 4), ("maxima publicidad", 8), ("cuanto tardan en responder", 7),
            ("plazo para responder", 6), ("ley de transparencia", 9), ("ley de transparencia del estado de mexico", 12),
            ("ley de transparencia del edomex", 12), ("ley estatal de transparencia", 11), ("transparencia en el estado de mexico", 9),
        ],
        "intro": (
            "El <b>acceso a la información pública</b> es un derecho humano (Art. 6° de la Constitución). La <b>Ley General de Transparencia y "
            "Acceso a la Información Pública (LGTAIP)</b>, nueva ley publicada en el DOF el 20-mar-2025, dice que este derecho comprende "
            "<b>solicitar, investigar, difundir, buscar y recibir</b> información (Art. 4). Por regla general, <b>toda la información en poder de "
            "los sujetos obligados es pública</b> y accesible a cualquier persona, y la ley se interpreta con <b>máxima publicidad</b> (Arts. 4 y 7)."
        ),
        "derechos_titulo": "Qué debes saber",
        "derechos": [
            "<b>¿A quién se la puedes pedir?</b> A los <i>sujetos obligados</i>: cualquier autoridad u organismo de los poderes Ejecutivo, Legislativo y Judicial "
            "de los tres niveles de gobierno, órganos autónomos, partidos, fideicomisos y fondos públicos, y cualquier persona o sindicato que reciba y ejerza "
            "recursos públicos o realice actos de autoridad (Art. 3, fracc. XIX). En general, las universidades públicas entran por recibir recursos públicos; "
            "confirma en la Unidad de Transparencia de la UAEMéx.",
            "<b>Solo pueden pedirte tres cosas</b> (Art. 126): un medio para recibir notificaciones, la descripción de la información que quieres y la "
            "modalidad en que la prefieres (consulta directa, copias simples o certificadas, o medios electrónicos). No pueden exigirte más requisitos.",
            "<b>La Unidad de Transparencia debe apoyarte</b> a redactar tu solicitud y garantizar condiciones de accesibilidad (Art. 123). Puedes pedir un formato accesible "
            "o que se te entregue en una <b>lengua indígena</b> (Art. 126).",
            "<b>Costos</b> (Art. 143): solo pueden cobrarte materiales de reproducción, envío y certificación. <b>Es gratis</b> si son <b>no más de 20 hojas simples</b>, y la "
            "Unidad puede exentar el pago según tu situación socioeconómica.",
            "<b>Nadie puede ser sancionado o investigado</b> por ejercer este derecho (Art. 5).",
            "<b>No tienes que explicar para qué quieres la información:</b> los sujetos obligados no pueden recabar datos que lleven a indagar los motivos de la solicitud ni el uso que le darás (Art. 121 de la ley estatal).",
        ],
        "pasos_titulo": "Cómo pedirla, paso a paso",
        "pasos": [
            "<b>Identifica a quién se la pides:</b> la institución que tiene o debería tener esa información. Si no es competente, debe avisarte <b>dentro de 3 días</b> "
            "y, si puede, decirte a quién acudir (Art. 138 de la ley general; Art. 133 de la ley estatal, en días hábiles).",
            "<b>Presenta la solicitud ante su Unidad de Transparencia</b> por la <b>Plataforma Nacional de Transparencia</b>, en la oficina, por correo electrónico, correo postal, "
            "mensajería, telégrafo o <b>verbalmente</b> (Art. 124 de la ley general; Art. 119 de la ley estatal).",
            "<b>Guarda tu folio o acuse.</b> En la Plataforma el folio se asigna solo; si la presentas por otro medio, la Unidad debe registrarla en 5 días y enviarte un acuse con la fecha, el folio y los plazos (Art. 125).",
            "<b>Plazo de respuesta:</b> máximo <b>20 días hábiles</b> desde el día siguiente a la presentación; excepcionalmente se amplía hasta <b>10 días más</b> si el "
            "Comité de Transparencia lo justifica antes de que venza (Arts. 128 y 134 de la ley general; Art. 129 de la ley estatal).",
            "Si tu solicitud es poco clara, pueden <b>prevenirte una sola vez</b> (dentro de 5 días); tendrás hasta 10 días para aclararla. Si no lo haces, se tiene por no presentada (Art. 130).",
            "Si no te responden o no estás conforme con la respuesta, puedes presentar un <b>recurso de revisión</b> (consulta el tema <i>“Me negaron información”</i>).",
            "<b>Si la institución es del Estado de México</b> (por ejemplo, la UAEMéx o un municipio), aplica además la <b>Ley de Transparencia y Acceso a la Información Pública del Estado de México y Municipios</b> (Gaceta del Gobierno, 1-oct-2026), con el mismo procedimiento: plazos en <b>días hábiles</b>, solicitud ante la Unidad de Transparencia (Arts. 119 a 121), respuesta en máximo 20 días hábiles, ampliables 10 (Art. 129) y costos del Art. 138. La ley general fija las bases mínimas (Art. 2, fracc. III).",
        ],
        "contactos": ["transparencia_mx", "uaemex_portal"],
        "fundamento": "CPEUM Art. 6°; Ley General de Transparencia y Acceso a la Información Pública (nueva ley, DOF 20-03-2025), Arts. 2, 3, 4, 5, 7, 123 a 128, 130, 134, 138 y 143; Ley de Transparencia y Acceso a la Información Pública del Estado de México y Municipios (Gaceta del Gobierno, 1-oct-2026, decreto 365), Arts. 119 a 121, 125, 129, 133 y 138.",
    },
    {
        "id": "info_reservada_recurso",
        "titulo": "Me negaron información: reservada, confidencial y recurso de revisión",
        "emoji": "🚫",
        "boton": "Me negaron información",
        "relacionados": ["acceso_informacion", "transparencia_mexiquense", "privacidad_datos"],
        "keywords": [
            ("me negaron la informacion", 10), ("me niegan la informacion", 10), ("me negaron informacion", 9), ("negaron informacion", 8),
            ("informacion reservada", 10), ("informacion confidencial", 9), ("informacion clasificada", 9), ("clasificaron la informacion", 9),
            ("recurso de revision", 10), ("version publica", 8), ("prueba de interes publico", 8),
            ("no respondieron mi solicitud", 9), ("no me respondieron la solicitud", 9), ("no me contestan la solicitud", 8),
            ("inexistencia de informacion", 8), ("informacion incompleta", 6), ("reservada", 4), ("confidencial", 3),
        ],
        "intro": (
            "No toda la información se entrega: la ley permite clasificarla como <b>reservada</b> (de forma temporal y por causas de interés público) o como "
            "<b>confidencial</b>. Pero la regla es la publicidad: el área debe <b>fundar y motivar</b> la clasificación y el <b>Comité de Transparencia</b> "
            "decide si la confirma, la modifica o la revoca (Art. 139). Si te niegan o no te responden, puedes <b>impugnar</b>."
        ),
        "derechos_titulo": "Qué se puede (y qué no) reservar",
        "derechos": [
            "<b>Reservada</b> (Art. 112): por ejemplo, si su publicación compromete la seguridad nacional o pública, pone en riesgo la vida, seguridad o salud de una persona, "
            "obstruye la prevención o persecución de delitos o una carpeta de investigación, o es parte de una deliberación aún sin decisión definitiva.",
            "<b>No puede reservarse</b> la información sobre <b>violaciones graves a los derechos humanos</b> o delitos de lesa humanidad (Art. 5).",
            "<b>Confidencial</b> (Art. 115): los <b>datos personales</b> de una persona identificada o identificable (sin límite de tiempo; solo acceden sus titulares, representantes y personal facultado) "
            "y los secretos bancario, fiduciario, industrial, comercial, fiscal, bursátil y postal de particulares.",
            "También es confidencial <b>confirmar o negar si existe</b> una queja, denuncia o procedimiento administrativo en trámite contra una persona servidora pública o un particular, mientras no haya sanción firme (Art. 115).",
            "Si un documento tiene partes reservadas o confidenciales, lo que corresponde es entregarte una <b>versión pública</b> (con esas partes eliminadas u omitidas; Art. 3, fracc. XXI).",
        ],
        "pasos_titulo": "Cómo presentar un recurso de revisión",
        "pasos": [
            "<b>Cuándo procede</b> (Art. 145): clasificación, declaración de inexistencia o de incompetencia, información incompleta o que no corresponde a lo pedido, <b>falta de respuesta</b> "
            "en el plazo, entrega en formato o modalidad distinta o incomprensible, costos o tiempos de entrega, falta de trámite, negativa a la consulta directa, o falta de fundamentación y motivación.",
            "<b>Plazo:</b> dentro de los <b>15 días</b> siguientes a la notificación de la respuesta o al vencimiento del plazo para responder (Art. 144). Los plazos en días son <b>hábiles</b> (Art. 128).",
            "<b>Dónde:</b> ante la <b>autoridad garante</b> que corresponda o ante la <b>Unidad de Transparencia</b> que atendió tu solicitud, que debe enviarlo a más tardar al día siguiente (Art. 144). "
            "En el Estado de México, en general, es <b>Transparencia Mexiquense</b> (Art. 27 de la ley estatal; verifica cuál es la autoridad garante de la institución a la que le pediste). La ley estatal también fija 15 días hábiles para el recurso (Art. 139), 40 días para resolverlo (Art. 143) y 10 días hábiles para entregar la información si ganas por falta de respuesta (Art. 144).",
            "<b>Qué debe incluir</b> (Art. 146): el sujeto obligado, tu nombre y medio para notificaciones, el <b>folio</b>, la fecha de la respuesta (o de tu solicitud si no respondieron), el acto que recurres, "
            "tus razones de inconformidad y copia de la respuesta. <b>No tienes que ratificarlo.</b>",
            "Si falta algo, te previenen <b>una sola vez</b> y tienes 5 días para corregirlo (Art. 147).",
            "<b>Resolución:</b> máximo 40 días desde la admisión (ampliables una vez hasta 20 más), con <b>suplencia de la queja a tu favor</b> (Art. 148); la autoridad aplica una <b>prueba de interés público</b> (Art. 152). "
            "Si ganas porque no te habían respondido, deben darte acceso en máximo 10 días hábiles y sin pagar derechos de reproducción (Art. 149).",
            "Si tienes una discapacidad o hablas una lengua indígena, se procurará darte <b>gratuitamente un traductor o intérprete</b> (Art. 144).",
        ],
        "contactos": ["transparencia_mx"],
        "fundamento": "Ley General de Transparencia y Acceso a la Información Pública (nueva ley, DOF 20-03-2025), Arts. 3 fracc. XXI, 5, 112, 115, 128, 139 y 144 a 149 y 152; Ley de Transparencia y Acceso a la Información Pública del Estado de México y Municipios (Gaceta del Gobierno, 1-oct-2026), Arts. 27, 106, 108, 109, 139, 141 a 144 y 147.",
    },
    {
        "id": "transparencia_mexiquense",
        "titulo": "Transparencia Mexiquense: ¿qué es y dónde acudo?",
        "emoji": "🏛️",
        "boton": "Transparencia Mexiquense",
        "relacionados": ["acceso_informacion", "info_reservada_recurso", "privacidad_datos"],
        "keywords": [
            ("transparencia mexiquense", 12), ("infoem", 12), ("que paso con el infoem", 12), ("desaparecio el infoem", 12),
            ("800 honesto", 10), ("honesto", 4), ("autoridad garante", 9), ("organo garante", 9),
            ("modulo de transparencia", 10), ("secretaria de la contraloria", 7), ("secogem", 8),
            ("contraloria del estado de mexico", 8), ("070$", 6),
        ],
        "intro": (
            "<b>Transparencia Mexiquense</b> es la <b>autoridad garante local</b> en materia de transparencia, acceso a la información y datos personales en el Estado de México. "
            "Es un órgano administrativo desconcentrado de la <b>Secretaría de la Contraloría</b> del Poder Ejecutivo estatal y asumió las funciones del <b>INFOEM</b>, "
            "que desapareció; según la prensa estatal, comenzó a operar en octubre de 2026."
        ),
        "derechos_titulo": "Qué debes saber",
        "derechos": [
            "<b>¿Por qué está en la Contraloría?</b> La LGTAIP define a la autoridad garante local como los órganos encargados de la <b>contraloría</b> u homólogos del Poder Ejecutivo de cada "
            "entidad federativa, que también atienden los asuntos de transparencia de sus municipios (Art. 3, fracc. IV).",
            "<b>Qué hace:</b> recibe y resuelve <b>recursos de revisión</b> sobre solicitudes de información y atiende la <b>protección de datos personales</b> en posesión de instituciones públicas del Estado de México.",
            "<b>Naturaleza (Art. 27 de la ley estatal):</b> es el órgano administrativo desconcentrado de la Secretaría de la Contraloría que actúa como <b>Autoridad Garante Local</b>, con autonomía técnica y operativa.",
            "Según la prensa estatal, los trámites que estaban en el INFOEM <b>continúan</b> bajo su responsabilidad.",
            "<b>Ojo:</b> según la prensa, el Poder Legislativo local designó a su propia contraloría como autoridad garante (octubre de 2026). La autoridad garante puede variar según el sujeto obligado, "
            "porque la LGTAIP prevé también los órganos internos de control de los poderes y órganos autónomos (Art. 3, fracc. V). <b>Verifica</b> a quién corresponde tu caso.",
        ],
        "pasos_titulo": "Cómo usarla",
        "pasos": [
            "<b>Para pedir información</b> a una institución, presenta tu solicitud en la Unidad de Transparencia de esa institución (consulta <i>“Pedir información pública”</i>).",
            "<b>Si no te responden o te niegan</b> la información, presenta un recurso de revisión (consulta <i>“Me negaron información”</i>).",
            "<b>Para orientación,</b> acude al módulo de atención o llama a la línea gratuita (datos abajo). La línea <b>800 HONESTO</b> es la línea gratuita de la Secretaría de la Contraloría.",
            "<b>Datos personales:</b> primero ejerce tus derechos ARCO ante el responsable; si no te atiende, acude a la autoridad garante (consulta <i>“Mis datos personales”</i>).",
        ],
        "contactos": ["transparencia_mx"],
        "fundamento": "Ley General de Transparencia y Acceso a la Información Pública (DOF 20-03-2025), Art. 3 fracs. III a V; Ley de Transparencia y Acceso a la Información Pública del Estado de México y Municipios (Gaceta del Gobierno, 1-oct-2026), Arts. 3 fracc. III y 27; datos de contacto institucionales (la dirección, el conmutador 722 275 6700 y la línea 800 466 3786 coinciden con los publicados por la Secretaría de la Contraloría del Estado de México); creación de Transparencia Mexiquense y extinción del INFOEM según prensa estatal (octubre de 2026). Verifica en el portal oficial.",
    },

    # ====================================================================== PLAN NACIONAL DE IA
    {
        "id": "ia_plan_nacional",
        "titulo": "Plan Nacional de Inteligencia Artificial de México (abril 2026)",
        "emoji": "🇲🇽",
        "boton": "Plan Nacional de IA",
        "relacionados": ["ia_chapultepec", "ia_plan_capacidades", "ia_derechos_humanos", "ia_requisitos", "ia_eeuu_vs_ue"],
        "keywords": [
            ("plan nacional de inteligencia artificial", 13), ("plan nacional de ia", 13), ("plan nacional ia", 12),
            ("estrategia nacional de ia", 10), ("estrategia nacional de inteligencia artificial", 10),
            ("atdt", 8), ("agencia de transformacion digital", 10), ("regulacion de la ia en mexico", 9),
            ("ley de ia en mexico", 9), ("ley de inteligencia artificial en mexico", 9), ("marco legal de la ia", 7),
            ("gobernanza de la ia", 8), ("ia en mexico", 6), ("transparencia algoritmica", 8),
            ("tres pilares", 7), ("ia en el sector publico", 8), ("ilia", 6),
        ],
        "intro": (
            "El <b>Plan Nacional de Inteligencia Artificial</b> (Agencia de Transformación Digital y Telecomunicaciones, ATDT, abril de 2026) es la ruta de acción pública "
            "del Gobierno de México para aprovechar la IA con sentido estratégico, responsabilidad institucional y orientación social. Su punto de partida: "
            "<b>la tecnología debe estar al servicio de las personas y del interés público</b>."
            "<div class='mt-2 text-xs text-slate-600'>Contexto: según el Índice Latinoamericano de IA 2025 (CEPAL), México obtuvo 47.03 puntos, categoría “Adoptantes”, "
            "por encima del promedio regional (42.63); los “Pioneros” son Chile, Brasil y Uruguay.</div>"
        ),
        "derechos_titulo": "Los tres pilares del Plan",
        "derechos": [
            "<b>1. Marco ético y legal sólido:</b> lineamientos para el uso responsable de la IA en el sector público, mecanismos de <b>evaluación de impacto</b> y armonización normativa. Se propone expedir un <b>marco legal federal</b> de IA.",
            "<b>2. Capacidades, talento y software público:</b> el Centro Público de Formación en IA y la Fábrica de IA (consulta el tema <i>“Talento, Fábrica de IA y Coatlicue”</i>).",
            "<b>3. Infraestructura estratégica para la soberanía tecnológica:</b> supercómputo (Coatlicue) y una red nacional de centros de datos.",
        ],
        "pasos_titulo": "Marco legal y gobernanza que propone",
        "pasos": [
            "<b>Seis principios rectores</b> de la ley federal propuesta: transparencia y explicabilidad; licitud y uso ético; no discriminación; proporcionalidad; <b>supervisión humana efectiva</b>; y corresponsabilidad entre quienes desarrollan, distribuyen y usan la IA.",
            "<b>Tres elementos centrales:</b> <i>transparencia algorítmica</i> (sistemas que impactan la vida de las personas deben poder explicarse y auditarse); <i>responsabilidad pública</i> "
            "(cuando una decisión automatizada afecte derechos, deben existir vías para identificar responsables, impugnar, pedir revisión y reparar el daño); e <i>inclusión</i> (diversidad social, cultural, lingüística y territorial).",
            "<b>Arquitectura institucional prevista:</b> una función de <b>supervisión y vigilancia</b>; otra de <b>evaluación, designación y notificación</b> (acreditar, validar o certificar sistemas y actores obligados); y una de <b>protección de derechos</b>, "
            "con facultades para requerir información, investigar y actuar en defensa de las personas, sobre todo en usos de alto impacto. Las instituciones concretas se definirán conforme evolucione el marco normativo; la ATDT tendrá un papel central.",
            "<b>Estado actual:</b> el Plan propone la ley, pero la definición de derechos y obligaciones corresponde al proceso legislativo. Hasta donde se pudo verificar (nov. 2026) no hay una ley general de IA. <b>Verifica</b> avances.",
            "<b>Riesgos que reconoce</b> al adoptar IA en el sector público: respuestas incorrectas o discriminatorias, falta de integración con los sistemas existentes, baja calidad de los datos, ciberseguridad y desigualdad de capacidades entre niveles de gobierno.",
            "<b>Para tu proyecto:</b> este asistente es un agente conversacional informativo. Cumple varios criterios del Plan: se explica por reglas, <b>deriva a personas e instituciones</b>, cita su fundamento, "
            "<b>no guarda tus mensajes</b> y no usa IA generativa. El propio Plan cita como ejemplo de agente conversacional de atención ciudadana la <b>Ventanilla 24/7</b> de gob.mx.",
        ],
        "fundamento": "Plan Nacional de Inteligencia Artificial (ATDT, abril de 2026), secciones 1 a 5 y Conclusión; Programa de Normatividad de la IA.",
    },
    {
        "id": "ia_chapultepec",
        "titulo": "Principios de Chapultepec: ética de la IA en México",
        "emoji": "📜",
        "boton": "Principios de Chapultepec",
        "relacionados": ["ia_plan_nacional", "ia_derechos_humanos", "ia_requisitos", "ia_unesco"],
        "keywords": [
            ("principios de chapultepec", 13), ("chapultepec", 9), ("diez principios", 8), ("10 principios", 8),
            ("declaracion de etica de la ia", 9), ("marco etico de la ia en mexico", 10), ("marco etico oficial", 9),
            ("etica de la ia en mexico", 10), ("la ia debe ampliar derechos", 10), ("secihti", 7),
        ],
        "intro": (
            "Los <b>Principios de Chapultepec</b> se presentaron el <b>29 de enero de 2026</b> por la Secretaría de Ciencia, Humanidades, Tecnología e Innovación (SECIHTI) y la ATDT. "
            "Son el <b>primer marco ético oficial</b> del Gobierno de México para orientar el uso y desarrollo de la IA en el ámbito público. "
            "<b>No sustituyen</b> la regulación futura ni la política sectorial: fijan criterios comunes para que las instituciones diseñen, adopten, implementen y supervisen estas tecnologías."
        ),
        "derechos_titulo": "Los diez principios",
        "derechos": [
            "<b>1.</b> La IA debe ampliar derechos, nunca reducirlos.",
            "<b>2.</b> Toda decisión apoyada por IA debe tener responsables humanos.",
            "<b>3.</b> Si una decisión no puede explicarse, no debe automatizarse.",
            "<b>4.</b> La IA se gobierna mejor cuando se decide en colectivo.",
            "<b>5.</b> La IA solo es valiosa si genera bienestar para todas las personas.",
            "<b>6.</b> Antes de automatizar, hay que comprender a quién y a qué afecta.",
            "<b>7.</b> La tecnología estratégica debe responder a las necesidades del país.",
            "<b>8.</b> El desarrollo de la IA requiere fortalecer la educación y el conocimiento en el país.",
            "<b>9.</b> La IA no puede ser ajena a la diversidad cultural y lingüística del país.",
            "<b>10.</b> Los datos son un bien público que debe cuidarse con responsabilidad.",
        ],
        "pasos_titulo": "Cómo los explica el Plan Nacional de IA",
        "pasos": [
            "<b>Ampliar derechos:</b> la IA no debe limitar injustificadamente el acceso a servicios, beneficios, información o mecanismos de atención, ni convertir los sesgos existentes en nuevas formas de exclusión.",
            "<b>Responsabilidad humana:</b> debe quedar claro quién diseñó, implementa y supervisa la herramienta y quién responde por sus efectos; sin esa cadena, la IA debilita la rendición de cuentas.",
            "<b>Explicabilidad:</b> ninguna decisión pública relevante debe automatizarse si no puede explicarse de manera suficiente. Las instituciones deben comprender los criterios generales, los datos, los riesgos y las vías para revisar los resultados.",
            "<b>Comprender a quién afecta:</b> evaluar impactos diferenciados entre grupos, datos incompletos o sesgados, efectos en el acceso a servicios y costos ambientales.",
            "<b>Decisión colectiva:</b> diálogo entre el Estado, la academia, la industria, las comunidades técnicas, la sociedad civil y los grupos potencialmente afectados.",
            "<b>Bienestar:</b> una herramienta no es exitosa solo por reducir costos o acelerar procesos, sino por mejorar la calidad de los servicios y atender necesidades reales.",
            "<b>Datos:</b> cómo se recopilan, almacenan, procesan, comparten y protegen es una condición ética, política y jurídica de cualquier sistema público de IA.",
        ],
        "fundamento": "Principios de Chapultepec (SECIHTI y ATDT, 29-ene-2026), según los resume el Plan Nacional de Inteligencia Artificial (abril de 2026), sección 3. Son orientadores; verifica el texto oficial.",
    },
    {
        "id": "ia_plan_capacidades",
        "titulo": "Talento, Fábrica de IA y Coatlicue (Plan Nacional de IA)",
        "emoji": "🖥️",
        "boton": "Talento, Fábrica de IA y Coatlicue",
        "relacionados": ["ia_plan_nacional", "ia_chapultepec"],
        "keywords": [
            ("coatlicue", 13), ("supercomputadora", 10), ("supercomputo", 9), ("fabrica de ia", 13),
            ("centro publico de formacion en ia", 13), ("cpfia", 11), ("ventanilla 24 7", 11), ("ventanilla digital", 5),
            ("kuul", 9), ("semaforo aduanal", 10), ("soberania tecnologica", 8), ("centros de datos", 7),
            ("grafos contra factureras", 10), ("gestor inteligente de desastres", 10), ("software publico", 7),
        ],
        "intro": (
            "Los pilares 2 y 3 del <b>Plan Nacional de IA</b> buscan que el Estado desarrolle <b>capacidades propias</b>: talento, software público e infraestructura, para no ser un usuario pasivo de tecnologías ajenas."
        ),
        "derechos_titulo": "Pilar 2: talento y software público",
        "derechos": [
            "<b>Centro Público de Formación en IA (CPFIA):</b> formación <b>gratuita</b> para estudiantes de bachillerato y educación superior en IA, análisis de datos, programación en Java, cómputo en la nube y ciberseguridad, "
            "en un formato intensivo de <b>cinco meses</b>. Opera con 14 empresas (Accenture, AWS, Axity, Ericsson, Google, IBM, Kyndryl, Meta, Microsoft, Oracle, Salesforce, SAP, Softtek y TCS) y otorga <b>doble certificación</b>: "
            "de las empresas y de las autoridades educativas mexicanas. La primera generación tiene 10,000 estudiantes y se proyectan 25,000 certificaciones al año; la segunda generación se proyecta para el segundo semestre de 2026.",
            "<b>Fábrica de IA:</b> el motor de desarrollo de soluciones tecnológicas del gobierno, con 100 expertos; define metodologías, estándares y buenas prácticas para implementar IA en el sector público. "
            "Entre sus seis proyectos del primer año están el <b>Semáforo Aduanal</b> (ANAM), la <b>Ventanilla 24/7</b> de gob.mx, <b>Kuúl</b> (asistente turístico), OCR y clasificación de patentes (IMPI), "
            "el modelo de grafos contra factureras (SAT) y el Gestor Inteligente de Desastres.",
            "<b>Ventanilla 24/7:</b> agente conversacional que orienta a las personas para encontrar trámites federales; desde su lanzamiento el 9-ene-2026 ha alcanzado a más de 280,000 personas usuarias. "
            "<i>Dato útil para tu proyecto:</i> busca coincidencias <b>por significado</b> (representaciones semánticas), mientras que este asistente usa <b>reglas con palabras clave</b>: es una diferencia de diseño, no de objetivo.",
        ],
        "pasos_titulo": "Pilar 3: infraestructura y soberanía tecnológica",
        "pasos": [
            "<b>Coatlicue:</b> la primera supercomputadora pública del país (ATDT y SECIHTI), con inversión aproximada de <b>6,000 millones de pesos</b>, construcción desde enero de 2026, primera piedra en junio y 24 meses de implementación. "
            "Se desarrolla con el Barcelona Supercomputing Center; tendrá <b>314 petaflops</b> y 14,480 GPU, con sede en el campus Zacatenco del IPN (Ciudad de México), y sería unas siete veces más potente que la mayor de la región.",
            "<b>Acceso:</b> investigadores, universidades y centros de investigación del país y de América Latina; además, la industria podrá rentar tiempo de cómputo. Usos prioritarios: clima y desastres, agricultura, energía, análisis fiscal y aduanal, e investigación en salud, movilidad e IA.",
            "<b>Centros de datos:</b> una red nacional para consolidar los servicios digitales del gobierno federal en una nube soberana. El de <b>Aguascalientes</b> (nodo central, inversión de 7 millones de dólares) y el de <b>Tulancingo</b> (en habilitación).",
            "<i>Verifica</i> el avance de estas obras y cifras; son las del Plan de abril de 2026.",
        ],
        "fundamento": "Plan Nacional de Inteligencia Artificial (ATDT, abril de 2026), secciones 5.2 y 5.3.",
    },
]
