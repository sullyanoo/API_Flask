# make_response: Função que estrutura o response da API.
# jsonify: Função que estrutura uma lista em arquivo json.

from flask import Flask, make_response, jsonify
from db import carros

# Instanciando o Flask

app = Flask(__name__)
app.run()

# Criando a rota para o nosso metodo (GET)
@app.route('/carros', methods = ['GET'])

def get_carros():
    return make_response(jsonify(carros))



