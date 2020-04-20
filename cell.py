
class Cell(object):

    """A cell class"""

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__neighbours = []

    def store_neighbours(self, neighbours):
        #store live neighbouring cells
        self.__neighbours = neighbours

    
    def get_dead_neighbours(self):

        cells = [Cell(self.__x-1, self.__y-1),
                Cell(self.__x-1, self.__y),
                Cell(self.__x-1, self.__y+1),
                Cell(self.__x, self.__y+1),
                Cell(self.__x+1, self.__y+1),
                Cell(self.__x+1, self.__y),
                Cell(self.__x+1, self.__y-1)
                ]
        
        dead_neighbours_list = []
        for cell in cells:
            matched_live_neighbour = False
            for live_neighbuour in self.__neighbours:
                if live_neighbuour.is_me(cell) == True:
                    matched_live_neighbour = True
                    break
            if matched_live_neighbour == False:
                dead_neighbours_list.append(cell)

        return dead_neighbours_list

    def print_neighbours(self):
        neighbour_string = ""
        for neighbour in self.__neighbours:
            neighbour_string += "({0},{1}),".format(neighbour.x, neighbour.y)

        print("({0}, {1}) has neighbours {2}".format(self.x, self.y, neighbour_string))

    @property
    def is_live_next_iteration(self):
        #Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        #Any live cell with two or three live neighbours lives on to the next generation.
        #Any live cell with more than three live neighbours dies, as if by overpopulation.       


        if len(self.__neighbours) < 2 or len(self.__neighbours) > 3:
            return False
        else:
            return True

    @property
    def will_be_born_next_iteration(self):
        #Any ded cell with exactly three neighbours will come alive

        if len(self.__neighbours) == 3:
            return True
        else:
            return False


    def is_me(self, cell):
        if self.__x == cell.x and self.__y == cell.y:
            return True #its me!
        else:
            return False

    def is_neighbour(self, x, y):

        if self.__x == x and self.__y == y:
            return False #its me!
        if abs(self.__x - x) <= 1 and abs(self.y - y) <= 1:
            return True
        else:
            return False
        

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


        