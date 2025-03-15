import requests

class APIFootball:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://livescore-api.com/api-client"

    def obtener_partidos(self, competition_id, team_id=None, group_id=None):
        """Obtiene los partidos de una competición, equipo o grupo específico."""
        url = f"{self.base_url}/fixtures/matches.json"
        params = {
            "key": self.api_key,
            "secret": self.api_secret,
            "competition_id": competition_id
        }
        if team_id:
            params["team"] = team_id
        if group_id:
            params["group_id"] = group_id
        response = requests.get(url, params=params)
        return response.json() if response.status_code == 200 else None

    def obtener_clasificacion(self, competition_id, group):
        """Obtiene la clasificación de un grupo en la competición."""
        url = f"{self.base_url}/leagues/table.json"
        params = {
            "key": self.api_key,
            "secret": self.api_secret,
            "competition_id": competition_id,
            "group": group
        }
        response = requests.get(url, params=params)
        return response.json() if response.status_code == 200 else None

    def obtener_ganadores_copa_mundial(self, competition_id):
        """Obtiene los países ganadores de la Copa del Mundo."""
        url = f"https://api.football-data.org/v2/competitions/{competition_id}/matches"
        headers = {"X-Auth-Token": self.api_key}
        
        response = requests.get(url, headers=headers)
        data = response.json()

        # 🔍 Debug: Muestra la estructura de la respuesta
        print("📡 Respuesta de la API:", data)

        # Verifica si 'matches' está en la respuesta
        if "matches" not in data:
            print("⚠️ No se encontraron partidos en la API.")
            return []

        paises_campeones = []
        for partido in data["matches"]:
            print("📝 Partido:", partido)  # Ver estructura de cada partido
            
            # Si no existen 'homeTeam' o 'awayTeam', ignoramos el partido
            if "homeTeam" not in partido or "awayTeam" not in partido:
                continue
            
            # 🔍 Verifica qué claves tiene el partido antes de acceder
            print("🔑 Claves en partido:", partido.keys())

            # Evita KeyError verificando si 'home_score' y 'away_score' existen
            if "score" in partido and "winner" in partido["score"]:
                paises_campeones.append(partido["score"]["winner"])
        
        return paises_campeones


# Ejemplo de inicialización
api = APIFootball(api_key="qdOmkHiHj1Yd0EJG", api_secret="9UBfzlDdcH0kWUJm7yJsf19y38M3NvJW")

# Obtener ganadores de la Copa Mundial
ganadores = api.obtener_ganadores_copa_mundial(competition_id=362)
print("Equipos ganadores:", ganadores)
