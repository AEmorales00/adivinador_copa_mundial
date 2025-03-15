from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Jugador(db.Model):
    __tablename__ = 'jugadores_campeones'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    pais = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    posicion = db.Column(db.String(50), nullable=False)
    equipo = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Jugador {self.nombre} ({self.pais}, {self.ano})>"

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'pais': self.pais,
            'ano': self.ano,
            'posicion': self.posicion,
            'equipo': self.equipo
        }
