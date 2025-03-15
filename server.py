from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from src.agente import Agente

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario:contraseña@localhost/nombre_base_datos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definir las credenciales de la API
API_TOKEN = "qdOmkHiHj1Yd0EJG"
API_SECRET = "9UBfzlDdcH0kWUJm7yJsf19y38M3NvJW"

# Crear una instancia del Agente con ambos parámetros
agente = Agente(api_token=API_TOKEN, api_secret=API_SECRET)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/iniciar", methods=["GET"])
def iniciar_juego():
    return jsonify({"mensaje": "¡Bienvenido al Adivinador de la Copa Mundial!"})

@app.route("/adivinar_pais", methods=["POST"])
def adivinar_pais():
    respuestas = request.json
    pais = agente.adivinar_pais(respuestas)
    return jsonify({"pais": pais})

if __name__ == "__main__":
    app.run(debug=True)
