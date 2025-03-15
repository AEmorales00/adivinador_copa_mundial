import requests

class APIFootball:
    def __init__(self, api_token):
        self.base_url = "http://api.football-data.org/v4/"
        self.headers = {
            "X-Auth-Token": api_token
        }

    def obtener_competiciones(self):
        """Obtiene la lista de competiciones disponibles."""
        url = self.base_url + "competitions"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def obtener_equipo(self, team_id):
        """Obtiene información sobre un equipo específico."""
        url = self.base_url + f"teams/{team_id}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def obtener_jugadores_equipo(self, team_id):
        """Obtiene la lista de jugadores de un equipo."""
        equipo = self.obtener_equipo(team_id)
        if equipo and "squad" in equipo:
            return equipo["squad"]
        else:
            print(f"No se encontró el campo 'squad' en la respuesta del equipo {team_id}.")
            return None

    def obtener_partidos_competicion(self, competition_id, filters=None):
        """Obtiene los partidos de una competición específica con filtros opcionales."""
        url = self.base_url + f"competitions/{competition_id}/matches"
        if filters:
            response = requests.get(url, headers=self.headers, params=filters)
        else:
            response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def obtener_estadisticas_jugador(self, player_id):
        """Obtiene las estadísticas de un jugador específico."""
        url = self.base_url + f"players/{player_id}/matches"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def obtener_ganadores_copa_mundial(self):
        """Obtiene los ganadores de la Copa Mundial."""
        competicion_id = 2000  # ID de la Copa Mundial
        filters = {
            "stage": "FINAL",  # Filtro para obtener solo partidos finales
            "status": "FINISHED"  # Filtro para obtener partidos finalizados
        }
        partidos = self.obtener_partidos_competicion(competicion_id, filters)

        if not partidos or "matches" not in partidos:
            print("Error: No se pudieron obtener los partidos de la Copa Mundial.")
            return []

        ganadores = set()
        for partido in partidos["matches"]:
            if partido["score"].get("winner") == "HOME_TEAM":
                ganadores.add(partido["homeTeam"]["id"])
            elif partido["score"].get("winner") == "AWAY_TEAM":
                ganadores.add(partido["awayTeam"]["id"])

        print(f"IDs de equipos ganadores: {ganadores}")

        jugadores_ganadores = []
        for team_id in ganadores:
            jugadores = self.obtener_jugadores_equipo(team_id)
            if jugadores:
                jugadores_ganadores.extend(jugadores)

        print(f"Jugadores de equipos ganadores: {jugadores_ganadores}")
        return jugadores_ganadores