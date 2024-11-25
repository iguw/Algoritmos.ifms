def verificar_sudoku(tabuleiro):
    for linha in tabuleiro:
        if not verificar_unicidade(linha):
            return False
    
    for col in range(9):
        coluna = [tabuleiro[row][col] for row in range(9)]
        if not verificar_unicidade(coluna):
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrade = [tabuleiro[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not verificar_unicidade(subgrade):
                return False
    return True

def verificar_unicidade(grupo):

    grupo = [x for x in grupo if x != 0]
    return len(grupo) == len(set(grupo))

tabuleiro_sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

if verificar_sudoku(tabuleiro_sudoku):
    print("O tabuleiro de Sudoku é válido!")
else:
    print("O tabuleiro de Sudoku não é válido!")