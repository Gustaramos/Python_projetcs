url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"

# Se a moeda de origem for igual a dolar, converter para real e se for origem real, converter para dolar
valor_dolar = 5.50
quantidade_converter = 100

moedaOrigem = 'dolar'
conversao = quantidade_converter / valor_dolar
print('O valor convertido fica em R${:.2f}'.format(conversao))



# extrator_url = ExtratorURL(url)
# VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
# moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
# moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
# quantidade = extrator_url.get_valor_parametro("quantidade")