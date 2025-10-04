"""
Exercício
Exiba os índices da lista
"""

lista = ['Luiz', 'Maria', 'João']
lista.append('Roger')
indice = range(len(lista))
for numero in indice:
    print(numero, lista[numero], type(lista[numero]))