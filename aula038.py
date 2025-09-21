"""
Repetições (enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> Quando um código não tem fim
"""


contador = 0

while contador <= 100:
    contador += 1

    if contador > 10 and contador < 15:
        continue

    print(contador)

    if contador == 25:
        break
