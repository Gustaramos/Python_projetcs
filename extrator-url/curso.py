# extrair o valor do parâmetro curso
url = "https://www.alura.com.br/curso?curso=python"

# Extrair a base para os parametros
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
url_parametro = url[indice_interrogacao + 1:]

parametro_busca = "curso"
indice_parametro_busca = url_parametro.find(parametro_busca)
indice_valor = indice_parametro_busca + len(parametro_busca) + 1
valor = url_parametro[indice_valor:]
print(valor)

# indice_valor = indice_curso + len("curso") + 1

# valor = url[indice_valor:]
# print(valor)