from flask import Flask, request, jsonify  # Importa as classes necessárias do Flask
from flask_cors import CORS  # Importa o Flask-CORS para lidar com solicitações cross-origin
import requests  # Importa o módulo requests para fazer solicitações HTTP

app = Flask(__name__)  # Cria uma instância do aplicativo Flask
CORS(app)  # Configuração do Flask-CORS para permitir solicitações cross-origin

api_key = 'dfd8650a'  # Chave de API para acessar o serviço de busca de filmes

@app.route('/buscar_filmes', methods=['GET'])  # Define uma rota '/buscar_filmes' que aceita apenas solicitações GET
def buscar_filmes():
    texto_buscar = request.args.get('filme')  # Obtém o parâmetro 'filme' da consulta da solicitação GET
    url = f"http://www.omdbapi.com/?type=movie&apikey={api_key}&s={texto_buscar}"  # Constrói a URL da API de busca de filmes
    pedido = requests.get(url)  # Faz uma solicitação GET para a API de busca de filmes
    
    if pedido.status_code == 200:  # Verifica se a solicitação foi bem-sucedida (status code 200)
        dicionario_do_pedido = pedido.json()  # Converte a resposta JSON em um dicionário Python
        quantidade_filmes = dicionario_do_pedido.get('totalResults', 'Erro ao buscar filmes')  # Obtém a quantidade de filmes encontrados ou retorna uma mensagem de erro
        return jsonify({'quantidade_filmes': quantidade_filmes})  # Retorna a quantidade de filmes encontrados como resposta JSON
    else:
        return jsonify({'error': 'Erro ao buscar filmes'}), 500  # Retorna uma mensagem de erro como resposta JSON com status code 500 em caso de falha na solicitação

if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor Flask em modo de depuração se este script for executado diretamente
