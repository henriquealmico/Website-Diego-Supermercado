from app.models import BaseModel
from app.extensions import db
from sqlalchemy import Table



associacao_cupom_user = Table ('association', BaseModel.metadata,
                                db.Column('user_id', db.ForeignKey('user.id')),
                                db.Column('cupom_id', db.ForeignKey('cupom.id')))


class Cupom(BaseModel):

    __tablename__ = 'cupom'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    desconto = db.Column(db.String(15), nullable = False)
    código = db.Column(db.String(20), nullable = False, unique = True, index = True)
    forma_utilizacao = db.Column(db.String(100), nullable = False)
    campanha = db.Column(db.String(20), nullable = False)
    data_inicio = db.Column(db.String(30), nullable = False)
    data_termino = db.Column(db.String(30), nullable = True)
    limite_usuarios = db.Column(db.Integer, nullable = True)
    objetivo = db.Column(db.String(50), nullable = False) #Ex: Atrair clientes, venda por impulso, conversão de carrinho abandonado, etc


    #Many-to-Many Relationships
    users = db.relationship("User", secondary = associacao_cupom_user, backref = "cupom")

    #One-to-Many Relationships
    carrinho = db.relationship("Carrinho")
    
    def json(self): 

        return {
            "id": self.id,
            "desconto": self.desconto,
            "código": self.código,
            "forma_utilizacao": self.forma_utilizacao,
            "campanha": self.campanha,
            "data_inicio": self.data_inicio,
            "data_termino": self.data_termino,
            "limite_usuarios": self.limite_usuarios,
        }