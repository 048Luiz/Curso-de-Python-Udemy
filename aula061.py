"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = 'Olha    só   que,    coisa     interessante'
lista_frases_antiga = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_antiga):
    lista_frases.append(lista_frases_antiga[i].strip())

frases_unidas = '-'.join(lista_frases)

print(lista_frases_antiga)
print(lista_frases)
print(frases_unidas)