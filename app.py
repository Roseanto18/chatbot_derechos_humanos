import os

from flask import Flask, render_template, request, jsonify
from models import ChatbotModel

app = Flask(__name__)
model = ChatbotModel()

MAX_LEN = 500  # límite de caracteres por mensaje


@app.route('/')
def index():
    # Los botones rápidos iniciales vienen del modelo
    return render_template('index.html', menu=model.menu())


@app.route('/chat', methods=['POST'])
def chat():
    # PRIVACIDAD: el mensaje se procesa en memoria y NO se guarda ni se registra.
    data = request.get_json(silent=True) or {}
    message = str(data.get('message', ''))[:MAX_LEN]
    topic = data.get('topic')
    topic = topic if isinstance(topic, str) else None

    return jsonify(model.get_response(message, topic))


@app.route('/privacidad')
def privacidad():
    return render_template('privacidad.html')


@app.route('/health')
def health():
    # Lo usan las plataformas de hosting para saber si la app está viva
    return jsonify(status='ok')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    debug = os.environ.get('FLASK_DEBUG', '1') == '1'  # en producción gunicorn no usa esto
    app.run(host='0.0.0.0', port=port, debug=debug)
