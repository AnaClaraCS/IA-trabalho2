from board_game import BoardGame
import numpy as np

class Breakthrough(BoardGame):
    def __init__(self, rows=8, cols=8):
        super().__init__(rows,cols)
        # Conjunto com as posições iniciais das peças dos jogadores
        #Jogador X ocupa as linhas 0 e 1
        self.pecas_jogadorX = [(c,l) for c in range(cols) for l in range(0,1)]
        # Jogador O ocupa as ultimas duas linhas
        self.pecas_jogadorO = [(c,l) for c in range(cols) for l in range(rows-1,rows)]

    def available_moves(self):
        movimentos = []
        if self.current == 'X':
            # Jogador X pode mover para baixo ou diagonalmente
            for c,l in self.pecas_jogadorX:
                if c+1 < self.cols and (c+1, l) not in self.pecas_jogadorO:
                    movimentos.append(((c,l), "frente"))
                if c+1 < self.cols and l+1 < self.rows:
                    movimentos.append(((c,l), "direita"))
                elif c+1 < self.cols and l-1 >= 0:
                    movimentos.append(((c,l), "esquerda"))
                return movimentos
        elif self.current == 'O':
            # Jogador O pode mover para cima ou diagonalmente
            for c,l in self.pecas_jogadorO:
                if c-1 >= 0 and (c-1, l) not in self.pecas_jogadorX:
                    movimentos.append(((c,l), "frente"))
                if c-1 >= 0 and l+1 < self.rows:
                    movimentos.append(((c,l), "direita"))
                elif c-1 >= 0 and l-1 >= 0:
                    movimentos.append(((c,l), "esquerda"))
                return movimentos
        
    def make_move(self, peca, move):
        if self.current == 'X':
            if move=="frente" and self.board[peca[0]][peca[1]+1] == ' ':
                self.board[peca[0]][peca[1]] = ' '
                self.board[peca[0]][peca[1]+1] = 'X'
                self.pecas_jogadorX.remove(peca)
                self.pecas_jogadorX.append((peca[0], peca[1]+1))
                return True
            if move=="direita":
                if self.board[peca[0]+1][peca[1]+1] == '0':
                    self.pecas_jogadorO.remove((peca[0]+1, peca[1]+1))
                self.board[peca[0]][peca[1]] = ' '
                self.board[peca[0]+1][peca[1]+1] = 'X'
                self.pecas_jogadorX.remove(peca)
                self.pecas_jogadorX.append((peca[0]+1, peca[1]+1))
                return True
            elif move=="esquerda":
                if self.board[peca[0]+1][peca[1]-1] == '0':
                    self.pecas_jogadorO.remove((peca[0]+1, peca[1]-1))
                self.board[peca[0]][peca[1]] = ' '
                self.board[peca[0]+1][peca[1]-1] = 'X'
                self.pecas_jogadorX.remove(peca)
                self.pecas_jogadorX.append((peca[0]+1, peca[1]-1))
                return True

        elif self.current == 'O':
            if move=="frente" and self.board[peca[0]][peca[1]-1] == ' ':
                self.board[peca[0]][peca[1]] = ' '
                self.board[peca[0]][peca[1]-1] = 'X'
                self.pecas_jogadorX.remove(peca)
                self.pecas_jogadorX.append((peca[0], peca[1]-1))
                return True
            if move=="direita":
                if self.board[peca[0]+1][peca[1]-1] == '0':
                    self.pecas_jogadorO.remove((peca[0]+1, peca[1]-1))
                self.board[peca[0]][peca[1]] = ' '
                self.board[peca[0]+1][peca[1]-1] = 'X'
                self.pecas_jogadorX.remove(peca)
                self.pecas_jogadorX.append((peca[0]+1, peca[1]-1))
                return True
            elif move=="esquerda":
                if self.board[peca[0]+1][peca[1]-1] == '0':
                    self.pecas_jogadorO.remove((peca[0]+1, peca[1]-1))
                self.board[peca[0]][peca[1]] = ' '
                self.board[peca[0]+1][peca[1]-1] = 'X'
                self.pecas_jogadorX.remove(peca)
                self.pecas_jogadorX.append((peca[0]+1, peca[1]-1))
                return True

        return False

    def winner(self):
        if self.current == 'X':
            for p in self.pecas_jogadorX:
                if p[1] == self.rows - 1:
                    return 'X'
        else:
            for p in self.pecas_jogadorO:
                if p[1] == 0:
                    return 'O'
        return None
