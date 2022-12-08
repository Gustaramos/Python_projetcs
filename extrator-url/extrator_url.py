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
            valor = self.get_url_parametros[indice_do_valor:]
        else:
            valor = self.get_url_parametros()[indice_do_valor:indice_e_comercial]
        return valor

    #def get_conversao_moeda(self, parametro_busca):
        #conversao = self.get_url_parametros(parametro_busca)
        #return conversao

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + '\n' + 'Base: ' + self.get_url_base() + '\n' + 'Parâmetros: ' + self.get_url_parametros()

    def __eq__(self, other):
        return self.url == other.url


url = 'https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real'
extrator_url = ExtratorURL(url)
#moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
#print(moeda_origem)
#VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
#extrator_url2 = ExtratorURL(url)
#print(f'O tamanho da url é {len(extrator_url)}')
#print(id(extrator_url))
#print(id(extrator_url2))
#moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("moedaOrigem")
print(quantidade)
#extrator_url = ExtratorURL(None)
#extrator_url = ExtratorURL('//bytbank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real')
#extrator_url = ExtratorURL('https://bytbank.com?moedaDestino=dolar&quantidade=100&moedaOrigem=real')
