# Filtrar tuplas com média maior que 5
# Escreva uma função que receba uma lista de tuplas, onde cada tupla contém
# números inteiros. Utilize map e filter para filtrar as tuplas cuja média dos valores
# seja maior que 5.
# Exemplo de entrada: [(2, 8), (4, 5, 6), (1, 2)]
# Exemplo de saída: [(2, 8), (4, 5, 6)]

tuplas = [(2, 8), (4, 5, 6), (1, 2)]

tuplas_media = list(map(lambda x: (x, sum(x) / len(x)), tuplas))
print(tuplas_media)

resultado = list(filter(lambda t: t[1] > 5, tuplas_media))

tuplas_filtradas = [t[0] for t in resultado]
print(tuplas_filtradas)