
# Solucionador de Sudoku

Este é um simples solucionador de Sudoku implementado em Python usando o algoritmo de backtracking.

## Como Usar

1. Clone o repositório para o seu sistema local:

    ```bash
    git clone https://github.com/seu-usuario/sudoku-solver.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd sudoku-solver
    ```

3. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    ```

4. Ative o ambiente virtual:

    - No Windows:

        ```bash
        venv\Scripts\activate
        ```

    - No Linux ou macOS:

        ```bash
        source venv/bin/activate
        ```

5. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

6. Execute o script do Sudoku Solver:

    ```bash
    python sudoku_solver.py
    ```

## Exemplos de Uso

- Sudoku exemplo com solução:

    ```python
    sudoku_example = [
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

    print(resolver_sudoku(sudoku_example))
    print(sudoku_example)
    ```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Autores

- [@eduardopetrocchi](https://www.github.com/eduardopetrocchi)

