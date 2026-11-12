"""
MODELO DEL CHATBOT
==================
Motor de orientación basado en reglas y una base de conocimiento curada.

Cómo decide qué responder:
  1. Normaliza el texto (minúsculas, sin acentos, sin signos).
  2. Revisa si hay una señal de URGENCIA (crisis emocional / peligro). Si la hay, esa respuesta va primero.
  3. Puntúa cada tema según las palabras clave que aparecen en el mensaje.
  4. Responde con el tema de mayor puntaje; si hay otros cercanos, los ofrece como botones.
  5. Si no entiende, lo dice con transparencia y ofrece el menú (nunca inventa).

Ventaja para un proyecto de normatividad en IA: es 100% explicable y auditable.
Cada respuesta sale de contenido que tú revisaste, con su fundamento legal, y no se
envían los mensajes de las personas a ningún servicio externo.
"""
import re
import unicodedata

import knowledge as kb

MIN_SCORE = 3          # puntaje mínimo para considerar que se entendió un tema
URGENT_MIN_SCORE = 3   # puntaje mínimo para activar un tema urgente
CLOSE_RATIO = 0.6      # otros temas con >= 60 % del puntaje mayor se sugieren como botones

DISCLAIMER = (
    "<span class='text-xs text-slate-500'>Soy un asistente automatizado: esta información es orientativa "
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

        # 1) Urgencias primero
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

        # 3) Tema con mejor puntaje
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

        # 5) No se entendió: honesto y con salida
        return self._fallback()

    # ------------------------------------------------------------------ internos
    @staticmethod
    def _score(topic, norm, tokens) -> int:
        return sum(w for kw, w in topic["keywords"] if _keyword_hit(kw, norm, tokens))

    @staticmethod
    def _button_label(topic) -> str:
        return topic.get("boton") or topic["titulo"]

    def _suggestions(self, ids):
        return [{"id": i, "label": self._button_label(self.topics[i])} for i in ids]

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
        for key in ("phone", "phone2"):
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
        html = f"📚 <b>Fuentes oficiales de información</b><ul class='mt-2 list-disc pl-5 space-y-1'>{items}</ul>"
        return {"html": html, "suggestions": [], "topic": "fuentes"}

    def _welcome(self) -> dict:
        html = (
            "Hola, soy el <b>asistente de derechos humanos de la Facultad de Ingeniería UAEMéx</b>. "
            "Puedo explicarte tus derechos, decirte <b>qué hacer ante una situación</b> y darte los "
            "teléfonos de ayuda del Estado de México y de la universidad.<br><br>"
            "Cuéntame qué te pasó con tus palabras (por ejemplo: <i>\"un profesor me acosa\"</i> o "
            "<i>\"me detuvo la policía\"</i>), o elige una opción:"
            "<div class='mt-2 text-xs text-slate-500'>No guardo tus mensajes. Si estás en peligro, llama al <b>911</b>.</div>"
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
