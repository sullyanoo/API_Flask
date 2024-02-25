# make_response: Função que estrutura o response da API.
# jsonify: Função que estrutura uma lista em arquivo json.
# request: Captura o conteudo da requisição.

from flask import Flask, make_response, jsonify, request
from db import carros
import json

# Instanciando o Flask

app = Flask(__name__)

# Essa configuração evita que ao inserir um novo item em nosso banco de dados, seja ordenado em ordem alfabética.
app.config['JSON_SORT_KEYS'] = False

# Criando a rota para o nosso metodo (GET)
@app.route('/carros', methods = ['GET'])
def get_carros():
    return make_response(
        jsonify(
            message = 'Lista de carros.',
            data = carros
        )
    )
@app.route('/carros/<int:id>', methods= ['GET'])
def get_carros_id(id):
    for carro in carros:
        if carro.get('id') == id:
            return jsonify(
                message = 'Carro selecionado.',
                data = carro
            )

@app.route('/carros', methods = ['POST'])
def create_carros():
    insert = request.json
    carros.append(insert)
    return make_response(
        jsonify(
            message = 'Carro cadastrado com sucesso.',
            data = carros
        )
    )

@app.route('/carros/<int:id>', methods = ['PUT'])
def alter_carros(id):
    carro_alter = request.get_json()
    for indice, carro in enumerate(carros):
        if carro.get('id') == id:
            indice[carro].update(carro_alter)
            return jsonify(indice[carro])


@app.route('/carros/<int:id>', methods = ['DELETE'])
def delete_carros(id):
    for carro in carros:
        if carro.get('id') == id:
            carros.remove(carro)
            return jsonify({"message": f"Car deleted successfully"})


app.run(port=5000, host='localhost', debug= True)