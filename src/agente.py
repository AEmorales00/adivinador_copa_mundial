from .api_football import APIFootball

class Agente:
    def __init__(self, api_token):
        self.api = APIFootball(api_token)
        self.jugadores = self._cargar_jugadores()  # Aquí llamamos a la función

    def _cargar_jugadores(self):
        """Carga los datos de los jugadores desde la API."""
        jugadores = self.api.obtener_ganadores_copa_mundial()
        print(f"Jugadores cargados desde la API: {jugadores}")  # Debug
        return jugadores

    def adivinar_jugador(self, respuestas):
            """Adivina el jugador basado en las respuestas del usuario."""
            posibles_jugadores = self.jugadores

            # Filtra los jugadores basado en las respuestas
            if respuestas.get("año") == "antes de 2000":
                posibles_jugadores = [j for j in posibles_jugadores if j["dateOfBirth"][:4] < "2000"]
            if respuestas.get("pais") == "Sudamérica":
                posibles_jugadores = [j for j in posibles_jugadores if j["nationality"] in ["Brazil", "Argentina", "Uruguay"]]
            if respuestas.get("posicion") == "Delantero":
                posibles_jugadores = [j for j in posibles_jugadores if j["position"] == "Attacker"]

            # Devuelve el primer jugador que coincida o un mensaje de error
            return posibles_jugadores[0]["name"] if posibles_jugadores else "No se encontró un jugador."
            #return "Jugador encontrado"