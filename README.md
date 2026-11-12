# Chatbot de Derechos Humanos – Facultad de Ingeniería UAEMéx

Asistente que explica derechos humanos, orienta ante situaciones concretas
("¿qué hago si…?") y entrega teléfonos de ayuda del Estado de México y de la UAEMéx.

## Estructura

```
app.py            Controlador Flask (rutas /, /chat, /health)
models.py         Motor: interpreta el mensaje y arma la respuesta
knowledge.py      TODO el contenido (temas, derechos, pasos, teléfonos, leyes)  <-- aquí editas
templates/        Interfaz web
test_chatbot.py   Pruebas automáticas (python test_chatbot.py)
requirements.txt  Dependencias      Procfile / render.yaml  Despliegue
```

## Temas que cubre (según el temario del proyecto)

| Tema del temario | Dónde está en el chatbot (`id` en `knowledge.py`) |
|---|---|
| Derechos como estudiante y los derechos "normales" | `derechos_estudiante` (derechos humanos + universitarios), `derechos_generales` |
| Informar bien cuáles son los derechos humanos | `que_son_dh`, `lista_dh` (resumen de los 30 artículos de la DUDH), `derechos_generales` |
| Protección de menores de edad | `proteccion_menores` (Ley de NNA del Edomex) |
| Números de emergencia si un menor es violentado | `emergencia_menores` (urgente), `donde_ayuda` |
| ¿Cómo saber si me discriminan? | `discriminacion_como_saber` (3 preguntas clave), `discriminacion` |
| ¿Qué hacer si me siento violentada por un profesor? | `violencia_docente`, `acoso_hostigamiento` |
| ¿Dónde puedo acudir para pedir ayuda? | `donde_ayuda` (directorio por situación) |
| Situaciones hipotéticas | `casos_practicos` + 6 casos (`caso_*`) |
| Ley Olimpia / violencia digital (Tema 9) | `ley_olimpia`, `violencia_digital`, `caso_foto_intima` |

## Cómo funciona (explicable y auditable)

1. Normaliza el texto (minúsculas, sin acentos).
2. Si detecta una **urgencia** (crisis emocional, peligro), responde eso primero.
3. Puntúa cada tema según las palabras clave que aparecen en el mensaje.
4. Responde con el tema de mayor puntaje y ofrece temas cercanos como botones.
5. Si no entiende, **lo dice** y ofrece un menú. No inventa respuestas.

## Ejecutar en tu computadora

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py                    # abre http://localhost:5001
python test_chatbot.py           # pruebas
```

## Agregar un tema nuevo

Copia un bloque de `TOPICS` en `knowledge.py`, cambia `id`, `titulo`, `keywords`,
`derechos`, `pasos`, `contactos` y `fundamento`. Las palabras clave van **sin acentos**.
Campos opcionales: `derechos_titulo` y `pasos_titulo` (cambian los encabezados),
`relacionados` (botones que se ofrecen al final) y `urgente_min` (puntaje mínimo para que
un tema urgente se active; úsalo para que no salte en preguntas informativas).
Luego agrega 1-2 casos a `test_chatbot.py` y córrelo.

## Publicarlo GRATIS con un enlace (Render)

1. Sube el proyecto a GitHub (**sin** la carpeta `.venv`; el `.gitignore` ya la excluye).
2. Entra a https://render.com y crea cuenta con tu GitHub.
3. **New +  →  Web Service** → elige tu repositorio.
4. Configura: Runtime `Python 3`, Build `pip install -r requirements.txt`,
   Start `gunicorn app:app`, Instance Type **Free**.
5. **Create Web Service**. En unos minutos tendrás un enlace `https://tu-nombre.onrender.com`.

Limitación del plan gratuito: la app "se duerme" tras ~15 min sin visitas y la
primera visita después tarda cerca de 1 minuto en despertar. Abre el enlace unos
minutos antes de tu exposición.

## Conexión con conceptos de normatividad en IA (para tu documento)

| Concepto | Cómo lo aplica este proyecto |
|---|---|
| Transparencia | Se identifica como asistente automatizado; cada respuesta cita su fundamento legal. |
| Explicabilidad | Motor por reglas: siempre se puede rastrear por qué dio una respuesta. |
| Privacidad / minimización de datos | No guarda ni registra mensajes; no los envía a terceros. |
| Exactitud y no alucinación | Solo responde con contenido curado y verificado; si no sabe, lo dice. |
| Supervisión humana / escalamiento | Deriva a personas e instituciones (911, CODHEM, Línea Sin Violencia, Defensoría). |
| Seguridad de usuarios vulnerables | Protocolo prioritario para crisis emocional y peligro. |
| No discriminación | Lenguaje incluyente y contenido sobre igualdad y no discriminación. |
| Límites de uso | Aviso de que no sustituye asesoría legal profesional. |

## Pendiente por verificar antes de entregar

- `uaemex_general` (722 226 2300) viene de tu versión original: confírmalo con la Facultad.
- Datos de contacto de la **Defensoría de los Derechos Universitarios de la UAEMéx**
  (no encontré teléfono oficial público; agrégalo en `CONTACTS["defensoria_uaemex"]`).
- `procuraduria_nna` (Procuraduría de Protección de NNA / DIF) y `conapred`: no incluyen teléfono porque
  no pude confirmarlo en fuente oficial. Agrégalo en `CONTACTS`.
- **Ley de Protección de Datos Personales del Edomex:** el PDF que adjuntaste indica que la ley de 2017 fue
  **abrogada** por el Decreto 365 (1 de octubre de 2026). Por eso `privacidad_datos` ya no cita esa ley por nombre.
  Confirma cuál es la norma vigente y si el **INFOEM** sigue siendo el órgano garante (contacto `infoem`).
- Sanciones de Ley Olimpia: vienen de la ficha técnica que adjuntaste (Edomex, Arts. 211 Ter y 211 Quater).
  Confírmalas en el Código Penal vigente.
- URLs nuevas en `SOURCES` (legislación del Edomex y Ley General de Acceso de las Mujeres): compruébalas.
- Revisa teléfonos y artículos citados antes de la exposición: los números cambian.
- Pide a alguien con formación jurídica (tu profesor/a) que revise `knowledge.py`.
