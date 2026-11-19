import os
import re
import unicodedata
from groq import Groq
import knowledge as kb

MIN_SCORE = 12         # solo dispara ficha estática si hay coincidencia muy fuerte
URGENT_MIN_SCORE = 3   # puntaje mínimo para activar un tema urgente
CLOSE_RATIO = 0.6      # otros temas con >= 60 % del puntaje mayor se sugieren como botones

DISCLAIMER = (
    "<span class='text-xs text-slate-500'>Asistente automatizado de orientación en derechos humanos e IA: "
    "esta información es solo de referencia, <b>puede contener errores</b> y no sustituye la asesoría de un "
    "profesional del derecho. Verifica siempre los datos y contactos en fuentes oficiales.</span>"
)

LINK_CLASS = "text-emerald-700 underline font-semibold hover:text-emerald-900"

STOPWORDS = {
    "el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", "al",
    "a", "en", "con", "por", "para", "sin", "sobre", "entre", "hasta", "desde",
    "y", "o", "u", "e", "ni", "que", "cual", "cuales", "quien", "quienes", "como",
    "cuando", "donde", "cuanto", "cuanta", "es", "son", "ser", "esta", "estan",
    "estar", "hay", "tiene", "tienen", "tener", "hacer", "hace", "puede", "pueden",
    "mi", "mis", "tu", "tus", "su", "sus", "me", "te", "se", "nos", "le", "les",
    "lo", "si", "no", "mas", "muy", "ya", "tambien", "pero", "porque", "asi",
}


def normalize(text: str) -> str:
    """minúsculas, sin acentos/ñ, sin signos, espacios simples."""
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def strip_html(text: str) -> str:
    """Elimina etiquetas HTML para pasar texto limpio al contexto de la IA."""
    clean = re.sub(r"<[^>]+>", " ", text or "")
    return re.sub(r"\s+", " ", clean).strip()


def _keyword_hit(keyword: str, norm_text: str, tokens: list) -> bool:
    if " " in keyword:  # frase: debe aparecer completa y empezar en límite de palabra
        return (" " + keyword) in (" " + norm_text)
    if keyword.endswith("$"):  # palabra exacta
        return keyword[:-1] in tokens
    return any(tok.startswith(keyword) for tok in tokens)  # prefijo


