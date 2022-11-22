import pandas as pd
from twilio.rest import Client

account_sid = 'AXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'XXXXXXXXXXXXXXXXXXXXXX'

client = Client(account_sid, auth_token)


lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to="+1111222222222",
            from_="+1122333333333",
            body=f'No mês de {mes} alguém conseguiu bater a meta!\nVendedor: {vendedor}, Vendas{vendas}')
        print(message.sid)