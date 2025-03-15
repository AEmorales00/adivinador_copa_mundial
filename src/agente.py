from .models import Jugador
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from .api_football import APIFootball


class Agente:
    def __init__(self, api_token, api_secret, app=None):
        self.api = APIFootball(api_token, api_secret)

        # Si la app no ha sido pasada, la obtenemos de 'current_app'
        if app is not None:
            self.app = app
        else:
            self.app = current_app._get_current_object()

        self.paises_campeones = self._cargar_paises_campeones()

    def _cargar_paises_campeones(self):
        """Carga los jugadores desde la base de datos dentro del contexto de la aplicación."""
        with self.app.app_context():  # Se asegura que la app esté en contexto
            # Acceso a la base de datos dentro del contexto de Flask
            jugadores = Jugador.query.all()

            paises = [{"country": jugador.pais, "wins": jugador.ano, "year": jugador.ano} for jugador in jugadores]
        
        return paises
