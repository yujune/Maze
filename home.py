from Tkinter import *
import turtle

def main():
    
    root =Tk()
    root.geometry('600x400')
    root.configure(background = "Black")
    l = Label (root, text="Welcome to Maze World",font="Verdana 30 bold",bg="Black",fg="orange")
    #l.pack(side=TOP)
    l.grid(column=25,row=0, padx=20, pady=0)


    def buttonClick1 ():
        root.destroy()
        algorithm = 1
        import chooseLevel
        chooseLevel.main(algorithm)

    def buttonClick2 ():
        root.destroy()
        algorithm = 2
        import chooseLevel
        chooseLevel.main(algorithm)

    def buttonClick3 ():
        root.destroy()
        algorithm = 3
        import chooseLevel
        chooseLevel.main(algorithm)

    
    button1 = Button(root,text="A Star Algorithm",command=buttonClick1,bg="yellow",height=3,width=35)
    #button1.pack(fill = BOTH, expand = True)
    button1.grid(column=25,row=9, padx=0, pady=20)

    button2 = Button(root,text="Best First Search",command=buttonClick2,bg="red",height=3,width=35)
    #button2.pack(fill = BOTH, expand = True)
    button2.grid(column=25,row=10, padx=0, pady=20)

    button3 = Button(root,text="Breadth First Search",command=buttonClick3,bg="blue",height=3,width=35)
    #button3.pack(fill = BOTH, expand = True)
    button3.grid(column=25,row=11, padx=0, pady=20)


    root.mainloop()
    
main()
