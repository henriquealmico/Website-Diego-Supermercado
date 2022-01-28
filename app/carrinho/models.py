from app.models import BaseModel
from app.extensions import db



class Carrinho(BaseModel):

    __tablename__ = 'carrinho'


    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    modelo_entrega = db.Column(db.String(15), nullable = False)
    preco_entrega = db.Column(db.String(15), nullable = False)
    prazo_entrega = db.Column(db.String(15), nullable = False)
    quantidade_itens = db.Column(db.Integer, nullable = False) 
    preco_total = db.Column(db.Float, nullable=False)
    data_pedido = db.Column(db.String(30), nullable = False)
    forma_pagamento = db.Column(db.String(15), nullable = False)
    agendamento_entrega = db.Column(db.String(30), nullable = True)


    #One-to-One Relationships
    user = db.relationship("User", back_populates="carrinho", uselist=False)
    pedido = db.relationship("Pedido", back_populates="carrinho", uselist=False)

    #Many-to-One Relationships
    id_cupom = db.Column(db.Integer, db.ForeignKey('cupom.id'))
    cupom = db.relationship("Cupom", back_populates="carrinho")


    def json(self): 

        return {
            "preco_total": self.preco_total,
            "data_pedido": self.data_pedido,
            "forma_pagamento": self.forma_pagamento,
            "modelo_entrega": self.modelo_entrega,
            "preco_entrega": self.preco_entrega,
            "quantidade_itens": self.quantidade_itens,
            "prazo_entrega": self.prazo_entrega,
            "agendamento_entrega": self.agendamento_entrega
        }
    
    
    


