# Exercício 4: Encontrar o Índice do Maior Elemento
# Escreva uma função recursiva chamada indice_maior_elemento(lista) que retorna o
# índice do maior elemento em uma lista.
# Exemplo de Entrada:
# indice_maior_elemento([1, 5, 3, 9, 2])
# Saída Esperada:
# 3 # O maior elemento é 9, que está no índice 3
def indice_maior_elemento(lista, indice=0, max_indice=0):
    if indice == len(lista):
        return max_indice
    return indice_maior_elemento(lista, indice + 1, indice if lista[indice] > lista[max_indice] else max_indice)

print(indice_maior_elemento([1, 5, 3, 9, 2]))