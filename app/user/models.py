from app.models import BaseModel
from app.extensions import db


class User(BaseModel):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    idade = db.Column(db.Integer, nullable = False)
    cpf = db.Column(db.String(15), nullable = False, unique = True)
    nome = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(70), nullable = False, unique = True, index = True)
    senha = db.Column(db.String(40), nullable = False)
    endereco = db.Column(db.String(80), nullable = False)
    cidade = db.Column(db.String(20), nullable = False)
    estado = db.Column(db.String(20), nullable = False)
    cep = db.Column(db.String(15), nullable = False)
    ja_realizou_compra = db.Column(db.Boolean, nullable = False)
    como_descobriu_site = db.Column(db.String(40), nullable = False)

    #One-to-One Relationships
    id_carrinho = db.Column(db.Integer, db.ForeignKey('carrinho.id'))
    carrinho = db.relationship("Carrinho", back_populates="user")

    def json(self): 

        return {
            "id": self.id,
            "nome": self.nome,
            "cpf": self.cpf,
            "idade": self.idade,
            "email": self.email,
            "endereco": self.endereco,
            "cidade": self.cidade,
            "estado": self.estado,
            "cep": self.cep,
            "ja_realizou_compra": self.ja_realizou_compra,
            "como_descobriu_site": self.como_descobriu_site
        }
    