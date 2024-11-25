def filtrar_numeros(lista):
    return [numero for numero in lista if numero % 2 == 0]


numeros = list(map(int, input("digite uma lista de números inteiros separados por espaço: ").split()))


pares = filtrar_numeros(numeros)
print(f"Lista com números pares: {pares}")