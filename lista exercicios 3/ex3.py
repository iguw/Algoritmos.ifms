# Somar os números de uma lista (com reduce)
# Crie uma função que, utilizando reduce e uma função lambda, receba uma lista de
# números inteiros e retorne a soma total dos números.
# Exemplo de entrada: [1, 2, 3, 4]
# Exemplo de saída: 10
from functools import reduce

lst = [1, 2, 3, 4]

soma = reduce(lambda x , y: x+y, lst)

print(soma)