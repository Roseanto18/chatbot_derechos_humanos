import os
import re
import unicodedata
from google import genai
from google.genai import types
import knowledge as kb

MIN_SCORE = 3          # puntaje mínimo para considerar que se entendió un tema
URGENT_MIN_SCORE = 3   # puntaje mínimo para activar un tema urgente
CLOSE_RATIO = 0.6      # otros temas con >= 60 % del puntaje mayor se sugieren como botones

DISCLAIMER = (
    "<span class='text-xs text-slate-500'>Asistente con orientación en derechos humanos y IA: esta información es orientativa "
    "y no sustituye la asesoría de un profesional del derecho.</span>"
)

LINK_CLASS = "text-emerald-700 underline font-semibold hover:text-emerald-900"


def normalize(text: str) -> str:
    """minúsculas, sin acentos/ñ, sin signos, espacios simples."""
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _keyword_hit(keyword: str, norm_text: str, tokens: list) -> bool:
    if " " in keyword:  # frase: debe aparecer completa y empezar en límite de palabra
        return (" " + keyword) in (" " + norm_text)
    if keyword.endswith("$"):  # palabra exacta
        return keyword[:-1] in tokens
    return any(tok.startswith(keyword) for tok in tokens)  # prefijo


class ChatbotModel:
    def __init__(self):
        self.topics = {t["id"]: t for t in kb.TOPICS}
        # Inicializar el cliente de Gemini de forma segura con la variable de entorno de Render
        api_key = os.environ.get("GEMINI_API_KEY")
        self.client = genai.Client(api_key=api_key) if api_key else None

    # ------------------------------------------------------------------ API pública
    def menu(self):
        """Botones rápidos iniciales: [{'id':..., 'label':...}]"""
        return [{"id": i, "label": self._button_label(self.topics[i])} for i in kb.MENU_IDS]

    def get_response(self, user_message: str, topic_id: str = None) -> dict:
        """Devuelve {'html': str, 'suggestions': [{'id','label'}], 'topic': id|None}."""
        # Botón rápido: respuesta directa y determinista
        if topic_id:
            if topic_id in self.topics:
                return self._answer(topic_id, extra=[])
            if topic_id == "fuentes":
                return self._sources()

        norm = normalize(user_message or "")
        if not norm:
            return self._welcome()
        tokens = norm.split()

        scores = {tid: self._score(t, norm, tokens) for tid, t in self.topics.items()}

        # 1) Urgencias primero (Prioridad absoluta por seguridad)
        urgent = [(s, tid) for tid, s in scores.items()
                  if self.topics[tid].get("urgente")
                  and s >= self.topics[tid].get("urgente_min", URGENT_MIN_SCORE)]
        if urgent:
            urgent.sort(reverse=True)
            return self._answer(urgent[0][1], extra=[])

        # 2) Fuentes / leyes
        src_score = sum(w for kw, w in kb.SOURCES_KEYWORDS if _keyword_hit(kw, norm, tokens))
        best_tid, best = max(scores.items(), key=lambda kv: kv[1])
        if src_score >= MIN_SCORE and src_score >= best:
            return self._sources()

        # 3) Tema con mejor puntaje local
        if best >= MIN_SCORE:
            extra = [tid for tid, s in sorted(scores.items(), key=lambda kv: -kv[1])
                     if tid != best_tid and s >= MIN_SCORE and s >= best * CLOSE_RATIO][:2]
            return self._answer(best_tid, extra=extra)

        # 4) Saludos / agradecimientos
        if any(_keyword_hit(g, norm, tokens) for g in kb.GREETING_WORDS):
            return self._welcome()
        if any(_keyword_hit(g, norm, tokens) for g in kb.THANKS_WORDS):
            return {"html": "¡Con gusto! 💚 Si necesitas algo más, aquí estoy. "
                            "Si es una emergencia, recuerda que el <b>911</b> está disponible las 24 h.",
                    "suggestions": [], "topic": None}

        # 5) SI NINGUNA REGLA LOCAL COINCIDE: ¡Mandamos la pregunta a Gemini con búsqueda web y aviso!
        if self.client:
            try:
                contexto_general = "\n".join([f"- {t['titulo']}: {t.get('fundamento', '')}" for t in self.topics.values() if t.get('fundamento')])
                
                system_instruction = (
                    "Eres el asistente virtual oficial de derechos humanos de la Facultad de Ingeniería de la UAEMéx. "
                    "Tu labor es orientar de forma empática, clara y formal sobre derechos humanos, normatividad y protocolos institucionales. "
                    "Básate en el siguiente marco institucional y utiliza la herramienta de búsqueda web en tiempo real si el usuario pregunta por temas externos, noticias o datos actualizados. "
                    "Reglas estrictas: "
                    "1. Nunca des asesoría jurídica formal ni actúes como abogado. "
                    "2. Si hay riesgo o peligro inminente, indica inmediatamente que llamen al 911 o a la CODHEM (800 999 4000). "
                    "3. Mantén un tono respetuoso, accesible y neutral.\n\n"
                    f"Contexto institucional:\n{contexto_general}"
                )

                response = self.client.models.generate_content(
                    model='gemini-2.0-flash',
                    contents=user_message,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        tools=[{"google_search": {}}],
                        temperature=0.3
                    )
                )
                
                # Agregamos un aviso visible indicando que la respuesta viene de la IA
                aviso_ia = "<div class='mb-2 text-xs font-semibold text-indigo-700 bg-indigo-50 p-2 rounded'>🤖 Respuesta generada con IA y búsqueda web en tiempo real:</div>"
                html_resp = f"{aviso_ia}<div class='mt-1'>{response.text.replace('\n', '<br>')}</div><div class='mt-3'>{DISCLAIMER}</div>"
                
                suggestions = [{"id": i["id"], "label": i["label"]} for i in self.menu()[:3]]
                return {"html": html_resp, "suggestions": suggestions, "topic": None}
            except Exception as e:
                print(f"Error con Gemini: {e}")

        # 6) Fallback estricto solo si fallara la API
        return self._fallback()


    # ------------------------------------------------------------------ internos
    @staticmethod
    def _score(topic, norm, tokens) -> int:
        return sum(w for kw, w in topic["keywords"] if _keyword_hit(kw, norm, tokens))

    @staticmethod
    def _button_label(topic) -> str:
        return topic.get("boton") or topic["titulo"]

    def _suggestions(self, ids):
        out = []
        for i in ids:
            if i == "fuentes":  # tema especial (no está en TOPICS)
                out.append({"id": "fuentes", "label": "Fuentes de información"})
            else:
                out.append({"id": i, "label": self._button_label(self.topics[i])})
        return out

    # --- contactos
    @staticmethod
    def _contact_html(cid: str) -> str:
        c = kb.CONTACTS[cid]
        parts = []
        if c.get("url"):
            parts.append(f"<a href='{c['url']}' target='_blank' rel='noopener noreferrer' class='{LINK_CLASS}'>{c['name']}</a>")
        else:
            parts.append(f"<b>{c['name']}</b>")
        phones = []
        for key in ("phone", "phone2", "phone3", "phone4"):
            if c.get(key):
                digits = re.sub(r"[^0-9]", "", c[key])
                phones.append(f"<a href='tel:{digits}' class='{LINK_CLASS}'>{c[key]}</a>")
        if phones:
            parts.append(" · 📞 " + " / ".join(phones))
        if c.get("note"):
            parts.append(f"<br><span class='text-xs text-slate-600'>{c['note']}</span>")
        return "".join(parts)

    # --- respuestas
    def _answer(self, tid: str, extra: list) -> dict:
        t = self.topics[tid]
        h = [f"{t['emoji']} <b>{t['titulo']}</b>"]
        if t.get("intro"):
            h.append(f"<div class='mt-2'>{t['intro']}</div>")
        if t.get("derechos"):
            items = "".join(f"<li>{x}</li>" for x in t["derechos"])
            h.append(f"<div class='mt-3 font-semibold'>{t.get('derechos_titulo', 'Tus derechos')}</div><ul class='list-disc pl-5 space-y-1'>{items}</ul>")
        if t.get("pasos"):
            items = "".join(f"<li>{x}</li>" for x in t["pasos"])
            h.append(f"<div class='mt-3 font-semibold'>{t.get('pasos_titulo', 'Qué puedes hacer')}</div><ol class='list-decimal pl-5 space-y-1'>{items}</ol>")
        if t.get("contactos"):
            items = "".join(f"<li>{self._contact_html(c)}</li>" for c in t["contactos"])
            h.append(f"<div class='mt-3 font-semibold'>A dónde acudir</div><ul class='space-y-2 mt-1'>{items}</ul>")
        if t.get("fundamento"):
            h.append(f"<div class='mt-3 text-xs italic text-slate-600'>Fundamento: {t['fundamento']}</div>")
        h.append(f"<div class='mt-2'>{DISCLAIMER}</div>")
        extra = extra or t.get("relacionados", [])
        return {"html": "".join(h), "suggestions": self._suggestions(extra), "topic": tid}

    def _sources(self) -> dict:
        items = "".join(
            f"<li><a href='{s['url']}' target='_blank' rel='noopener noreferrer' class='{LINK_CLASS}'>{s['name']}</a></li>"
            for s in kb.SOURCES)
        html = (f"📚 <b>Fuentes oficiales de información</b><ul class='mt-2 list-disc pl-5 space-y-1'>{items}</ul>"
                f"<div class='mt-3 text-sm'>Para ver <b>de dónde salió cada tema</b>, las versiones consultadas y lo que <b>falta verificar</b>, "
                f"abre la página <a href='/fuentes' target='_blank' class='{LINK_CLASS}'>Fuentes y base de conocimientos</a>.</div>")
        return {"html": html, "suggestions": [], "topic": "fuentes"}

    def _welcome(self) -> dict:
        html = (
            "Hola, soy el <b>asistente de derechos humanos de la Facultad de Ingeniería UAEMéx</b>. "
            "Puedo explicarte tus derechos, decirte <b>qué hacer ante una situación</b> y darte los "
            "teléfonos de ayuda del Estado de México y de la universidad.<br><br>"
            "Cuéntame qué te pasó con tus palabras (por ejemplo: <i>\"un profesor me acosa\"</i> o "
            "<i>\"me detuvo la policía\"</i>), o elige una opción:"
            "<div class='mt-2 text-xs text-slate-500'>Si estás en peligro, llama al <b>911</b>.</div>"
        )
        return {"html": html, "suggestions": [], "topic": None}

    def _fallback(self) -> dict:
        html = (
            "No estoy seguro de haber entendido tu situación, y prefiero no darte información equivocada. "
            "¿Podrías contarme un poco más? Por ejemplo, <i>qué pasó, dónde y quién estuvo involucrado</i>. "
            "También puedes elegir uno de estos temas.<br><br>"
            "<span class='text-xs text-slate-500'>Si estás en peligro, llama al <b>911</b>. "
            "Para hablar con una persona: CODHEM 800 999 4000 (24 h).</span>"
        )
        return {"html": html, "suggestions": [{"id": i["id"], "label": i["label"]} for i in self.menu()], "topic": None}
