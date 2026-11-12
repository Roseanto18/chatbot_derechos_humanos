"""Pruebas rápidas: python test_chatbot.py
Cada caso es (mensaje del usuario, tema esperado). Sirve como evidencia de pruebas
para tu proyecto y para no romper nada cuando edites knowledge.py."""
from models import ChatbotModel

CASES = [
    ("¿Cuáles son mis derechos humanos?", "derechos_generales"),
    ("cuales son mis derechos", "derechos_generales"),
    ("Mi profesor me acosa y me manda mensajes", "acoso_hostigamiento"),
    ("un compañero me tocó sin mi permiso", "acoso_hostigamiento"),
    ("me discriminan en mi salón por ser indígena", "discriminacion"),
    ("me detuvo la policía y me pidieron dinero", "detencion_policia"),
    ("me asaltaron afuera de la facultad", "victima_delito"),
    ("difundieron mis fotos íntimas", "violencia_digital"),
    ("tengo mucha ansiedad por los exámenes", "salud_mental"),
    ("mi novio me pega", "violencia_pareja_familia"),
    ("quiero morir", "crisis_emocional"),
    ("ya no quiero vivir", "crisis_emocional"),
    ("auxilio me persiguen", "emergencia"),
    ("el maestro me reprobó injustamente, quiero revisión de examen", "derechos_estudiante"),
    ("quiero ejercer mis derechos ARCO sobre mis datos personales", "privacidad_datos"),
    ("me ofrecieron un trabajo y no me dejan salir, me quitaron mis documentos", "trata"),
    ("tengo un amigo policía", None),
    ("me siento solo", "salud_mental"),
    ("mi maestro me humilla enfrente de todos", "violencia_docente"),
    ("mi profesor me amenaza con reprobarme", "violencia_docente"),
    ("me amenazan por whatsapp", "victima_delito"),
    ("amenazas de muerte", "emergencia"),
    ("me paró la policía", "detencion_policia"),
    ("el teléfono de la facultad", "uaemex_servicios"),
    ("¿Qué son los derechos humanos?", "que_son_dh"),
    ("para qué sirven los derechos humanos", "que_son_dh"),
    ("quién creó los derechos humanos", "que_son_dh"),
    ("qué es la CODHEM", "glosario_instituciones"),
    ("cómo presento una queja", "glosario_instituciones"),
    ("qué es un derecho universitario", "glosario_instituciones"),
    ("fuentes", "fuentes"),
    ("¿guardas mis mensajes?", "privacidad_bot"),
    ("qué datos guardas", "privacidad_bot"),
    # ---- ampliación del temario
    ("¿Cuáles son mis derechos como estudiante y los normales?", "derechos_estudiante"),
    ("derechos de los estudiantes", "derechos_estudiante"),
    ("hay una diferencia entre mis derechos de estudiante a como ciudadano", "estudiante_vs_ciudadano"),
    ("¿qué derechos tengo como ciudadana?", "estudiante_vs_ciudadano"),
    ("diferencia entre derechos humanos y derechos de estudiante", "estudiante_vs_ciudadano"),
    ("protección de menores de edad", "proteccion_menores"),
    ("¿cuáles son los derechos de los niños?", "proteccion_menores"),
    ("qué es el interés superior de la niñez", "proteccion_menores"),
    ("números de emergencia si un menor de edad es violentado", "emergencia_menores"),
    ("mi primo de 9 años dice que su papá le pega", "emergencia_menores"),
    ("sospecho maltrato infantil en mi vecina", "emergencia_menores"),
    ("soy menor de edad y me golpean", "emergencia_menores"),
    ("informar cuáles son los derechos humanos", "lista_dh"),
    ("¿cuáles son los derechos humanos?", "lista_dh"),
    ("explícame la declaración universal", "lista_dh"),
    ("¿Cómo saber si me discriminan?", "discriminacion_como_saber"),
    ("qué es la discriminación", "discriminacion_como_saber"),
    ("ejemplos de discriminación", "discriminacion_como_saber"),
    ("¿Qué hacer si me siento violentada por un profesor?", "violencia_docente"),
    ("un profesor me grita y me insulta", "violencia_docente"),
    ("mi profesor me acosa", "acoso_hostigamiento"),
    ("¿Dónde puedo acudir para pedir ayuda?", "donde_ayuda"),
    ("quién me puede ayudar", "donde_ayuda"),
    ("teléfonos de ayuda", "donde_ayuda"),
    ("necesito ayuda", "donde_ayuda"),
    ("qué es la ley olimpia", "ley_olimpia"),
    ("sanciones de la ley olimpia", "ley_olimpia"),
    ("qué es el ciberacoso", "ley_olimpia"),
    ("me aplica la ley olimpia, difundieron mis fotos", "violencia_digital"),
    ("hicieron un deepfake mío", "violencia_digital"),
    ("dame un ejemplo", "casos_practicos"),
    ("situaciones hipotéticas", "casos_practicos"),
    ("quiero practicar con casos prácticos", "casos_practicos"),
    ("números de emergencia", "emergencia"),
    ("el profesor me toca sin permiso", "acoso_hostigamiento"),
    ("un niño de mi salón sufre bullying", "proteccion_menores"),
    ("mi hijo está triste", "salud_mental"),
    ("hola", None),
    ("asdfgh qwerty", None),
]

m = ChatbotModel()
fails = 0
for msg, expected in CASES:
    got = m.get_response(msg)["topic"]
    ok = got == expected
    fails += not ok
    print(("OK  " if ok else "FAIL"), f"{msg!r:75} -> {got}  (esperado: {expected})")
print(f"\n{len(CASES)-fails}/{len(CASES)} correctos")
raise SystemExit(1 if fails else 0)
