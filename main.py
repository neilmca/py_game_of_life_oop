import sys
from grid import Grid
from cell import Cell

def main(args):
    
   
    game = Grid()

    seed_cells = [Cell(0,0), Cell(1,1), Cell(0,-1)]

    game.seed_game(seed_cells)
    game.run_game(1)


if __name__ == "__main__":
   main(sys.argv[1:])

   