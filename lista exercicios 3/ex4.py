# Nomes com mais de 5 letras (com filter)
# Escreva uma função que receba uma lista de nomes e, utilizando filter, retorne
# apenas os nomes com mais de 5 letras.
# Exemplo de entrada: ["Ana", "Lucas", "Fernanda", "João"]
# Exemplo de saída: ["Lucas", "Fernanda"]

lst = ["Ana", "Lucas", "Fernanda", "João"]

maiores_nomes = list(filter(lambda x: len(x) >= 5, lst))

print(maiores_nomes)