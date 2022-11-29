url = 'https://bytbank.com/cambio?moedaDestino=dolar&moedaOrigem=real'

indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

parametro_de_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_de_busca)

print(indice_parametro)

indice_valor = indice_parametro + len(parametro_de_busca) + 1
valor = url_parametros[indice_valor:]
print(valor)