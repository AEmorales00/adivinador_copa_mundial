from flask import Flask, jsonify, request
from flask_cors import CORS
from src.agente import adivinar_jugador  # Importa la lógica del agente

app = Flask(__name__)
CORS(app)  # Permite solicitudes desde cualquier origen (útil para desarrollo)

# Endpoint para iniciar el juego
@app.route("/iniciar", methods=["GET"])
def iniciar_juego():
    return jsonify({"mensaje": "¡Bienvenido al Adivinador de la Copa Mundial!"})

# Endpoint para procesar respuestas del usuario
@app.route("/adivinar", methods=["POST"])
def adivinar():
    datos = request.json
    respuesta_usuario = datos.get("respuesta")
    resultado = adivinar_jugador(respuesta_usuario)
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)