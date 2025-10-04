# if / elif / else
# se / se não se / se não

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Este é o bloco 1.')
elif condicao2:
    print('Este é o bloco 2.')
elif condicao3:
    print('Este é o bloco 3.')
elif condicao4:
    print('Este é o bloco 4.')
else: 
    print('[ERRO]')

# Em um bloco composto de if elif e else, apenas uma condição
# Será executada e depois ele pula o bloco de código.
print('FORA DOS BLOCOS')
