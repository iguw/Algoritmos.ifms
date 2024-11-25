def remover_duplicados(lista_aninhada):
    nova_lista = [list(set(sublista)) for sublista in lista_aninhada]
    return nova_lista


lista_aninhada = [
    [1, 2, 2, 3, 4],
    [5, 5, 6, 7, 7],
    [8, 8, 9, 9, 9]
]


resultado = remover_duplicados(lista_aninhada)

print("Lista de listas com valores únicos:")
for sublista in resultado:
    print(sublista)
