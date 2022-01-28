from app.models import BaseModel
from app.extensions import db


class Pedido(BaseModel):

    __tablename__ = 'pedido'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    pagamento_confirmado = db.Column(db.Boolean, nullable = False)
    data_confirmacao_pagamento = db.Column(db.String(30), nullable = True)
    numero_parcelas = db.Column(db.Integer, nullable = True)

    #One-to-One Relationships
    id_carrinho = db.Column(db.Integer, db.ForeignKey('carrinho.id'))
    carrinho = db.relationship("Carrinho", back_populates="pedido")

    def json(self): 

        return {
            "pagamento_confirmado": self.pagamento_confirmado,
            "data_confirmacao_pagamento": self.data_confirmacao_pagamento,
            "numero_parcelas": self.numero_parcelas,
        }
