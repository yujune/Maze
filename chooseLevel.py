from Tkinter import *
import GenerateMaze
import breadth

def main(algorithm):
    
    root =Tk()
    root.geometry('500x550')
    root.configure(background = "Black")
    l = Label (root, text="Level",font="Verdana 30 bold",bg="Black",fg="light grey")
    l.grid(column=25,row=0, padx=110, pady=0)


    def buttonClick1 ():
        root.destroy()
        chosenLevel =1
        if(algorithm==3):
            breadth.main(chosenLevel)
        else:
            GenerateMaze.main(chosenLevel,algorithm)
    
    def buttonClick2 ():
        root.destroy()
        chosenLevel =2
        if(algorithm==3):
            breadth.main(chosenLevel)
        else:
            GenerateMaze.main(chosenLevel,algorithm)

    def buttonClick3 ():
        root.destroy()
        chosenLevel =3
        if(algorithm==3):
            breadth.main(chosenLevel)
        else:
            GenerateMaze.main(chosenLevel,algorithm)

    def buttonClick4 ():
        root.destroy()
        chosenLevel =4
        if(algorithm==3):
            breadth.main(chosenLevel)
        else:
            GenerateMaze.main(chosenLevel,algorithm)

    def buttonClick5 ():
        root.destroy()
        chosenLevel =5
        if(algorithm==3):
            breadth.main(chosenLevel)
        else:
            GenerateMaze.main(chosenLevel,algorithm)
        

    button1 = Button(root,text="Easy",command=buttonClick1,bg="yellow",height=3,width=35)
    button1.grid(column=25,row=9, padx=110, pady=20)

    button2 = Button(root,text="Medium",command=buttonClick2,bg="red",height=3,width=35)
    button2.grid(column=25,row=10, padx=110, pady=20)

    button3 = Button(root,text="Hard",command=buttonClick3,bg="blue",height=3,width=35)
    button3.grid(column=25,row=11, padx=110, pady=20)

    button4 = Button(root,text="Advanced",command=buttonClick4,bg="orange",height=3,width=35)
    button4.grid(column=25,row=12, padx=110, pady=20)

    button5 = Button(root,text="Expert",command=buttonClick5,bg="purple",height=3,width=35)
    button5.grid(column=25,row=13, padx=110, pady=20)


    root.mainloop()
#main(1)    
