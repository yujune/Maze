def main(a,b,c,d):
    global xStart,yStart,xEnd,yEnd
    xStart=a
    yStart=b
    xEnd=c
    yEnd=d
    import turtle
    import sys
    import time
    from collections import deque
    import tkinter as Tkinter 
      
    counter = 0
    counter2 = 0
    running = False
    
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


    def backRoute(x,y,xStart,yStart):
        global startTime
        pathCost = 0
        yellow.goto(x,y)
        yellow.stamp()
        
        while (x,y) != (xStart,yStart):    # stop loop when current cells == start cell
            yellow.goto(solution[x,y])        # move the yellow sprite to the key value of solution ()
            yellow.stamp()
            x,y = solution[x,y]               # "key value" now becomes the new key
            pathCost +=1
        label['text']= "Time cost: %.2f seconds"%(time.time() - startTime) + "\nPath Cost:  " + str(pathCost) + " nodes"


    green = Green()
    yellow = Yellow()
    red = Red()
    path = []
    visited = set()
    frontier = deque()
    solution = {}
    
    search(xStart,yStart) # calling A* algorithm function
    backRoute(xEnd,yEnd,xStart,yStart)

     
