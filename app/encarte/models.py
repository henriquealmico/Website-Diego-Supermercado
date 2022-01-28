from app.models import BaseModel
from app.extensions import db


class Encarte(BaseModel):

    __tablename__ = 'encarte'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(80), nullable = False, unique = True)
    data_inicio = db.Column(db.String(30), nullable = False)
    data_termino = db.Column(db.String(30), nullable = False)


    def json(self): 

        return {
            "id": self.id,
            "nome": self.nome,
            "data_inicio": self.data_inicio,
            "data_termino": self.data_termino,           
        }


