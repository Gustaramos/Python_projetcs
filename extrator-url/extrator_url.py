import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitizacao_url(url)
        self.valida_url()

    def sanitizacao_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL esta vazia')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL não é valida')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_de_busca):
        indice_parametro = self.get_url_parametros().find(parametro_de_busca)
        indice_do_valor = indice_parametro + len(parametro_de_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_do_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_do_valor:]
        else:
            valor = self.get_url_parametros()[indice_do_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + '\n' + 'Base: ' + self.get_url_base() + '\n' + 'Parâmetros: ' + self.get_url_parametros()

    def __eq__(self, other):
        return self.url == other.url


url = 'https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real'
extrator_url = ExtratorURL(url)


valor_dolar = 5.50  # 1 dólar = 5.50 reais
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
quantidade = extrator_url.get_valor_parametro("quantidade")


# Se a moeda destino for igual a dolar, retornar o calculo = valor_em_dolar / valor_em_real

if moeda_origem == 'dolar' and moeda_destino == 'real':
    quantidade = int(quantidade)
    valor_conversao = quantidade / valor_dolar
    print(f'O valor da sua conversão de R${quantidade} reais, fica no total de U${valor_conversao:.2f} dolares')
elif moeda_origem == 'real' and moeda_destino == 'dolar':
    quantidade = int(quantidade)
    valor_conversao = quantidade * valor_dolar
    print(f'O valor da sua conversão de U${quantidade} dolares, fica no total de R${valor_conversao:.2f}')
else:
    print('Não foi possivel realizar a sua conversão!')