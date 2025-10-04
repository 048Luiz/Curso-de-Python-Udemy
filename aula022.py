# Operadores lógicos
# and (e) or (ou) not (não)

# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc ja viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# usuario = input('Usuário: ')
# senha = input('Senha: ')

# # if condição: Só é executado se for True

# if usuario == 'admin' or usuario == 'Admin' and senha == 'admin' or senha == 'Admin':
#     print('Entrada permitida.')
# else: 
#     print('[ERRO] Dados incorretos! Preencha novamente.')

# Avaliação de curto circuito
senha = input('Senha: ') or '[ERRO] Digite sua senha para continuar'
print(senha)
