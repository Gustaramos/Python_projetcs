class Produtos:
    def __init__(self, nome, valor, descricao_produto):
        self._nome = nome
        self._valor = valor
        self._descricao_produto = descricao_produto

    @property
    def valor(self):
        return self._valor

    @property
    def nome(self):
        return self._nome

    @property
    def descricao_produto(self):
        return self._descricao_produto

class Doce(Produtos):
    def __init__(self, nome, valor, descricao_produto, sabor):
        super().__init__(nome, valor, descricao_produto)
        self.sabor = sabor

class Salgados(Produtos):
    def __init__(self, nome, valor, descricao_produto, sabor):
        super().__init__(nome, valor, descricao_produto)
        self.sabor = sabor

class Paes(Produtos):
    def __ini_(self, nome, valor, descricao_produto, massa, graos):
        super().__init__(nome, valor, descricao_produto)
        self.massa = massa
        self.graos = graos

class Sucos(Produtos):
    def __init__(self, nome, valor, descricao_produto, polpa, tamanho):
        super().__init__(nome, valor, descricao_produto)
        self.polpa = polpa
        self.tamanho = tamanho

class Refrigerantes(Produtos):
    pass

sucos = Sucos('Tropical', 7.90, 'Suco refrescante', 'Manga, abacaxi, laranja e maracujá', '500ml')
print(f'Sabor do suco: {sucos.nome}\nValor do suco: {sucos.valor :.2f}\nPolga/Sabor: {sucos.polpa}\nDescrição: {sucos.descricao_produto}\nTamanho: {sucos.tamanho}')
