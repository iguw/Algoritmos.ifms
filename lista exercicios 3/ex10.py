# 10. Média ponderada com dicionário e reduce
# Crie uma função que receba um dicionário onde as chaves são nomes de alunos e
# os valores são listas de notas (com pesos na última posição). A função deve calcular
# a média ponderada de cada aluno usando reduce e retornar um novo dicionário
# com os resultados.
# Exemplo de entrada:
# {
#  "João": [8, 7, 9, 2], # (notas: 8, 7, 9; peso: 2)
#  "Ana": [5, 6, 7, 3] # (notas: 5, 6, 7; peso: 3)
# }
# Exemplo de saída:
# {
#  "João": 8.0,
#  "Ana": 6.0
# }

from functools import reduce

def media_ponderada(alunos):
    return {aluno: reduce(lambda acc, nota: acc + nota * notas[-1], notas[:-1], 0) / len(notas[:-1]) for aluno, notas in alunos.items()}

entrada = {
    "João": [8, 7, 9, 2],
    "Ana": [5, 6, 7, 3]
}

saida = media_ponderada(entrada)
print(saida)