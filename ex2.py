""" 
Explicação da estratégia: 
    OBS: Este exerício é baseado no exercício 1. A Alteração aqui é na criação do tabuleiro, para atingir o requisito NxN.
    O usuário deve informar o número de linhas/colunas desejado. Esse valor é usado para a criação do tabuleiro.

    Realizadas validações dentro de uma lista multidimensional (listas dentro de uma lista) para validar se a linha e a coluna informada por cada jogador existe. 
        caso a linha / coluna exista:
            É preenchida a posição no tabuleiro, realizada a verificação de vitória ou empate. Caso hum dos dois tenha ocorrido:
                Jogo é encerrado.
            Caso contrário:
                Jogador é alterado e é solicitada uma nova entrada.
        Caso contrário:
            entrada é inválida e é solicitada uma nova entrada válida que exista no tabuleiro

Detalhamento das estruturas usadas: Para construir o tabuleiro, foram utilizadas listas dentro de uma lista principal, representando o tabuleiro
"""
tamanho_tabuleiro = 0

def imprimir_tabuleiro(tabuleiro):
    """Imprime o tabuleiro

    Args:
        tabuleiro (list): Lista de linhas que também são listas com os valores preenchidos nas colunas, populadas com o valor " ", "X" ou "O"
    """
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 14)

def verificar_vitoria(tabuleiro, jogador):
    """Verifica se o Jogador venceu o jogo

    Para todas as condições, foi utilizada a função all() do python, para verificar se todos os elementos da iteração atendiam aos critérios validados
    1º IF - Valida se o jogador venceu em todas as casas em uma linha (horizontal)
    2º - Valida se o jogador venceu em todas as casas em uma coluna (vertical)
    3º - Valida nos quadrantes diagonais se o jogador ganhou ou não

    Args:
        tabuleiro (list): Lista multidimensional representando o tabuleiro
        jogador (str): string representando o jogador (valores possíveis: "X" ou "O")

    Returns:
        bool: Valor booleano representando vitória ou derrota
    """
#   [
#       [' ', ' ', ' ', ' '],
#       [' ', ' ', ' ', ' '],
#       [' ', ' ', ' ', ' '],
#       [' ', ' ', ' ', ' ']
#   ]
    for linha in tabuleiro:
        if all(casa == jogador for casa in linha):
            return True

    for coluna in range(tamanho_tabuleiro):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(tamanho_tabuleiro)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(tamanho_tabuleiro)) or all(tabuleiro[i][(tamanho_tabuleiro - 1) - i] == jogador for i in range(tamanho_tabuleiro)):
        return True

    return False

def verificar_empate(tabuleiro):
    """Verifica se o jogo empatou, ou seja, todas as casas estão preenchidas (a função é chamada após verificar que não ocorreu vitória)

    Args:
        tabuleiro (list): o tabuleiro

    Returns:
        bool: Valor booleano indicando se o jogo terminou em empate ou não ou não
    """
    return all(casa != " " for linha in tabuleiro for casa in linha)

def jogar_jogo_da_velha():

    while True:
        global tamanho_tabuleiro
        tamanho_tabuleiro = int(input(f"Informe o número de colunas e linhas do seu tabuleiro: "))
        if tamanho_tabuleiro < 3:
            print("O número deve ser maior ou igual a 3.")
        else:
            break

    tabuleiro = [[" " for i in range(tamanho_tabuleiro)] for i in range(tamanho_tabuleiro)]
    jogador_atual = "X"

    while True:
        imprimir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (1-{tamanho_tabuleiro}): "))
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (1-{tamanho_tabuleiro}): "))

        if 0 <= (linha - 1) <= (tamanho_tabuleiro - 1) and 0 <= (coluna - 1) <= (tamanho_tabuleiro - 1) and tabuleiro[(linha - 1)][(coluna - 1)] == " ":
            tabuleiro[(linha - 1)][(coluna - 1)] = jogador_atual

            if verificar_vitoria(tabuleiro, jogador_atual):
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                break
            elif verificar_empate(tabuleiro):
                imprimir_tabuleiro(tabuleiro)
                print("O jogo terminou em empate!")
                break
            else:
                if jogador_atual == "X":
                    jogador_atual = "O"
                else:
                    jogador_atual = "X"
        else:
            print("Movimento inválido. Tente novamente.")

if __name__ == "__main__":
    jogar_jogo_da_velha()