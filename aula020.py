valor_1 = input('Digite um valor: ')
valor_2 = input('Digite outro valor: ')

valor_1_int = int(valor_1)
valor_2_int = int(valor_2)

if valor_1_int > valor_2_int: 
    print(f'O valor {valor_1_int} é maior que o valor {valor_2_int}.')
elif valor_1_int < valor_2_int:
    print(f'O valor {valor_1_int} é menor que o valor {valor_2_int}.')
else:
    print(f'Os valores {valor_1_int} e {valor_2_int} são iguais.')
