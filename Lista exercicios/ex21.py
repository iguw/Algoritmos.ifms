def duplicados(lista):
    sem_duplicados = []
    for elemento in lista:
        if elemento not in sem_duplicados:
            sem_duplicados.append(elemento)
    return sem_duplicados


numeros = list(map(int, input("digite uma lista de números separados por espaço: ").split()))


nova_lista = duplicados(numeros)
print(f"Lista sem duplicados: {nova_lista}")