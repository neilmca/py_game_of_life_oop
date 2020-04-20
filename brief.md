Game of Life Candidate Instructions

Brief from Wikipedia
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

Any live cell with two or three neighbors survives.
Any dead cell with three live neighbors becomes a live cell.
All other live cells die in the next generation. Similarly, all other dead cells stay dead.
The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.





The Game of Life is set in an infinite two-dimensional grid inhabited by “cells”. Every cell interacts with up to eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. 


From an initial seed grid the game "evolves" one iteration at a time. An iteration applies rules to the grid to determine its next state. These scenarios are:	


Scenario 0: 
No interactions 	
Given a game of life 	
When there are no live cells 	
Then on the next step there are still no live cells


Scenario 1: Underpopulation 	
Given a game of life 	
When a live cell has fewer than two neighbours 	
Then this cell dies


Scenario 2: Overcrowding 	
Given a game of life 	
When a live cell has more than three neighbours 	
Then this cell dies


Scenario 3: Survival 	
Given a game of life 	
When a live cell has two or three neighbours 	
Then this cell stays alive


Scenario 4: Creation of Life 	
Given a game of life 	
When an empty position has exactly three neighbouring cells 	
Then a cell is created in this position

When applied these scenarios result in the following:	

Scenario 5: Grid with no live cells 	
Given a game of life with the initial state containing no live cells 	
When the game evolves one turn 	Then the next state also contains no live cells

Scenario 6: Expected game outcome for seeded grid
Where `.` represents an empty cell, and `X` a live cell, 
Given a game of life with the initial state

```
...
000
...
```
When the game evolves one turn  	
Then the next state is
```
.0.
.0.
.0.
```
When the game evolves another turn  	
Then the next state is
```
...
000
...
```