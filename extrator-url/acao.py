url = 'https://www.fundamentus.com.br/detalhes.php?papel=CAML3&tipo=2'

# Finalidade: Extrair valor do papel pesquisado

# Passo 1:
# Definir base da url para extrair os parâmetros
posicao_interrogacao = url.find('?')
url_base = url[:posicao_interrogacao + 1]
url_parametros = url[posicao_interrogacao + 1:]
print(url_parametros)

# Passo 2
# Definir o parâmetro de busca para encontrar o valor final

paramentro_busca = 'tipo'
indice_parametro = url_parametros.find(paramentro_busca)
tamanho_parametro = indice_parametro + len(paramentro_busca) + 1
posicao_e_comercial = url_parametros.find('&', indice_parametro)
if posicao_e_comercial == -1:
    valor = url_parametros[tamanho_parametro:]
else:
    valor = url_parametros[tamanho_parametro:posicao_e_comercial]
print(valor)
