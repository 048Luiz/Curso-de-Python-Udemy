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
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)
