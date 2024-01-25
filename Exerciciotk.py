from tkinter import *
root= Tk()
root.wm_title('Primeiro App')

e = Entry(root,width=80)
e.pack()
e.insert(0,"Entre com o nome")


def myclick():
    hello= "hello" + e.get()
    mylabel= Label(root,text=hello)
    mylabel.pack()

myButton = Button(root,text="Enter your name",command=myclick)
myButton.pack()

root.mainloop()

