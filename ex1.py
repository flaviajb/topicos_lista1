
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 14)

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(casa == jogador for casa in linha):
            return True

    for coluna in range(4):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(4)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(4)) or all(tabuleiro[i][3 - i] == jogador for i in range(4)):
        return True

    return False

def verificar_empate(tabuleiro):
    return all(casa != " " for linha in tabuleiro for casa in linha)

def jogar_jogo_da_velha():
    tabuleiro = [[" " for i in range(4)] for i in range(4)]
    jogador_atual = "X"

    while True:
        imprimir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (1-4): "))
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (1-4): "))

        if 0 <= (linha - 1) <= 3 and 0 <= (coluna - 1) <= 3 and tabuleiro[(linha - 1)][(coluna - 1)] == " ":
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