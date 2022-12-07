url = 'https://bytbank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real'
# url = ''

# Limpeza da url
url = url.strip()

# Validação da url
if url == '':
    raise ValueError('Esta URL esta vazia')

# Separa a base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parâmetro
parametro_de_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_de_busca)
indice_do_valor = indice_parametro + len(parametro_de_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_do_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_do_valor:]
else:
    valor = url_parametros[indice_do_valor:indice_e_comercial]
print(valor)