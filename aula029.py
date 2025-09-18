"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input('Digite um número para ver o dobro: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro dê {numero_float} é {numero_float * 2:.2f}.')
except:
    print('Isso não é um número!')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro dê {numero_float} é {numero_float * 2:.2f}.')
# else:
#     print('Isso não é um número!')
