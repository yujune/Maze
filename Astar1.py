def main(maze,start,end,endValue):

        import time
        import turtle
        import Tkinter as Tkinter
        
        class Node():
                def __init__(self, parent=None, position=None):
                    self.parent = parent
                    self.position = position

                    self.g = 0
                    self.h = 0
                    self.f = 0

                def __eq__(self, other):
                    return self.position == other.position

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

        def AstarSearch():
            

                """Returns a list of tuples as a path from the given start to the given end in the given maze"""
                global startTime
                startTime = time.time()
                start_node = Node(None, start)
                start_node.g = start_node.h = start_node.f = 0
                end_node = Node(None, end)
                end_node.g = end_node.h = end_node.f = 0

                open_list = []
                closed_list = []

                open_list.append(start_node)
                
                while len(open_list) > 0:
                    time.sleep(0)
                    current_node = open_list[0]  # take the first node in open list
                    current_index = 0
                    
                    for index, item in enumerate(open_list):  # compare all the nodes in the open list
                        if item.f < current_node.f:         # choose the least f value of nodes in open list
                            current_node = item 
                            current_index = index
                            
                    open_list.pop(current_index)
                    closed_list.append(current_node)  # add the least f node to the closed list

                    if current_node == end_node: 
                        path = []
                        current = current_node
                        
                        pathCost =0

                        while current is not None:
                            
                            path.append(current.position)
                            yellow.goto(current.position[0],current.position[1])
                            yellow.stamp()
                            current = current.parent
                            pathCost +=1
                            
                        #label['text'] = "Time cost: %.2f seconds"%(time.time() - startTime) + "\nPath Cost:  " + str(pathCost) + " nodes"
                        import again
                        again.main(startTime,pathCost)
                        return path
                

                    # Generate children
                    children = []
                    for new_position in [(0,24), (0,-24), (24,0), (-24,0)]: # Adjacent squares (up, down, right, left)

                        # Get node position
                        node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])                                                                                                                                                                                                                                                                                               
                        
                        mazeLength = (((len(maze)-1)*24)/2)

                        # Make sure did not out of range
                        if node_position[0] > mazeLength or node_position[0] < -mazeLength or node_position[1] > mazeLength or node_position[1] < -mazeLength:
                            continue
                                                 
                        
                        #Make sure in path
                        mazeSizeX = abs(int((node_position[1]-mazeLength)/24))
                        mazeSizeY = abs(int((node_position[0]+mazeLength)/24))
                        if maze[mazeSizeX][mazeSizeY] != " " and maze[mazeSizeX][mazeSizeY] != "f": # if maze[x,y] (x and y start from 0 until maze.length) 
                            continue
                                                                                                                                                                                                                                                                    
                        green.goto(node_position[0],node_position[1]) # walkable path will be printed in green color
                        green.stamp()

                        # Create new node
                        new_node = Node(current_node, node_position)

                        # Append
                        children.append(new_node)

                   # Loop through children
                    for child in children:
                    
                        if child not in closed_list:

                            child.g = current_node.g + 5
                            xValue = abs((child.position[0]+mazeLength)/24)
                            yValue = abs((child.position[1]-mazeLength)/24)
                            #child.h = float(math.sqrt(((xValue - endValue[0])**2 ) + ((yValue - endValue[1])**2 )))
                            child.h = (xValue - endValue[0])**2 + (yValue - endValue[1])**2
                            #child.h = math.sqrt(((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2))

                            child.f = child.g + child.h
                            
                            if child not in open_list:
                                open_list.append(child)
        green = Green()
        yellow = Yellow()
        AstarSearch()
