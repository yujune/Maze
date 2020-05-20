from Tkinter import *
import time
import sys

def endProgram():
    sys.exit()
        
def main(startTime,pathCost):
    root =Tk()
    root.geometry('550x350')
    root.title("Result")
    root.configure(background = "black")
    label = Label(root, text="GAME OVER", fg="Orange", font="Verdana 30 bold",bg="black")
    #label.pack()
    label.grid(column=60,row=0, padx=60, pady=0)
    label = Label(root, text="Time cost: %.2f seconds"%(time.time() - startTime) + ("\nPath Cost:  " + str(pathCost) + " nodes") , fg="yellow", font="Verdana 20 bold",bg="black")
    #label.pack()
    label.grid(column=60,row=1, padx=60, pady=10)
    #label['text'] = "Time cost: %.2f seconds"%(time.time() - startTime) + "\nPath Cost:  " + str(pathCost) + " nodes" 
    l = Label (root, text="Do you want to continue?",font="Verdana 15 bold",bg="black",fg="white")
    #l.pack()
    l.grid(column=60,row=10, padx=60, pady=20)


    def buttonClick1 ():
        root.destroy()
        import home
        home.main()
        
    def buttonClick2 ():
        root.destroy()
        endProgram()

    button1 = Button(root,text="Yes",command=buttonClick1,bg="light green",height=2,width=15)
    button1.grid(column=60,row=11, padx=60, pady=0)
    #button1.pack()

    button2 = Button(root,text="No",command=buttonClick2,bg="red",height=2,width=15)
    #button2.pack()
    button2.grid(column=60,row=12, padx=60, pady=5)

    root.mainloop()

#main(0,0)
