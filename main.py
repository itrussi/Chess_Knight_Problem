from time import time
from os import system
import logging

global logger

logging.basicConfig(
    filename='main.log',
    level=logging.INFO,
    format=
    '%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s'
)

logger = logging.getLogger(__name__)

class Solver:

    __slots__ = "chessboard", "solution", "moves"
    
    def __init__(self):
        self.chessboard = [[0 for _ in range(8)] for _ in range(8)]
        self.solution = [[0, 0]]

        self.moves =((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))

    def begin(self):
        self.chessboard[0][0] = 1
        
        if self.iterate(2, 0, 0) == True:
            return True
            
        else:
            return False

    def iterate(self, counter, x, y):
        if counter == 64:
            return True

        possible_moves = self.get_moves(x, y)
        
        for move in possible_moves:

            system('clear')
            self.print_board()
            print("\n")

            attempt_x = move[0]
            attempt_y = move[1]
                
            self.chessboard[attempt_x][attempt_y] = counter
            self.solution.append([attempt_x, attempt_y])

            logger.info(f"Moved to ({attempt_x}, {attempt_y}) from ({x}, {y})")
                
            if self.iterate(counter+1, attempt_x, attempt_y) == True:
                return True

            try:
                self.solution.pop()
                    
            except:
                continue
                    
            finally:
                self.chessboard[attempt_x][attempt_y] = 0
                logger.info(f"Backtracked from ({attempt_x}, {attempt_y}) to ({x}, {y})")

        return False

    def validate(self, x, y):
        if (x >= 0 and x < 8 and y >= 0 and y < 8 and self.chessboard[x][y] == 0):
            return True
        else:
            return False

    def get_moves(self, x, y):

        valid_moves = []
        
        for i in range(8):
            check_x = x + self.moves[i][0]
            check_y = y + self.moves[i][1]

            if self.validate(check_x, check_y) == True:
                valid_moves.append([check_x, check_y])

        return valid_moves

    def print_board(self):
        for y in range(8):
            for x in range(8):
                print(self.chessboard[x][y], end='  ')
            print()

        print("\n")
        print(f"Solution: {self.solution}")

s = Solver()
start = time()
s.begin()
s.print_board()
end = time()
print("\n")
print(end - start)
