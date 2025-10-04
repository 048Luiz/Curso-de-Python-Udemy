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

usuario = input('Usuário: ')
senha = input('Senha: ')
usuario_correto = 'admin'
senha_correta = 'admin'

# if condição: Só é executado se for True

if usuario == usuario_correto and senha == senha_correta:
    print('Entrada permitida.')
else: 
    print('[ERRO] Dados incorretos! Preencha novamente.')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)
print(bool(0.0))
print(bool(''))
