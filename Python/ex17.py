def negativos(lista):
    negativos = [x for x in lista if x < 0]
    positivos = [x for x in lista if x >= 0]
    return negativos + positivos


numeros = list(map(int, input("digite uma lista de números separados por espaço: ").split()))
lista_ordenada = negativos(numeros)

print(f"Lista reorganizada: {lista_ordenada}")
