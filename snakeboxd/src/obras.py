import os
import sys

def voltar_ao_menu_principal():
    ''' Função de retornar ao menu principal'''
    input('\nAperte uma tecla para voltar ao menu principal. ')

class Obra:
    '''Classe com o nome, categoria, duração, autor e ano de lançamento'''
    obras = []

    def __init__ (self, nome, categoria, genero, classificacao, duracao, ano, diretor,):
        self.nome = nome
        self.categoria = categoria
        self.genero = genero
        self._classificacao = classificacao
        self.duracao = duracao
        self.ano = ano
        self.diretor = diretor
        Obra.obras.append(self)

    @classmethod
    def listar_obras(cls):
        '''Metodo de classe que lista as obras cadastradas'''
        print("\nLista de obras cadastradas:\n")
        print('★ ' * 20) 
        for obra in cls.obras: 
            print()
            print(f"Nome: {obra.nome}")
            print(f"Categoria: {obra.categoria}")
            print(f'Gênero: {obra.genero}')
            print(f"Classificação: {obra.classificacao}")
            print(f"Duração: {obra.duracao} minutos")
            print(f"Ano: {obra.ano}")
            print(f"Diretor(a): {obra.diretor}")
            print()
            print('★ ' * 20)
        voltar_ao_menu_principal()

    @property
    def classificacao(self):
        '''Propriedade que retorna a classificação etária'''
        if self._classificacao.lower() == 'livre':
            return 'Livre (para todos os públicos)'
        return f'{self._classificacao} anos'

def opcao_invalida():
    '''Função que exibe mensagem de opção inválida'''
    print('Opção inválida!')
    voltar_ao_menu_principal()