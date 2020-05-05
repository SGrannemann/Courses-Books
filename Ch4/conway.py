# Conway's Game of Life

import random, copy, time
WIDTH = 60
HEIGHT = 20

# Create a list of lists for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') # Add a living cell
        else:
            column.append('') # Add a dead cell
    nextCells.append(column) # nextCells is a list of column lists

while True: #Main program loop
    print('\n\n\n\n\n') # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or space
        print() # Print a new line at the of the row

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # '% WIDTH' ensures leftCoord is always between 0 and WIDTH -1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count numbers of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 #Top-Left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # top right alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # left neighbor alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # bottom left alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # bottom neighbor is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # bottom right is alive

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                #living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == '' and numNeighbors == 3:
                #Dead cells with three neighbors become alive
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ''
    time.sleep(1) #1 second pause.
