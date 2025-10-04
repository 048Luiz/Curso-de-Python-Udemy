# senha_salva = '123456'
# senha_digitada = ''
# tentativas = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Digite sua senha {tentativas}x: ')
#     tentativas += 1
    
# print(tentativas)
# print('O laço acima pode ter infinitas tentativas.')

texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')



