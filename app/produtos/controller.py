from datetime import datetime
from app.produtos.models import Produto, Encarte
from flask import request, jsonify
from flask.views import MethodView


class ProdutoG(MethodView): #/produto

    def post(self):

        body = request.json

        nome = body.get('nome')
        marca = body.get('marca')
        tamanho = body.get('tamanho')
        descricao = body.get('descricao')
        categoria = body.get('categoria')
        subcategoria = body.get('subcategoria')
        preco_normal = body.get('preco_normal')
        preco_descontado = body.get('preco_descontado')
        lote = body.get('lote')
        validade = body.get('validade')
        custo = body.get('custo')
        estoque = body.get('estoque')
        importado_nacional = body.get('importado_nacional')
        proibido_menor_idade = body.get('proibido_menor_idade')
        alergenos = body.get('alergenos')


        if  isinstance(nome, str) and isinstance(marca, str) and isinstance(tamanho, str) and\
            isinstance(descricao, str) and isinstance(categoria, str) and isinstance(subcategoria, str) and\
            isinstance(preco_normal, float) and isinstance(preco_descontado, float) and isinstance(lote, str) and\
            isinstance(validade, datetime) and isinstance(custo, float) and isinstance(estoque, int) and\
            isinstance(importado_nacional, str) and isinstance(proibido_menor_idade, bool) and isinstance(alergenos, str):

            produto = Produto.query.filter_by(lote=lote).first()

            if produto:
                return {"code_status":"produto already exists"}, 400

            produto = Produto(nome=nome, marca=marca, tamanho=tamanho, descricao=descricao, categoria=categoria,\
                              subcategoria=subcategoria, preco_normal=preco_normal, preco_descontado=preco_descontado, lote=lote,\
                              validade=validade, custo=custo, estoque=estoque, importado_nacional=importado_nacional,\
                              proibido_menor_idade=proibido_menor_idade, alergenos=alergenos)

            produto.save()
            return produto.json(), 201
        
        else:
            return {"code_status":"invalid data in request"}, 400


    def get(self):

        produtos = Produto.query.all()
        return jsonify([produto.json() for produto in produtos]), 200


