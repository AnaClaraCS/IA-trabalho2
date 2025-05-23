import time

from colorama import Fore, Style, init
init(autoreset=True)

from connect_four import ConnectFour, ROWS, COLS
from mcts import mcts
from helper_functions import print_board
from breakthrough import Breakthrough

def play():
    '''
    Main function to play the game
    '''
    game = Breakthrough()
    human = input("Escolha seu lado (X ou O): ").strip().upper()
    assert human in ['X', 'O']
    ai = 'O' if human == 'X' else 'X'

    while not game.game_over():
        print_board(game.board, COLS)
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
                        print("Coluna inválida ou cheia.")
                except ValueError:
                    print("Entrada inválida.")
        else:
            print("IA pensando...")
            move = mcts(game, iterations=200)
            print(f"IA joga na coluna {move}")
            game.make_move(move)
            time.sleep(0.5)

    print_board(game.board)
    winner = game.winner()
    if winner == human:
        print("Você venceu!")
    elif winner == ai:
        print("Você perdeu!")
    else:
        print("Empate.")

def play_ai_vs_ai():
    game = Breakthrough()
    print("IA vs IA iniciando...")
    time.sleep(1)

    while not game.game_over():
        game.print_board()
        print(f"IA ({game.current}) pensando...")
        move = mcts(game, iterations=200)
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
