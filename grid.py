

class Grid(object):
    """Grid class to hold live cells"""

    def __init__(self):
        self.__live_cells_list = []
        self.__game_iteration = 0


    @property
    def live_cells(self):
        return self.__live_cells_list


    def seed_game(self, cells):
        """intial seed for the game"""
        self.__live_cells_list = cells
        #calculate live neighbours for each cell and store in the cell
        self.store_live_neighbours(self.__live_cells_list)
        

    def store_live_neighbours(self,cells):

        for cell in cells:
            neighbours = []
            for neighbour in self.__live_cells_list:
                if cell.is_neighbour(neighbour.x, neighbour.y) == True:
                    neighbours.append(neighbour)
            cell.store_neighbours(neighbours)
        

    
    def neighbouring_cells_reproduced(self, cell):
        #look around this cell to see if any of its neighbours come to life

        self.__live_cells_list
        
        #get dead neighbours list
        dead_neighbours_list = cell.get_dead_neighbours()
        #into ech cell we store and live neighbours
        self.store_live_neighbours(dead_neighbours_list)
        born_cells = []
        for cell in dead_neighbours_list:
            if cell.will_be_born_next_iteration == True:
                born_cells.append(cell)

        return born_cells
    
    

    @property
    def print_grid(self):
        

        print("After {} iterations the live cells are at....".format(self.__game_iteration))
        for cell in self.__live_cells_list:
            cell.print_neighbours()


    @staticmethod
    def is_cell_in_list(cell_to_find, cell_list):
        for cell in cell_list:
            if cell.is_me(cell_to_find) == True:
                return True

        return False

    def run_game(self, iterations):

        self.print_grid

        self.__game_iteration = 1
        for i in range(0,iterations):

            next_iteration_live_cell_list = []

            #for each cell calculate if it is live or dead in next iteration
            for cell in self.__live_cells_list:
                if cell.is_live_next_iteration == True:
                    next_iteration_live_cell_list.append(cell)

                #determine if new cells arund it come to life 
                born_cells = self.neighbouring_cells_reproduced(cell)
                #de-dup before adding to list of new cells for next iteration
                for new_cell in born_cells:
                    if Grid.is_cell_in_list(new_cell, next_iteration_live_cell_list) == False:
                        next_iteration_live_cell_list.append(cell)



            
            self.__live_cells_list = next_iteration_live_cell_list
            self.store_live_neighbours(self.__live_cells_list)
            self.print_grid


            self.__game_iteration += 1

            

