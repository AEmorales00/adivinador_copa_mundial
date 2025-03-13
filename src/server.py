from flask import Flask, jsonify, request
from flask_cors import CORS
from src.agente import Agente

app = Flask(__name__)
CORS(app)  # Permite solicitudes desde cualquier origen (útil para desarrollo)

# Inicializa el agente con tu token de la API
agente = Agente(api_token="186a0d3d459e489daeb548cc02d8efd6")

# Endpoint para iniciar el juego
@app.route("/iniciar", methods=["GET"])
def iniciar_juego():
    return jsonify({"mensaje": "¡Bienvenido al Adivinador de la Copa Mundial!"})

# Endpoint para procesar respuestas del usuario
@app.route("/adivinar", methods=["POST"])
def adivinar():
    datos = request.json
    resultado = agente.adivinar_jugador(datos)
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)