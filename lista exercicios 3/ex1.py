# Dobrar elementos de uma lista (com map)
# Escreva uma função que, utilizando map e uma função lambda, receba uma lista
# de números inteiros e retorne uma nova lista com todos os elementos dobrados.
# Exemplo de entrada: [1, 2, Exemplo de saída: [2, 4, 6, 8]

numeros = [1, 2, 3, 4]

numeros_dobrados = list(map(lambda x: x*2, numeros))

print(numeros_dobrados)