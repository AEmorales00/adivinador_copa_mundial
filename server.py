from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from src.agente import Agente

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

# Inicializa el agente con tu API token
agente = Agente(api_token="95353c8ad2b34088beab0d2003fb5211")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/iniciar", methods=["GET"])
def iniciar_juego():
    return jsonify({"mensaje": "¡Bienvenido al Adivinador de la Copa Mundial!"})

@app.route("/adivinar", methods=["POST"])
def adivinar():
    datos = request.json
    resultado = agente.adivinar_jugador(datos)
    return jsonify({"resultado": resultado if resultado else "No se encontró un jugador"})

if __name__ == "__main__":
    app.run(debug=True)
