"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamente
Métodos úteis:

append - Adiciona um item ao final
insert - Adiciona um item ao índice escolhido 
pop - Remove um item do final ou do índice escolhido
del - apaga um índice
clear - limpa a lista
extend - estende a lista
+ - concatena as listas

Create Read Update   Delete
Criar, ler, alterar, apagar = listas[1] (CRUD)
"""

#         0   1   2   3   4
#        -5  -4  -3  -2  -1 
lista = [10, 20, 30, 40, 50]
lista.append('Luiz')
nome = lista.pop()
lista.append(1234)
del lista[-1]
# lista.clear()
lista.insert(0, 5) 
# primeiro argumento índice 
# Segundo argumento o que eu quero adicionar
print(lista[6])