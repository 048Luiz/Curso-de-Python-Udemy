"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'João'), (2, 'Luiz'), (3, 'Helena')]
lista = ['Maria', 'João', 'Luiz']
lista.append('Helena')

for indice, nome in enumerate(lista):
    print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('For da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
