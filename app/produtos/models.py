from app.models import BaseModel
from app.extensions import db
from sqlalchemy import Table


#Many-to-Many Relationships
associacao_produtos_carrinho = Table ('association_product_cart', BaseModel.metadata,
                                db.Column('id_carrinho', db.ForeignKey('carrinho.id')),
                                db.Column('id_produtos', db.ForeignKey('produto.id')))


#Many-to-Many Relationships
associacao_produtos_encarte = Table ('association_product_encarte', BaseModel.metadata,
                                db.Column('id_encarte', db.ForeignKey('encarte.id')),
                                db.Column('id_produtos', db.ForeignKey('produto.id')))



class Produto(BaseModel):

    __tablename__ = 'produto'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(80), nullable = False)
    marca = db.Column(db.String(30), nullable = False)
    tamanho = db.Column(db.String(20), nullable = False)
    preco_descontado = db.Column(db.Float, nullable = True)
    descricao = db.Column(db.String(100), nullable = False)
    categoria = db.Column(db.String(30), nullable = False)
    subcategoria = db.Column(db.String(30), nullable = False)
    preco_normal = db.Column(db.Float, nullable = False)
    lote = db.Column(db.String(40), nullable = False, unique = True)
    validade = db.Column(db.String(30), nullable = False)
    custo = db.Column(db.Float, nullable = False)
    estoque = db.Column(db.Integer, nullable = False)
    importado_nacional = db.Column(db.String(20), nullable = False)
    proibido_menor_idade = db.Column(db.Boolean, nullable = True)
    alergenos = db.Column(db.String(100), nullable = False) #Aproximar o público com intolerancias alimentares


    #Many-to-Many Relationships
    carrinhos = db.relationship("Carrinho", secondary = associacao_produtos_carrinho, backref="produto")
    encartes = db.relationship("Encarte", secondary = associacao_produtos_encarte, backref="produto")


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
            "validade": self.validade,
            "estoque": self.estoque,
            "importado_nacional": self.importado_nacional,
            "proibido_menor_idade": self.proibido_menor_idade,
            "alergenos": self.alergenos           
        }
