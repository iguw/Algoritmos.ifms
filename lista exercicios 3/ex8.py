# Contar letras em uma lista de palavras (com map e reduce)
# Crie uma função que receba uma lista de palavras e retorne a soma total de letras
# em todas as palavras, utilizando map para contar as letras e reduce para somar.
# Exemplo de entrada: ["casa", "python", "lambda"]
# Exemplo de saída: 16
from functools import reduce

lst = ["casa", "python", "lambda"]
tamanho = list(map(len, lst))
somar = reduce(lambda ac, x: ac + x, tamanho, 0)

print(somar)