# Chatbot de Derechos Humanos – Facultad de Ingeniería UAEMéx

Asistente que explica derechos humanos, orienta ante situaciones concretas
("¿qué hago si…?") y entrega teléfonos de ayuda del Estado de México y de la UAEMéx.

## Estructura

```
app.py            Controlador Flask (rutas /, /chat, /health)
models.py         Motor: interpreta el mensaje y arma la respuesta
knowledge.py      Contenido base (temas, derechos, pasos, teléfonos, leyes)  <-- aquí editas
knowledge_unidades.py  Contenido v5: preguntas frecuentes + Unidades 3 y 4 del temario (se suma a knowledge.py)
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
- **Ley de Protección de Datos Personales del Edomex:** el texto que adjuntaste es el de 2017 (sin reformas). Confirma cuál es la norma vigente y si el **INFOEM** sigue siendo el órgano garante (contacto `infoem`).
- Sanciones de Ley Olimpia: vienen de la ficha técnica que adjuntaste (Edomex, Arts. 211 Ter y 211 Quater).
  Confírmalas en el Código Penal vigente.
- URLs nuevas en `SOURCES` (legislación del Edomex y Ley General de Acceso de las Mujeres): compruébalas.
- Revisa teléfonos y artículos citados antes de la exposición: los números cambian.
- Pide a alguien con formación jurídica (tu profesor/a) que revise `knowledge.py`.


## Ampliación v3 (14-nov-2026)
Temas nuevos: violencia contra las mujeres (ley general + ley del Edomex + Código Civil), violentómetro (IPN, incl. laboral),
abuso laboral (NOM-035, Convenio 190), protección de datos personales (LFPDPPP 2025), persona vs. animal,
IA y derechos humanos (requisitos, alto riesgo, EE. UU. vs. UE, cumplimiento), "otros temas" y 4 casos prácticos nuevos.
Páginas nuevas/ampliadas: `/privacidad` (aviso integral) y `/fuentes` (de dónde salió la base de conocimientos; la tabla tema→fundamento se genera sola desde `knowledge.py`).
Antes de entregar: llena `[NOMBRE DEL EQUIPO O ESTUDIANTE]` y `[CORREO DE CONTACTO]` en `templates/privacidad.html` y `templates/fuentes.html`, y resuelve el `[CONFIRMAR]` de la sección 6 de fuentes.
Pruebas: `python test_chatbot.py` (94 casos en v3; 103 desde v4).

## Ampliación v4 (15-nov-2026)
Temas nuevos: `datos_y_derechos_humanos` (datos personales y derechos humanos: CPEUM Arts. 6 y 16, ley estatal de 2017, UNESCO y NIST),
`ia_unesco` (Recomendación de la UNESCO sobre la ética de la IA, 2021) e `ia_nist_rmf` (NIST AI RMF 1.0).
Temas ampliados: `privacidad_datos` (instituciones públicas del Edomex), `ia_requisitos` (UNESCO y NIST), `ia_eeuu_vs_ue` (fila y bloque del NIST AI RMF) e `ia_cumplimiento`.
Fuentes y página `/fuentes` actualizadas. Pruebas: `python test_chatbot.py` (103 casos).
Pendiente de verificar: vigencia de la ley estatal de datos personales (el texto usado es de 2017; hay leyes nuevas aprobadas por el Congreso del Edomex).

### Ajuste (15-nov-2026): personas vs. animales
`persona_vs_animal` se reescribió con tabla comparativa y base en la Constitución (Arts. 1°, 3°, 4° párr. sexto y 73 XXIX-G), la Declaración Universal (Arts. 1, 2, 6, 7, 8 y 29) y la LGEEPA (Arts. 79 y 87 Bis 2). Pruebas: 107 casos.
Pendiente de verificar: la Ley General de Bienestar, Cuidado y Protección de los Animales (aprobada por el Senado, falta Diputados según prensa) y la ley estatal de bienestar animal del Edomex (aprobada en abril de 2026 según prensa).


## Ampliación v5 (15-nov-2026): preguntas frecuentes y Unidades 3 y 4 del temario
Nuevo archivo `knowledge_unidades.py` (se importa al final de `knowledge.py`). Total: 68 temas, 166 pruebas (`python test_chatbot.py`).

**Preguntas que ahora responde correctamente**

| Pregunta del usuario | Tema (`id`) |
|---|---|
| ¿Qué son los derechos humanos? / ¿Cuáles son mis derechos? | `que_son_dh` / `derechos_generales` |
| ¿Mis derechos son los mismos que los de un animal? | `persona_vs_animal` (ahora abre con "No son los mismos…") |
| ¿Cómo sé si estoy siendo víctima de acoso? | `acoso_como_saber` (4 preguntas clave, señales y tipos) |
| ¿Cómo sé si sufro abuso laboral? | `abuso_laboral_como_saber` (4 áreas + prueba rápida) |
| ¿Quién creó los derechos o quién me los dio? | `origen_dh` (reconocidos, no otorgados; línea del tiempo; reforma de 2011) |
| ¿Qué deben seguir los modelos de IA para no vulnerar los derechos humanos? | `ia_requisitos` |
| ¿Cómo sé si un sistema de IA vulnera derechos humanos? | `ia_detectar_vulneracion` (8 señales de alerta, prueba comparativa y qué hacer) |
| Diferencia entre la Unión Europea y Estados Unidos | `ia_eeuu_vs_ue` (tabla comparativa) |

**Cobertura del temario**

| Subtema | Tema (`id`) |
|---|---|
| U3 – índice | `unidad3_hub` |
| 3.1.1 y 3.1.2 UE: modelo de derechos, RGPD | `ue_modelo_rgpd` |
| 3.1.3 AI Act | `ue_ai_act` (+ `ia_alto_riesgo`, `ia_requisitos`) |
| 3.1.4 DSA y DMA | `ue_dsa_dma` |
| 3.2.1 y 3.2.2 EE. UU.: modelo y Blueprint for an AI Bill of Rights | `eeuu_blueprint` |
| 3.2.3 NIST AI RMF | `ia_nist_rmf` |
| 3.3.1 y 3.3.3 OCDE y GPAI | `ocde_gpai` |
| 3.3.2 UNESCO | `ia_unesco` |
| 3.4 Estrategias latinoamericanas | `latam_ia` |
| U4 – índice | `unidad4_hub` |
| 4.1.1 Privacidad y datos | `datos_y_derechos_humanos`, `privacidad_datos` |
| 4.1.2 No discriminación y sesgos | `ia_sesgos` |
| 4.1.3 Libertad de expresión y contenido generado por IA | `ia_libertad_expresion` |
| 4.2.1 y 4.2.2 Responsabilidad civil y penal | `ia_responsabilidad` |
| 4.3.1 y 4.3.2 Salud y finanzas | `ia_salud_finanzas` |
| 4.3.3 y 4.3.4 Seguridad pública, educación y empleo | `ia_seguridad_educacion_empleo` |
| 4.4.1 Algoritmos de alto riesgo | `ia_alto_riesgo` |
| 4.4.2 IA generativa | `ia_generativa` |
| 4.4.3 y 4.4.4 Vehículos autónomos, robots y sistemas autónomos | `ia_vehiculos_robots` |

El menú inicial incluye los botones "Unidad 3" y "Unidad 4". También se agregaron contactos (`condusef`, `cofepris`) y fuentes nuevas.

**Pendiente de verificar antes de entregar (datos que cambian)**
- Estado de leyes en trámite: PL 2338/2023 de Brasil (Cámara de Diputados), proyecto de ley de Chile, iniciativas de IA en México, reglamento de Perú (vigencia desde enero de 2026 según fuentes consultadas).
- Calendario del AI Act tras el *Digital Omnibus* (el acuerdo es de mayo de 2026; confirma el texto final publicado) y plazo de la Directiva (UE) 2024/2853 (9-dic-2026).
- Marcadas como "verifica" en las respuestas: la regulación mexicana de IA médica (COFEPRIS), reconocimiento facial y vehículos autónomos; casos judiciales y multas citados (Clearview AI, OpenAI, *Thaler v. Perlmutter*).
- Artículos del Código Civil Federal (1910, 1913, 1916, 1924), CNPP Art. 421 y LFT Arts. 87 y 133: confírmalos en el texto vigente.
- Pide a tu profesor/a que revise `knowledge_unidades.py`.
