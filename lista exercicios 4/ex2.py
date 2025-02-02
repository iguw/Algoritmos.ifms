# Exercício 2: Soma de Números em uma Lista Aninhada

# Implemente uma função recursiva chamada soma_lista_aninhada(lista) que calcula a soma de todos os números em uma lista, mesmo que os números estejam dentro de sublistas (listas aninhadas).
# Exemplo de Entrada:
# soma_lista_aninhada([1, [2, 3], [4, [5]]])
# Saída Esperada:
# 15 # (1 + 2 + 3 + 4 + 5)
# Dica: Verifique se o elemento atual é uma lista ou um número para decidir se deve continuar a recursão.

lista = [1, [2, 3], [4, [5]]]

soma_lista_aninhada(lista)