def soma_coluna(matriz, coluna):
    soma = 0
    for linha in matriz:
        soma += linha[coluna]
    return soma
    
matriz = [[0, 0],[0, 0]]
for l in range(0, 2):
    for c in range(0, 2):
        matriz[l][c] = int(input(f'digite um valor para [{l}, {c}]: '))

for l in range(0, 2):
    for c in range(0, 2):
        print(f'[{matriz [l][c]:^5}]', end='')
    print()

coluna_escolhida = 1
resultado = soma_coluna(matriz, coluna_escolhida)

print(f'a soma da coluna {coluna_escolhida} é {resultado}')