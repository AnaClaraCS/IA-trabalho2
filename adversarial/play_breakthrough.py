import time
import play_breakthrough_mcts
import play_breakthrough_minimax_with_hef

regras = '''
    Regras:
    * Peças: Cada jogador começa com duas fileiras de peças.
    * Movimentação: As peças podem avançar um passo à frente ou nas diagonais.
    * Captura: Uma peça só pode capturar a peça do adversário nas diagonais, e apenas uma por turno.
    * Condição de vitória: O jogador vence quando uma de suas peças alcança a última fileira do tabuleiro.
    * Condição de derrota: O jogador perde quando fica sem peças no tabuleiro.
    '''

modos_jogo = '''
    Modos de Jogo:

    * Minimax com Heurística
    1 - Jogar contra IA 
    2 - IA vs IA 

    * MCTS
    3 - Jogar contra IA 
    4 - IA vs IA 
    '''


def play():
    print("----- Bem-vindo ao jogo Breakthrough -----")
    print(regras)

    jogo = int(input(modos_jogo))

    match jogo:
        case 1:
            print("Você escolheu jogar contra a IA com Minimax.")
            time.sleep(0.5)
            play_breakthrough_minimax_with_hef.play()
        case 2:
            print("Você escolheu IA vs IA com Minimax.")
            time.sleep(0.5)
            play_breakthrough_minimax_with_hef.play_ai_vs_ai()
        case 3:
            print("Você escolheu jogar contra a IA com MCTS.")
            time.sleep(0.5)
            play_breakthrough_mcts.play()
        case 4:
            print("Você escolheu IA vs IA com MCTS.")
            time.sleep(0.5)
            play_breakthrough_mcts.play_ai_vs_ai()
        case _:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    play()
