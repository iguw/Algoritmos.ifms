# Filtrar números pares de uma lista (com filter)
# Escreva uma função que, utilizando filter e uma função lambda, receba uma lista
# de números inteiros e retorne apenas os números pares.
# Exemplo de entrada: [1, 2, 3, 4, 5]
# Exemplo de saída: [2, 4]

numeros = [1, 2, 3, 4, 5]

numeros_pares = list(filter(lambda x : x % 2 == 0, numeros))

print(numeros_pares)