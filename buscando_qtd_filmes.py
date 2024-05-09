import requests 

api_key = 'dfd8650a'

def busca_qtd_filmes(texto_buscar):
    url = f"http://www.omdbapi.com/?type=movie&apikey={api_key}&s={texto_buscar}"
    pedido = requests.get(url) #conectar na URL
    dicionario_do_pedido = pedido.json() #transformo a string que eu recebi num dicionário de python
    return dicionario_do_pedido['totalResults']

# Exemplo de uso:
# texto_usuario = "Um filme que você deseja obter a quantidade de variações"
# quantidade_filmes = busca_qtd_filmes(texto_usuario)
# print(f"A pesquisa por '{texto_usuario}' encontrou {quantidade_filmes} filmes")
