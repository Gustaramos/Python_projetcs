import os
import pandas as pd

# Lógica de programação

# Passo 0 - Entender o desafio que você quer resolver

# Passo 1 - Percorrer todos os arquivos da pasta base de dados (Pasta Vendas)
lista_arquivos = os.listdir('C:\Gustaramos\Python_projetcs\AnaliseDados\Vendas')

tabela_total = pd.DataFrame()


# Passo 2 - Importar as bases de dados de vendas
for arquivo in lista_arquivos:
    # print(arquivo)
    # Se tem 'Vendas' no nome do arquivo, então
    if 'Vendas' in arquivo:
        # Importar o arquivo
        tabela = pd.read_csv(f'C:\Gustaramos\Python_projetcs\AnaliseDados\Vendas/{arquivo}')
        tabela_total = pd.concat([tabela])
print(tabela_total)
# se tem "Vendas" no nome do arquivo, então

# Passo 3 - Tratar / Compilar as bases de dados

# Passo 4 - Calcular o produto mais vendido (em quantidade)

# Passo 5 - Calcular o produto que mais faturou (em faturamento)

# Passo 6 - Calcular a loja/cidade que mais vendeu (em faturamento) - criar um gráfico/dashboard


# .append já está fora de uso na biblioteca do pandas