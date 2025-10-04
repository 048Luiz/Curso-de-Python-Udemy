"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamente
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = listas[1] (CRUD)
"""
#         0   1   2   3   4
#        -5  -4  -3  -2  -1 
lista = [10, 20, 30, 40, 50]

# lista[2] = 200
# del lista[1]
# print(lista)
# print(lista[3])

lista.append(60)
lista.append(70)
lista.append(80)
ultimo_valor = lista.pop(3)
print(lista,'removido:', ultimo_valor)

