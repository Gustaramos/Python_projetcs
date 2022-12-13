import plotly.express as px
import os
import pandas as pd

# Lógica de programação

# Passo 0 - Entender o desafio que você quer resolver

# Passo 1 - Percorrer todos os arquivos da pasta base de dados (Pasta Vendas)
lista_arquivos = os.listdir('C:\Gustaramos\Python_projetcs\AnaliseDados\Vendas')
tabela_total = pd.DataFrame(lista_arquivos)
# Passo 2 - Importar as bases de dados de vendas
for arquivo in lista_arquivos:
    # Se tem 'Vendas' no nome do arquivo, então
    if 'Vendas' in arquivo:
        # Importar o arquivo
        tabela = pd.read_csv(f'C:\Gustaramos\Python_projetcs\AnaliseDados\Vendas/{arquivo}')
        tabela_total = pd.concat([tabela])

# Passo 3 - Tratar / Compilar as bases de dados
print(tabela_total)

# Passo 4 - Calcular o produto mais vendido (em quantidade)
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
print(tabela_produtos)

# Passo 5 - Calcular o produto que mais faturou (em faturamento)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tabela_faturamento)

# Passo 6 - Calcular a loja/cidade que mais vendeu (em faturamento) - criar um gráfico/dashboard
tabela_loja = tabela_total.groupby('Loja').sum()
tabela_loja = tabela_loja[['Faturamento']]
print(tabela_loja)

# .append já está fora de uso na biblioteca do pandas
grafico = px.bar(tabela_loja, x=tabela_loja.index,  y=tabela_faturamento.index)
grafico.show()