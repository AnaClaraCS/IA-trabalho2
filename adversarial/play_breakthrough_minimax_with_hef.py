import time
from colorama import Fore, Style, init

# Reinitialize colorama after reset
init(autoreset=True)

from minimax import minimax_with_hef
from breakthrough import Breakthrough

from helper_functions import print_board

# Heuristic Evaluation Function
def evaluate_breakthrough(board, player):
    opponent = 'O' if player == 'X' else 'X'
    score = 0
    linhas = len(board)
    colunas = len(board[0])
    chegada = linhas - 1 if player == 'X' else 0

    for l in range(linhas):
        for c in range(colunas):
            if board[l][c] == player:
                # Pontua por distância até a chegada
                dist = abs(l - chegada)  # Distância da peça até a linha de chegada
                score += ((linhas - dist) ** 2) * 2  # Quanto mais perto, maior a pontuação

                # Pontua por possibilidade de captura
                nova_linha = l+1 if player == 'X' else l-1
                if nova_linha in range(0,linhas) and (
                    (c-1 >= 0 and board[nova_linha][c-1] == opponent) 
                    or (c+1 <colunas and board[nova_linha][c+1] == opponent)):
                    score += 100

                # Pontua por peça estar no centro
                if 2 <= c <= 5:
                    score += 20
            #print(f"linha {l}, coluna {c}. Pontuação: {score}")
    return score



# AI Move Selector
def best_move(game, depth=4):
    '''
    Essa função determina a melhor jogada para a IA em um jogo de Connect Four,
    utilizando o algoritmo Minimax com uma função de avaliação heurística.
    Ela avalia todas as jogadas disponíveis e escolhe a que maximiza a pontuação
    heurística para o jogador atual, considerando a profundidade especificada.
    :param game: Instância do jogo Connect Four
    :param depth: Profundidade da busca Minimax
    :return: A melhor coluna para jogar
    '''
    player = game.current
    best_score = float('-inf')
    move_choice = None
    for move in game.available_moves():
        new_game = game.copy()
        new_game.make_move(move)
        # score = minimax_with_dls(new_game, depth - 1, False, player)
        score = minimax_with_hef(
            game=new_game,
            depth=depth - 1,
            maximizing=False,
            player=player,
            evaluate_fn=evaluate_breakthrough
        )
        if score > best_score:
            best_score = score
            move_choice = move
    return move_choice

# Replace Breakthrough.print_board with updated function
Breakthrough.print_board = lambda self: print_board(self.board, self.cols)

def play():
    game = Breakthrough()
    human = input("Escolha seu lado (X ou O): ").strip().upper()
    assert human in ['X', 'O']
    ai = 'O' if human == 'X' else 'X'

    while not game.game_over():
        game.print_board()
        if game.current == human:
            while True:
                try:
                    print(f"Sua jogada ({human})")
                    l = int(input(f"Escolha a linha: "))
                    c = int(input(f"Escolha a coluna: "))
                    movimento = input("Escolha o movimento (frente, esquerda, direita): ").strip().lower()
                    move = (l, c, movimento)
                    if move in game.available_moves():
                        game.make_move(move)
                        time.sleep(0.5)
                        break
                    else:
                        print("Movimento inválido. Tente novamente.")
                except ValueError:
                    print("Entrada inválida.")
        else:
            print("IA pensando...")
            move = best_move(game, depth=4)
            print(f"IA joga na coluna {move}")
            game.make_move(move)
            time.sleep(0.8)

    game.print_board()
    winner = game.winner()
    if winner == human:
        print(Fore.GREEN + "Você venceu!")
    elif winner == ai:
        print(Fore.RED + "A IA venceu.")
    else:
        print(Fore.CYAN + "Empate.")

def play_ai_vs_ai():
    game = Breakthrough()
    print("IA vs IA iniciando...")
    time.sleep(1)

    while not game.game_over():
        game.print_board()
        print(f"IA ({game.current}) pensando...")
        move = best_move(game, depth=4)
        print(f"IA ({game.current}) joga: {move}")
        game.make_move(move)
        time.sleep(0.8)

    game.print_board()
    winner = game.winner()
    if winner:
        print(Fore.YELLOW + f"A IA '{winner}' venceu!")
    else:
        print(Fore.CYAN + "Empate.")


if __name__ == "__main__":
    play_ai_vs_ai()