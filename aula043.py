frase = 'O python é uma linguagem de programação ' \
'multiparadigma. ' \
'Python foi criado por Guido van Rossum.'

i = 0
qntd_apareceu_mais = 0
letra_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue

    qntd_atual = frase.count(letra_atual)

    if qntd_apareceu_mais < qntd_atual:
        qntd_apareceu_mais = qntd_atual
        letra_apareceu_mais = letra_atual

    i += 1


print(f'A letra que apareceu mais vezes foi: "{letra_apareceu_mais}" \nApareceu um total dê: {qntd_apareceu_mais}x')