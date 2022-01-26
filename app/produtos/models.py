from app.models import BaseModel
from app.extensions import db
from sqlalchemy import Table


associacao_produtos_carrinho = Table ('association_product_cart', BaseModel.metadata,
                                db.Column('id_carrinho', db.ForeignKey('carrinho.id')),
                                db.Column('id_produtos', db.ForeignKey('produto.id')))


associacao_produtos_encarte = Table ('association_product_encarte', BaseModel.metadata,
                                db.Column('id_encarte', db.ForeignKey('encarte.id')),
                                db.Column('id_produtos', db.ForeignKey('produto.id')))


class BaseEncarteProduto(BaseModel):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(80), nullable = False)
    marca = db.Column(db.String(30), nullable = False)
    tamanho = db.Column(db.String(20), nullable = False)
    preco_descontado = db.Column(db.Float, nullable = True)



class Produto(BaseEncarteProduto):

    __tablename__ = 'produto'
    
    descricao = db.Column(db.String(100), nullable = False)
    categoria = db.Column(db.String(30), nullable = False)
    subcategoria = db.Column(db.String(30), nullable = False)
    preco_normal = db.Column(db.Float, nullable = False)
    lote = db.Column(db.String(40), nullable = False, unique = True)
    validade = db.Column(db.DateTime, nullable = False)
    custo = db.Column(db.Float, nullable = False)
    estoque = db.Column(db.Integer, nullable = False)
    importado_nacional = db.Column(db.String(20), nullable = False)
    proibido_menor_idade = db.Column(db.Boolean, nullable = True)
    alergenos = db.Column(db.String(100), nullable = False) #Aproximar o público com intolerancias alimentares


    #Many-to-Many Relationships
    carrinhos = db.relationship("Carrinho", secondary = associacao_produtos_carrinho)
    encartes = db.relationship("Encarte", secondary = associacao_produtos_encarte)


    def json(self): 

        return {
            "id": self.id,
            "nome": self.nome,
            "marca": self.marca,
            "tamanho": self.tamanho,
            "descricao": self.descricao,
            "categoria": self.categoria,
            "subcategoria": self.subcategoria,
            "preco_normal": self.preco_normal,
            "preco_descontado": self.preco_descontado,
            "lote": self.lote,
            "validade": self.validade,
            "custo": self.custo,
            "estoque": self.estoque,
            "importado_nacional": self.importado_nacional,
            "proibido_menor_idade": self.proibido_menor_idade,
            "alergenos": self.alergenos           
        }



class Encarte(BaseEncarteProduto):

    __tablename__ = 'encarte'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(80), nullable = False, unique = True)
    data_inicio = db.Column(db.DateTime, nullable = False)
    data_termino = db.Column(db.DateTime, nullable = False)


    def json(self): 

        return {
            "id": self.id,
            "nome": self.nome,
            "data_inicio": self.data_inicio,
            "data_termino": self.data_termino,           
        }


