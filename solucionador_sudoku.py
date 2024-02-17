"""
Módulo para resolver Sudoku usando o algoritmo de backtracking.

Funções:
    - procurar_proximo_vazio(puzzle)
    - validador(puzzle, valor, linha, coluna)
    - resolver_sudoku(puzzle)
"""
def procurar_proximo_vazio(puzzle):
    """
    Procura a próxima célula vazia (-1) no Sudoku.

    Args:
        puzzle: Uma lista de listas representando o Sudoku.

    Returns:
        Uma tupla (linha, coluna) da próxima célula vazia, ou (None, None) se não houver nenhuma.
    """
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == -1:
                return i, j
    return None, None


def validador(puzzle, valor, linha, coluna):
    """
    Valida se o valor pode ser colocado na célula indicada.

    Args:
        puzzle: Uma lista de listas representando o Sudoku.
        valor: O valor a ser validado.
        linha: A linha da célula.
        coluna: A coluna da célula.

    Returns:
        True se o valor é válido, False caso contrário.
    """
    valor_linha = puzzle[linha]
    if valor in valor_linha:
        return False

    valor_coluna = [puzzle[i][coluna] for i in range(9)]
    if valor in valor_coluna:
        return False

    linha_inicial = (linha // 3) * 3
    coluna_inicial = (linha // 3) * 3

    for i in range(linha_inicial, linha_inicial + 3):
        for r in range(coluna_inicial, coluna_inicial + 3):
            if puzzle[i][r] == valor:
                return False


def resolver_sudoku(puzzle):
    """
    Resolve o Sudoku usando o algoritmo backtracking.

    Args:
        puzzle: Uma lista de listas representando o Sudoku.

    Returns:
        True se o Sudoku foi resolvido, False caso contrário.
    """
    linha, coluna = procurar_proximo_vazio(puzzle)
    if linha is None:
        return True

    for valor in range(1, 10):
        if validador(puzzle, valor, linha, coluna):
            puzzle[linha][coluna] = valor
            if resolver_sudoku(puzzle):
                return True
        puzzle[linha][coluna] = -1
    return False


sudoku_exampleFalse = [
    [5, 3, -1, -1, 7, -1, -1, -1, -1],
    [6, -1, -1, 1, 9, 5, -1, -1, -1],
    [-1, 9, 8, -1, -1, -1, -1, 6, -1],
    [8, -1, -1, -1, 6, -1, -1, -1, 3],
    [4, -1, -1, 8, -1, 3, -1, -1, 1],
    [7, -1, -1, -1, 2, -1, -1, -1, 6],
    [-1, 6, -1, -1, -1, -1, 2, 8, -1],
    [-1, -1, -1, 4, 1, 9, -1, -1, 5],
    [-1, -1, -1, -1, 8, -1, -1, 7, 9],
]

sudoku_exampleTrue = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
]

if __name__ == "__main__":
    print(resolver_sudoku(sudoku_exampleFalse))
    print(sudoku_exampleFalse)


print(resolver_sudoku(sudoku_exampleTrue))
print(sudoku_exampleTrue)