class ChatbotModel:
    def __init__(self):
        self.topics = {t["id"]: t for t in kb.TOPICS}
        api_key = os.environ.get("GROQ_API_KEY")
        self.client = Groq(api_key=api_key) if api_key else None
        self._search_index = self._build_search_index()

    def _build_search_index(self) -> dict:
        """Indexa el texto completo de todos los temas (knowledge + unidades + v6) para RAG local."""
        index = {}
        for tid, t in self.topics.items():
            if tid == "mas_temas":
                continue
            titulo_norm = normalize(t.get("titulo", ""))
            cuerpo_raw = " ".join([
                t.get("intro", ""),
                " ".join(t.get("derechos", [])),
                " ".join(t.get("pasos", [])),
                t.get("fundamento", ""),
            ])
            cuerpo_norm = normalize(strip_html(cuerpo_raw))
            kw_norm = " ".join(kw.rstrip("$") for kw, _ in t.get("keywords", []))
            index[tid] = {
                "titulo_tokens": set(titulo_norm.split()) - STOPWORDS,
                "kw_tokens": set(kw_norm.split()) - STOPWORDS,
                "cuerpo_tokens": set(cuerpo_norm.split()) - STOPWORDS,
            }
        return index

    def _retrieve_relevant_topics(self, norm_query: str, keyword_scores: dict, top_k: int = 3) -> list:
        """Recupera los temas más relevantes combinando keywords + coincidencia de texto completo."""
        q_tokens = [tok for tok in norm_query.split() if len(tok) > 2 and tok not in STOPWORDS]
        if not q_tokens:
            return []

        ranked = []
        for tid, idx in self._search_index.items():
            score = float(keyword_scores.get(tid, 0))
            for qt in q_tokens:
                if any(tt.startswith(qt) or qt.startswith(tt) for tt in idx["titulo_tokens"] if len(tt) > 2):
                    score += 3.5
                if any(kt.startswith(qt) or qt.startswith(kt) for kt in idx["kw_tokens"] if len(kt) > 2):
                    score += 2.5
                if any(ct.startswith(qt) for ct in idx["cuerpo_tokens"]):
                    score += 1.0
            if score > 0:
                ranked.append((score, tid))

        ranked.sort(reverse=True)
        return [tid for _, tid in ranked[:top_k]]

    def _format_topic_for_rag(self, tid: str) -> str:
        """Formatea una ficha de knowledge en texto limpio y compacto para el prompt de Groq."""
        t = self.topics[tid]
        partes = [f"### FICHA: {t['titulo']}"]
        if t.get("intro"):
            partes.append(f"Resumen: {strip_html(t['intro'])}")
        if t.get("derechos"):
            derechos_limpios = [strip_html(d) for d in t["derechos"][:5]]
            partes.append(f"{t.get('derechos_titulo', 'Puntos clave')}: " + " | ".join(derechos_limpios))
        if t.get("pasos"):
            pasos_limpios = [strip_html(p) for p in t["pasos"][:5]]
            partes.append(f"{t.get('pasos_titulo', 'Acciones y detalles')}: " + " | ".join(pasos_limpios))
        if t.get("fundamento"):
            partes.append(f"Fundamento legal: {strip_html(t['fundamento'])}")
        if t.get("contactos"):
            ctos = []
            for cid in t["contactos"][:3]:
                if cid in kb.CONTACTS:
                    c = kb.CONTACTS[cid]
                    tel = c.get("phone", "")
                    ctos.append(f"{c['name']}" + (f" (Tel: {tel})" if tel else ""))
            if ctos:
                partes.append("Contactos: " + "; ".join(ctos))
        return "\n".join(partes)[:1800]

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

        # 3) Coincidencia local muy fuerte (ahorra API y responde al instante)
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

        # 5) MINI-RAG + GROQ: Busca en los 3 archivos knowledge y responde con base jurídica actualizada
        if self.client:
            top_tids = self._retrieve_relevant_topics(norm, scores, top_k=3)
            contexto_rag = "\n\n".join(self._format_topic_for_rag(tid) for tid in top_tids)

            system_instruction = (
                "Eres un asistente automatizado de orientación sobre derechos humanos y normatividad de la IA. "
                "Tu labor es orientar de forma empática, clara, estructurada y formal, sin presentarte como "
                "canal oficial ni autoridad.\n\n"
                "REGLAS ESTRICTAS DE CONTENIDO:\n"
                "1. Usa PRIORITARIAMENTE la información de las 'FICHAS DE CONOCIMIENTO VERIFICADAS' de abajo. "
                "Contienen legislación mexicana y del Estado de México actualizada a 2025-2026 (por ejemplo: Secretaría Anticorrupción y Buen Gobierno en lugar de INAI, Transparencia Mexiquense en lugar de INFOEM, LFPDPPP 2025, Ley Olimpia, Principios de Chapultepec, Plan Nacional de IA 2026, AI Act de la UE). No uses organismos extintos si la ficha indica el vigente.\n"
                "2. Si las fichas cubren la pregunta del usuario, sintetiza una respuesta directa, clara y bien organizada citando el fundamento legal.\n"
                "3. Si ninguna ficha trata directamente el tema, responde con tus conocimientos sobre derechos humanos y marco legal mexicano vigente, manteniendo rigor y neutralidad.\n"
                "4. Formato obligatorio: escribe en párrafos cortos y listas con guiones (-). NO uses tablas Markdown (con |) ni encabezados con # o ##; usa **negritas** para títulos y conceptos clave.\n"
                "5. Nunca des asesoría jurídica formal ni actúes como abogado, y recuerda que la respuesta puede contener errores y debe verificarse en fuentes oficiales.\n"
                "6. Si detectas riesgo o peligro inminente, indica inmediatamente llamar al **911** o a la **CODHEM (800 999 4000)**.\n\n"
                f"FICHAS DE CONOCIMIENTO VERIFICADAS:\n{contexto_rag}"
            )

            try:
                todos_modelos = [
                    m.id for m in self.client.models.list().data
                    if not any(x in m.id.lower() for x in ("whisper", "guard", "tts", "orpheus", "allam"))
                ]
                modelos_disponibles = sorted(
                    todos_modelos,
                    key=lambda x: (0 if "llama" in x.lower() else 1, x)
                )

                for modelo_groq in modelos_disponibles[:4]:
                    try:
                        completion = self.client.chat.completions.create(
                            model=modelo_groq,
                            messages=[
                                {"role": "system", "content": system_instruction},
                                {"role": "user", "content": user_message},
                            ],
                            temperature=0.25,
                            max_tokens=850,
                        )

                        respuesta_texto = completion.choices[0].message.content
                        if respuesta_texto:
                            texto_formateado = re.sub(r"^#{1,3}\s+(.+)$", r"<b>\1</b>", respuesta_texto, flags=re.MULTILINE)
                            texto_formateado = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", texto_formateado)
                            texto_formateado = texto_formateado.replace("\n", "<br>")
                            aviso_ia = (
                                "<div class='mb-2 text-xs font-semibold text-indigo-700 bg-indigo-50 p-2 rounded'>"
                                "🤖 Respuesta generada con IA a partir de nuestra base normativa: puede contener errores; verifica en fuentes oficiales.</div>"
                            )
                            html_resp = (
                                f"{aviso_ia}<div class='mt-1'>{texto_formateado}</div>"
                                f"<div class='mt-3'>{DISCLAIMER}</div>"
                            )
                            sugerencias_ids = top_tids[:2] + [i["id"] for i in self.menu()[:1]]
                            suggestions = self._suggestions(list(dict.fromkeys(sugerencias_ids))[:3])
                            return {"html": html_resp, "suggestions": suggestions, "topic": None}
                    except Exception as err_mod:
                        print(f"Fallo con {modelo_groq}: {err_mod}")
                        continue

            except Exception as e:
                print(f"Error general con Groq: {e}")

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
            if i == "fuentes":
                out.append({"id": "fuentes", "label": "Fuentes de información"})
            elif i in self.topics:
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
            "Hola, soy un <b>asistente automatizado de orientación sobre derechos humanos</b>. "
            "Puedo explicarte tus derechos, orientarte sobre <b>qué hacer ante una situación</b> y facilitarte teléfonos "
            "de ayuda del Estado de México y de la UAEMéx. "
            "Esta información es solo de referencia, <b>puede contener errores</b> y debes verificarla en fuentes oficiales.<br><br>"
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
