from board_game import BoardGame
import numpy as np

class Breakthrough(BoardGame):
    def __init__(self, rows=8, cols=8):
        super().__init__(rows,cols)
        # Conjunto com as posições iniciais das peças dos jogadores
        self.inicializar_tabuleiro()

    def inicializar_tabuleiro(self):
        for i in range(self.cols):
            # Jogador X ocupa as duas primeiras linhas
            self.board[0][i] = 'X'
            self.board[1][i] = 'X'
            # Jogador O ocupa as duas últimas linhas
            self.board[self.rows-2][i] = 'O'
            self.board[self.rows-1][i] = 'O'

            # Preenche o restante do tabuleiro com espaços vazios
            for j in range(2, self.rows-2):
                self.board[j][i] = ' '
            

    def available_moves(self):
        movimentos = []
        for l in range(self.rows):
            for c in range(self.cols):
                if self.board[l][c] == self.current:
                    # Jogador X se move para baixo e O para cima
                    nova_linha = l+1 if self.current == 'X' else l-1
                    # Verifica se a nova linha está dentro dos limites do tabuleiro 
                    if nova_linha in range(self.rows): 
                        # Verifica se a peça pode se mover para frente
                        if self.board[nova_linha][c] == ' ': # Deve estar vazio
                            movimentos.append((l, c, "frente"))
                        # Verifica se a peça pode se mover para a direita
                        if c+1 < self.cols and self.board[nova_linha][c + 1] != self.current:
                            movimentos.append((l, c, "direita"))
                        # Verifica se a peça pode se mover para a esquerda
                        if  c > 0 and self.board[nova_linha][c - 1] != self.current:
                            movimentos.append((l, c, "esquerda"))
        return movimentos
        
        
    def make_move(self, move):
        l = move[0]
        c = move[1]
        movimento = move[2]
        # Jogador X se move para baixo e O para cima
        nova_linha = l+1 if self.current == 'X' else l-1

        if movimento == "frente":
            # Só pode se mover para frente se estiver vazio
            if nova_linha in range(self.rows) and self.board[nova_linha][c] == ' ':
                self.board[l][c] = ' '
                self.board[nova_linha][c] = self.current
                self.current = 'O' if self.current == 'X' else 'X'
                return True
            else:
                self.current = 'O' if self.current == 'X' else 'X'
                return False
        else:
            nova_coluna = c+1 if movimento == "direita" else c-1
            # Pode se mover na diagonal se estiver vazio ou ocupado pelo oponente
            if nova_coluna in range(self.cols) and self.board[nova_linha][nova_coluna] != self.current:
                self.board[l][c] = ' '
                self.board[nova_linha][nova_coluna] = self.current
                self.current = 'O' if self.current == 'X' else 'X'
                return True
            else:
                self.current = 'O' if self.current == 'X' else 'X'
                return False
           
    def winner(self):
        for c in range(self.cols):
            # Verifica se tem alguma peça do jogador O na primeira linha
            if self.board[0][c] == 'O':
                return 'O'
            # Verifica se tem alguma peça do jogador X na última linha
            if self.board[self.rows-1][c] == 'X':
                return 'X'
        
        # Um jogador ganha se o outro fica sem peças
        if not any('X' in row for row in self.board):
            return 'O'
        if not any('O' in row for row in self.board):
            return 'X'
        return None
