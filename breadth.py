def main(chosenLevel):
    import turtle
    import sys
    import time
    from collections import deque
    import Tkinter as Tkinter 
      
    counter = 0
    counter2 = 0
    running = False
    window = turtle.Screen()
    window.reset()
    window.bgcolor("black") # window background color
    window.title("A.I. Maze Game") 
    window.setup(width = 1400, height = 820, startx = None, starty = None) # set up the turtle window width and height


    class Wall(turtle.Turtle): # this is Pen class, it will be called whenever you create pen object
        def __init__(self):   # this is a default constructor
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("light grey")
            self.penup()
            self.speed(0)

    class Green(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("green")
            self.penup()
            self.speed(0)

    class Yellow(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("circle")
            self.color("yellow")
            self.penup()
            self.speed(0)

    class Red(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("red")
            self.penup()
            self.speed(0)

    class Node():

        def __init__(self, parent=None, position=None):
            self.parent = parent
            self.position = position

            self.g = 0
            self.h = 0
            self.f = 0

        def __eq__(self, other):
            return self.position == other.position


      
    # start function of the stopwatch 
        
        
      
    # Stop function of the stopwatch 

    
    storeMaze = [""]  # to store all the maze
    path=[] 

    maze1 = [
            "XXXXXXXXXXXXXXXXXXXXX",   # let us know how the algorithm search its destination without obstacles
            "XS                  X",
            "X             XXXX  X",
            "X           XXXXX   X",
            "X          XXXXX    X",
            "X         XXXXX     X",
            "X        XXXXX      X",
            "X       XXXXX       X",
            "X      XXXXX        X",
            "X     XXXXX         X",
            "X   XXXXXX          X",
            "X  XXXXXX           X",
            "X   XXX             X",
            "X  XXX              X",
            "X  XX               X",
            "X                   X",
            "X                   X",
            "X                   X",
            "X                   X",
            "X                  fX",
            "XXXXXXXXXXXXXXXXXXXXX"
            ]

    maze2 = [
            "XSXXXXXXXXXXX",
            "X           X",
            "XX XXXXXX XXX",
            "XX XX      XX",
            "XX XXXX X XXX",
            "X          XX",
            "X XX XXX XXXX",
            "X XX   X    X",
            "X XX XXX  XXX",
            "X  X XX X  XX",
            "X  X    XX XX",
            "XX    X XX XX",
            "XXXXXXXXXXfXX"
            ]

    maze3 = [
            "XSXXXXXXXXXXXXXXXXXXX",
            "X      X   XX  X    X",
            "XXX XX XX XXX XXX XXX",
            "XXX XX XX      XX   X",
            "X       XX XX XXXX  X",
            "X XXXXX XX XX       X",
            "X    XX XX XXXX XXX X",
            "X XX XX       XXXXX X",
            "X  X XXXXXXXX XX    X",
            "XX X   XX     XX XX X",
            "X  XXX XX XXX XX XX X",
            "XX     XX XXX  X    X",
            "X  XX  X  XX   XXX XX",
            "X X  X XX      X    X",
            "X X XX   XXXXXXXXXX X",
            "X   XX X XX  XX     X",
            "XXX XXXX XX       X X",
            "X     XX XXXXX XX X X",
            "X XXX XX   X X X  X X",
            "X       XX     XX   X",
            "XXXXXXXXXXXXXXXXXXXfX"
            ]

    maze4 = [
            "XSXXXXXXXXXXXXXXXXXXXXXXX",
            "X  XX     X     X      XX",
            "XX X XXXX XXX XXX XXXXXXX",
            "XX X      X    XX       X",
            "XX XXXX XXXXX XXX XXXXXXX",
            "X     X  X             XX",
            "XXXX XXX XX XXX XXX XX XX",
            "X XX     XX XXX X    X XX",
            "X XX XXX    XXXXX XX X XX",
            "X    XX XXX       XX    X",
            "XX X  X XXX X XX X X XXXX",
            "XXXXX X   X X XXXX X XX X",
            "X     X XXX XXXX        X",
            "X X XXX XXX      XXXXXX X",
            "X X         XXXXXXX XXX X",
            "X XXXXX XXX             X",
            "X    XX   XX XXXXXXXXXX X",
            "X XXXXXXXXXX          X X",
            "XXXXXX       XXX XX XXX X",
            "X    X XX XXXXXXXXXXX   X",
            "X XX X XX  X        X XXX",
            "X XX X XXX X XXXXXX     X",
            "X X    X   X  X     XXX X",
            "X X  X   X    XX XX  X  X",
            "XXXXXXXXXXXXXXXXXXXXfXXXX"
            ]

    maze5 = [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XS  XX XX XX X XX       X       X",
            "X X             XXXX XXXX XX XX X",
            "X X XXX XXXX XX            X    X",
            "X        X   XXX XXX XX X   X XXX",
            "XX XXXXXX XX           XX XXX X X",
            "XX      X XX XXXXXX XX    X     X",
            "XXX XXXXX XX      X XX XXXXXX X X",
            "X   XX       X XX X        XX X X",
            "X    XXX X X XX X XXXX X X    X X",
            "X XX XX  X X         X X X XXXX X",
            "X  X XX XX XX X XXXXXX X X      X",
            "XXXX  X X   X    X X   X X XX  XX",
            "X   X X   X XXXXXX X XXXX  X X  X",
            "X X XXX  XX    X     XX   X  XX X",
            "X   X   XXXXX XXXXX XXX X XX  X X",
            "XXX  XX XX     XX      XX XX XX X",
            "XXX XXX    XXXX XX XX X X    XX X",
            "X      XX XXXX     X  X XXXX X  X",
            "X X XX XX XX   X X XXXX XXXX XXXX",
            "X X XX      XXX XX         X  X X",
            "X X XXXX XX XXX XX XX XX X  X X X",
            "XXX      XX      X XX XX XX     X",
            "X   XX XX  XX XX     XX X   XXX X",
            "X XXXX XX XXX XX XXXX  XXXX X   X",
            "XXXX   X      X      X X  X  XX X",
            "X    X XXXXXX XXXXXX   X  X  XXXX",
            "X XXXX XX   X    XX  XXX  X     X",
            "X X        XX X X X    X XXXXXX X",
            "X XXXXXX  XX  X     XX X X      X",
            "X  X   X  X  XXXXXX XX X XXX  X X",
            "X    X X  X  XX     X      X  X X",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXfXXXX"
            
            ]






    #store maze1 to maze5 into storeMaze
    storeMaze.append(maze1) 
    storeMaze.append(maze2)
    storeMaze.append(maze3)
    storeMaze.append(maze4)
    storeMaze.append(maze5)

    def generateMaze(maze):
        global xStart,yStart,xEnd,yEnd
        mazeLength = len(maze)

        # Generate topleft indexes for X and Y
        topleftX = -(((mazeLength-1)*24)/2) 
        topleftY = ((mazeLength-1)*24)/2
        
        for y in range (mazeLength):
            
            for x in range (len(maze[y])):
                
                character = maze[y][x]
                xCoordinate = topleftX + (x*24) # distance between two grid is always 24 in turtle
                yCoordinate = topleftY - (y*24)
                
                if character == "X":  # if 'X' is encountered, generate wall
                    wall.goto(xCoordinate,yCoordinate)  # go to that location
                    wall.stamp()  # stick it at that location
            
                if character == " " or character == "f": # if encounter empty path or destination point 
                    path.append((xCoordinate, yCoordinate))

                if character == "f": # if encounter destination point
                    red.goto(xCoordinate, yCoordinate)       # send green sprite to screen location
                    red.stamp()
                    end = (xCoordinate,yCoordinate)
                    xEnd = xCoordinate
                    yEnd = yCoordinate
       

                if character == "S":  # if encounter stating point
                    red.goto(xCoordinate, yCoordinate)
                    red.stamp()
                    start= (xCoordinate, yCoordinate)
                    xStart = xCoordinate
                    yStart = yCoordinate

        search(xStart,yStart) # calling A* algorithm function
        backRoute(xEnd, yEnd)
        window.exitonclick()




    def endProgram():
        window.exitonclick()
        sys.exit()

    def search(x,y):
        global startTime
        startTime = time.time()
        frontier.append((x, y))
        solution[x,y] = x,y

        while len(frontier) > 0:          # exit while loop when frontier queue equals zero
            time.sleep(0)
            x, y = frontier.popleft()     # pop next entry in the frontier queue an assign to x and y location

            if(x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
                cell = (x - 24, y)
                solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
                #blue.goto(cell)        # identify frontier cells
                #blue.stamp()
                frontier.append(cell)   # add cell to frontier list
                visited.add((x-24, y))  # add cell to visited list

            if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
                cell = (x, y - 24)
                solution[cell] = x, y
                #blue.goto(cell)
                #blue.stamp()
                frontier.append(cell)
                visited.add((x, y - 24))
                #print(solution)

            if(x + 24, y) in path and (x + 24, y) not in visited:   # check the cell on the  right
                cell = (x + 24, y)
                solution[cell] = x, y
                #blue.goto(cell)
                #blue.stamp()
                frontier.append(cell)
                visited.add((x +24, y))

            if(x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
                cell = (x, y + 24)
                solution[cell] = x, y
                #blue.goto(cell)
                #blue.stamp()
                frontier.append(cell)
                visited.add((x, y + 24))
            green.goto(x,y)
            green.stamp()


    def backRoute(x,y):
        global startTime
        pathCost = 0
        yellow.goto(x,y)
        yellow.stamp()
        
        while (x,y) != (xStart,yStart):    # stop loop when current cells == start cell
            yellow.goto(solution[x,y])        # move the yellow sprite to the key value of solution ()
            yellow.stamp()
            x,y = solution[x,y]               # "key value" now becomes the new key
            pathCost +=1
        import again
        again.main(startTime,pathCost)
        

    wall = Wall() # calling pen constructor
    green = Green()
    yellow = Yellow()
    red = Red()
    path = []
    visited = set()
    frontier = deque()
    solution = {} 

    generateMaze(storeMaze[chosenLevel])  # calling generateMaze and you can change your maze level here
    
    root.mainloop()
