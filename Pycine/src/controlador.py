from obras import Obra
from interface import
import sys
import json

def adicionar_obras():
    nome = input('Digite o nome da obra: ')
    categoria = input('Informe a categoria da obra: ')
    genero = input('Informe o gênero da obra: ')
    classificacao = input ('Informe a classificação da obra: ')
    duracao = input ('Informe a duração da obra: ')
    ano = input ('Informe o ano de lançamento da obra: ')
    diretor = input ('Informe o nome do Diretor(a) da obra: ')

    nova_obra = Obra(nome, categoria, duracao, ano, diretor, classificacao, genero)
    print(f'\nObra "{nome}" adicionada com sucesso!')
    voltar_ao_menu_principal()

def exibir_detalhes_da_obra(obra):
    print(f"\nNome: {obra.nome}")
    print(f"Categoria: {obra.categoria}") 
    print(f"Gênero: {obra.genero}")
    print(f"Classificação: {obra.classificacao}")
    print(f"Duração: {obra.duracao} minutos")
    print(f"Ano: {obra.ano}")
    print(f"Diretor(a): {obra.diretor}")


def listar_obras():
    obras = Obra.obras 
    print("\nLista de obras cadastradas:\n")
    print('★ ' * 20)
    for obra in obras:
        exibir_detalhes_da_obra(obra)
        print()
        print('★ ' * 20)
    voltar_ao_menu_principal()


def buscar_obras():
    buscar = input('Digite o nome da obra que deseja buscar: ')
    for obra in Obra.obras:
        if buscar.lower() in obra.nome.lower():
            print(f'Obra encontrada: {obra.nome}')
            exibir_detalhes_da_obra(obra)
    voltar_ao_menu_principal()
    
def editar_obras():
    editar = input('Digite o nome da obra que deseja editar: ')
    for obra in Obra.obras:
        if editar.lower() in obra.nome.lower():
            print(f'Obra encontrada: {obra.nome}')
            exibir_detalhes_da_obra(obra)
            print("\nPressione Enter para manter a informação atual da obra.\n")
                
            novo_nome = input('Digite o novo nome da obra (ou pressione Enter para manter): ')
            if novo_nome:
                obra.nome = novo_nome
            nova_categoria = input('Digite a nova categoria da obra (ou pressione Enter para manter): ')
            if nova_categoria:
                obra.categoria = nova_categoria
            novo_genero = input('Digite o novo gênero da obra (ou pressione Enter para manter): ')
            if novo_genero:
                obra.genero = novo_genero
            nova_classificacao = input('Digite a nova classificação da obra (ou pressione Enter para manter): ')
            if nova_classificacao:
                obra.classificacao = nova_classificacao
            nova_duracao = input('Digite a nova duração da obra (ou pressione Enter para manter): ')
            if nova_duracao:
                obra.duracao = nova_duracao
            novo_ano = input('Digite o novo ano de lançamento da obra (ou pressione Enter para manter): ')
            if novo_ano:
                obra.ano = novo_ano
            novo_diretor = input('Digite o novo nome do Diretor(a) da obra (ou pressione Enter para manter): ')
            if novo_diretor:
                obra.diretor = novo_diretor
            print(f'Obra "{obra.nome}" editada com sucesso!')
            voltar_ao_menu_principal()

def remover_obra():
    remover = input('Digite o nome da obra que deseja remover: ')
    for obra in Obra.obras:
        if remover.lower() in obra.nome.lower():
            print(f'Obra encontrada: {obra.nome}')
            exibir_detalhes_da_obra(obra)
            Obra.obras.remove(obra)
            print(f'Obra "{obra.nome}" removida com sucesso!')
            voltar_ao_menu_principal()

def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()

def exibir_ajuda():
    print('\n🆘  AJUDA DO SNAKE BOXD\n')
    print(' ✦ 1. ➕ Adicionar uma nova obra: Cadastre um novo filme ou animação.')
    print(' ✦ 2. 📋 Listar obras: Veja todas as obras cadastradas.')
    print(' ✦ 3. 🔍 Buscar obra: Encontre uma obra pelo nome.')
    print(' ✦ 4. ✏️ Editar obra: Modifique os detalhes de uma obra existente.')
    print(' ✦ 5. ❌ Remover obra: Exclua uma obra do catálogo.')
    print(' ✦ 6. ❓ Ajuda: Exibe este menu de ajuda.')
    print(' ✦ 7. 🚪 Sair: Fecha o programa.\n')
    print('No menu, digite o número da opção desejada.')
    
    input('Pressione Enter para voltar ao menu principal.')

def finalizar_app():
    print('Saindo do programa. Até mais!')

def salvar_obras_em_json():
    with open('obras.json', 'w', encoding='utf-8') as f:
        lista = [
            {
                'nome': obra.nome,
                'categoria': obra.categoria,
                'genero': obra.genero,
                'classificacao': obra._classificacao,
                'duracao': obra.duracao,
                'ano': obra.ano,
                'diretor': obra.diretor
            }
            for obra in Obra.obras
        ]
        json.dump(lista, f, ensure_ascii=False, indent=4)

def carregar_obras_json():
    try:
        with open('obras.json', 'r', encoding= 'utf-8') as f:
            lista = json.load(f)
            for item in lista:
                Obra(**item)
    except FileNotFoundError:
        pass