class ProdutoId(MethodView): #/produto/<int:id>

    def get(self, id):

        produto = Produto.query.get_or_404(id)
        return produto.json()

    def put(self, id):

        body = request.json
        produto = Produto.query.get_or_404(id)

        nome = body.get('nome')
        marca = body.get('marca')
        tamanho = body.get('tamanho')
        descricao = body.get('descricao')
        categoria = body.get('categoria')
        subcategoria = body.get('subcategoria')
        preco_normal = body.get('preco_normal')
        preco_descontado = body.get('preco_descontado')
        lote = body.get('lote')
        validade = body.get('validade')
        custo = body.get('custo')
        estoque = body.get('estoque')
        importado_nacional = body.get('importado_nacional')
        proibido_menor_idade = body.get('proibido_menor_idade')
        alergenos = body.get('alergenos')


        if  isinstance(nome, str) and isinstance(marca, str) and isinstance(tamanho, str) and\
            isinstance(descricao, str) and isinstance(categoria, str) and isinstance(subcategoria, str) and\
            isinstance(preco_normal, float) and isinstance(preco_descontado, float) and isinstance(lote, str) and\
            isinstance(validade, datetime) and isinstance(custo, float) and isinstance(estoque, int) and\
            isinstance(importado_nacional, str) and isinstance(proibido_menor_idade, bool) and isinstance(alergenos, str):

            produto.nome = nome
            produto.marca = marca
            produto.tamanho = tamanho
            produto.descricao = descricao
            produto.categoria = categoria
            produto.subcategoria = subcategoria
            produto.preco_normal = preco_normal
            produto.preco_descontado = preco_descontado
            produto.lote = lote
            produto.validade = validade
            produto.custo = custo
            produto.estoque = estoque
            produto.importado_nacional = importado_nacional
            produto.proibido_menor_idade = proibido_menor_idade
            produto.alergenos = alergenos


            produto.update()
            return produto.json(), 201
        
        else:

            return {"code_status":"invalid data in request"}, 400


    def patch(self, id):

        body = request.json
        produto = Produto.query.get_or_404(id)

        nome = body.get('nome', produto.nome)
        marca = body.get('marca', produto.marca)
        tamanho = body.get('tamanho', produto.tamanho)
        descricao = body.get('descricao', produto.descricao)
        categoria = body.get('categoria', produto.categoria)
        subcategoria = body.get('subcategoria', produto.subcategoria)
        preco_normal = body.get('preco_normal', produto.preco_normal)
        preco_descontado = body.get('preco_descontado', produto.preco_descontado)
        lote = body.get('lote', produto.lote)
        validade = body.get('validade', produto.validade)
        custo = body.get('custo', produto.custo)
        estoque = body.get('estoque', produto.estoque)
        importado_nacional = body.get('importado_nacional', produto.importado_nacional)
        proibido_menor_idade = body.get('proibido_menor_idade', produto.proibido_menor_idade)
        alergenos = body.get('alergenos', produto.alergenos)


        if  isinstance(nome, str) and isinstance(marca, str) and isinstance(tamanho, str) and\
            isinstance(descricao, str) and isinstance(categoria, str) and isinstance(subcategoria, str) and\
            isinstance(preco_normal, float) and isinstance(preco_descontado, float) and isinstance(lote, str) and\
            isinstance(validade, datetime) and isinstance(custo, float) and isinstance(estoque, int) and\
            isinstance(importado_nacional, str) and isinstance(proibido_menor_idade, bool) and isinstance(alergenos, str):

            produto.nome = nome
            produto.marca = marca
            produto.tamanho = tamanho
            produto.descricao = descricao
            produto.categoria = categoria
            produto.subcategoria = subcategoria
            produto.preco_normal = preco_normal
            produto.preco_descontado = preco_descontado
            produto.lote = lote
            produto.validade = validade
            produto.custo = custo
            produto.estoque = estoque
            produto.importado_nacional = importado_nacional
            produto.proibido_menor_idade = proibido_menor_idade
            produto.alergenos = alergenos

            produto.update()
            return produto.json(), 201
        
        else:

            return {"code_status":"invalid data in request"}, 400


    def delete(self, id):

        produto = Produto.query.get_or_404(id)
        produto.delete(produto)
        return produto.json()
        
        



class EncarteG(MethodView): #/encarte

    def post(self):

        body = request.json


        data_inicio = body.get('data_inicio')
        data_termino = body.get('data_termino')
        nome = body.get('nome')


        if  isinstance(data_inicio, datetime) and isinstance(data_termino, datetime) and isinstance(nome, str):

            encarte = Encarte(nome=nome, data_inicio=data_inicio, data_termino=data_termino)

            encarte.save()
            return encarte.json(), 201
        
        else:
            return {"code_status":"invalid data in request"}, 400


    def get(self):

        encartes = Encarte.query.all()
        return jsonify([encarte.json() for encarte in encartes]), 200


class EncarteId(MethodView): #/encarte/<int:id>

    def get(self, id):

        encarte = Encarte.query.get_or_404(id)
        return encarte.json()

    def put(self, id):

        body = request.json
        encarte = Encarte.query.get_or_404(id)


        data_inicio = body.get('data_inicio')
        data_termino = body.get('data_termino')
        nome = body.get('nome')


        if  isinstance(data_inicio, datetime) and isinstance(data_termino, datetime) and isinstance(nome, str):

            encarte.data_inicio = data_inicio
            encarte.data_termino = data_termino
            encarte.nome = nome

            encarte.update()
            return encarte.json(), 201
        
        else:

            return {"code_status":"invalid data in request"}, 400


    def patch(self, id):

        body = request.json
        encarte = Encarte.query.get_or_404(id)

        data_inicio = body.get('data_inicio', encarte.data_inicio)
        data_termino = body.get('data_termino', encarte.data_termino)
        nome = body.get('nome', encarte.nome)


        if  isinstance(data_inicio, datetime) and isinstance(data_termino, datetime) and isinstance(nome, str):

            encarte.nome = nome
            encarte.data_inicio = data_inicio
            encarte.data_termino = data_termino

            encarte.update()
            return encarte.json(), 201
        
        else:

            return {"code_status":"invalid data in request"}, 400


    def delete(self, id):

        encarte = Encarte.query.get_or_404(id)
        encarte.delete(encarte)
        return encarte.json()