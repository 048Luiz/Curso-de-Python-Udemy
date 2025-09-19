"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro,  informe que não é um número inteiro.
"""
number = input('Digite um número inteiro: ')

try:
    even_odd_number = float(number)  
except ValueError:
    print('[ERRO] Tente um número inteiro!')
else:
    if even_odd_number % 2 == 0:
        print(f'O número {even_odd_number} é par!')
    else:
        print(f'O número {even_odd_number} é ímpar!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

receive = input('Digite a hora em números inteiros: ')

try:
    time = int(receive)

    if time >= 0 and time <= 11:
        print('Bom dia!')
    elif time >= 12 and time <= 17:
        print('Boa tarde!')
    elif time >= 18 and time <= 23:
        print('Boa noite!')
    else:
        print('Horário desconhecido. Tente novamente!')
except:
    print('[ERRO] Digite novamente!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreva "Seu nome é curto"; se tiver entre 5 a 6 letras, escreva
"Seu nome é médio"; maior que 6 escreva "Seu nome é grande."
"""

name = input('Digite seu nome: ')
size = len(name)

if size <= 4:
    print('Seu nome é um nome pequeno.')
elif size <= 6:
    print('Seu nome é um nome médio.')
else:
    print('Seu nome é um nome grande.')
