"""
Faça umam lista de comprar com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista de compras.
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""

import os

shopping_list = []

def clean_the_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print('\n---Selecione uma opção:---')
    option = input('\n[i]nserir [a]pagar [l]istar [s]air: ').lower()

    if option == 'i':
        clean_the_screen()
        item = input('\nDigite o item a ser inserido: ')
        shopping_list.append(item)
        print(f'\n"{item}" foi adicionado à lista.')

    elif option == 'a':
        try:
            index = int(input('\nDigite o índice do item que deseja excluir: '))
            item_removed = shopping_list.pop(index)
            print(f'\n\nItem: {item_removed}.\nFoi removido da lista.\n')
        except (ValueError, IndexError):
            print('\n[ERRO] Índice invalido! Tente novamente.')
    
    elif option == 'l':
        if not shopping_list:
            print('\nA lista de compras está vazia.')
        else:
            print('\nLista de compras:')
            for i, item in enumerate(shopping_list):
                print(f'{i}: {item}')
    
    elif option == 's':
        clean_the_screen()
        print('\nSaindo do programa. Até mais!')
        break
    
    else:
        print('\nOpção inválida! Tente novamente.')
