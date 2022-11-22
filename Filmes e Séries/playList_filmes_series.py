class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome}\nAno: {self.ano}\nDuração: {self.duracao}min\nLikes: {self.likes}\n'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome}\nAno: {self.ano}\nTemporadas: {self.temporadas}\nLikes: {self.likes}\n'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 140)
atlanta = Serie('atlanta', 2020, 7)
homem_aranha = Filme('homem-aranha', 2020, 180)
vikings = Serie('vikings', 2016, 10)

homem_aranha.dar_like()
homem_aranha.dar_like()
homem_aranha.dar_like()
vikings.dar_like()
vikings.dar_like()
vikings.dar_like()
vikings.dar_like()
vikings.dar_like()
vikings.dar_like()
vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, vikings, homem_aranha]
playlist_fim_de_semana = Playlist('Playlist quente para o fim de semana!', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tá ou não tá?\n'
      f'A série Vikings está na minha playlist?')
if vikings in playlist_fim_de_semana:
    print('Sim')
else:
    print('Não')


# print('Filmes')
# print(f'Nome: {vingadores.nome}\nAno: {vingadores.ano}\nDuração: {vingadores.duracao}\nLikes: {vingadores.likes}\n')
# print('Séries')
# print(f'Nome: {atlanta.nome}\nAno: {atlanta.ano}\nTemporadas: {atlanta.temporadas}\nLikes: {atlanta.likes}')

