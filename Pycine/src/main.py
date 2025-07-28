import os
import sys

#força o Python a enxergar a pasta onde o main.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from interface import exibir_nome_do_programa, exibir_opcoes
from controlador import adicionar_obras, listar_obras, buscar_obras, editar_obras, remover_obra, exibir_ajuda, finalizar_app, opcao_invalida, carregar_obras_json, salvar_obras_em_json

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            adicionar_obras()
            salvar_obras_em_json()
        elif opcao_escolhida == 2: 
            listar_obras()
        elif opcao_escolhida == 3:
            buscar_obras()
        elif opcao_escolhida ==4:
            editar_obras()
            salvar_obras_em_json()
        elif opcao_escolhida == 5:
            remover_obra()
            salvar_obras_em_json()
        elif opcao_escolhida == 6:
            exibir_ajuda()
        elif opcao_escolhida == 7:
            finalizar_app()
            sys.exit()
        else: 
            opcao_invalida()
    except SystemExit:
        raise  # deixa passar para sair do programa
    except:
        opcao_invalida()

def main():
    carregar_obras_json()
    while True:
        os.system('cls')
        exibir_nome_do_programa()
        exibir_opcoes()
        escolher_opcao()

if __name__ == '__main__':
    main()