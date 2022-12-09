
endereco = 'Capitão do Mato, 450, Jacomo Violim, Londrina, PR, 86088-030'

import re    #RegEx --- Expressões regulares
# Encontrando o padrão - CEP
# 5 digitos + hífen (opcional) + 3 digitos

# Criando padrão com método compile. Após definir o padrão, atribuir a uma variavel.
padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')
# Após definir o padrão, fazer a busca dele dentro de uma string
busca = padrao.search(endereco)    #Match
if busca:
    cep = busca.group()
    print(cep)

    .sum