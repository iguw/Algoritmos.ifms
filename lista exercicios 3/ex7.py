# Agrupar números em categorias (com dicionários e lambdas)
# Escreva uma função que receba uma lista de números inteiros e utilize map e filter
# para criar um dicionário que agrupe os números em três categorias:
# o "positivos" (números maiores que 0)
# o "negativos" (números menores que 0)
# o "zeros" (números iguais a 0).
# o Exemplo de entrada: [1, -2, 0, 3, -5, 0]
# o Exemplo de saída: {"positivos": [1, 3], "negativos": [-2, -5], "zeros": [0, 0]}

vetor = [1, -2, 0, 3, -5, 0]
numero = list(map(lambda x: ('positivo', x) if x > 0 else ('negativo', x) if x < 0 else ('zero', x), vetor))

positivos = list(map(lambda x: x [1], filter(lambda x : x [0] == 'positivo', numero)))
negativos = list(map(lambda x: x [1], filter(lambda x : x [0] == 'negativo', numero)))
zero = list(map(lambda x: x [1], filter(lambda x : x [0] == 'zero', numero)))

dicionario = {
        'positivos': positivos,
        'negativos': negativos,
        'zero': zero
    }

print(f'positivos{positivos}, negativos{negativos}, zero{zero}')