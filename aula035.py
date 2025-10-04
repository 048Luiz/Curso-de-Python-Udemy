"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
condition = True

while condition:
    name = input('Qual seu nome? ')

    if name == 'sair':
        break # encerra o bloco de comando.

    print(f'Seu nome é {name}!')

    break

print('Acabou!')