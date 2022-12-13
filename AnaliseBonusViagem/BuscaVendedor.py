import pandas as pd
import openpyxl
#from twilio.rest import Client

<<<<<<< Updated upstream
#account_sid = 'AXXXXXXXXXXXXXXXXXXX'
#auth_token = 'XXXXXXXXXXXXXXXXXXXXXX'
=======
account_sid = 'co'
auth_token = 'XXXXXXXXXXXXXXXXXXXXXX'
>>>>>>> Stashed changes

#client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        #message = client.messages.create(
            #to="+1111111111111",
            #from_="+1111111111111",
            #body=f'No mês de {mes} alguém conseguiu bater a meta!\nVendedor: {vendedor}, Vendas{vendas}')
        #print(message.sid)
