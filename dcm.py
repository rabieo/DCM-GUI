from tkinter import *
import tkinter.messagebox

root = Tk()

v = StringVar()

def newuser():
    string1 = v.get
    print(string1)


root.config(background="light blue")
root.geometry("500x600")
root.title("beatsronix")



welcome = Label(text = "Welcome to BeatTronix", font=('none', 25)).place(x = 100, y = 60)

#photo = PhotoImage(file="pmm.png")
#pic = Label(root, image = photo)
#pic.place( x = 100, y = 110)



label_1 = Label(text ="Username").place(x=207, y=277)
label_2 = Label(text ="Password").place(x = 210, y=300)

entry1 = Entry(root,textvariable=v).place(x=270, y =277)
entry2 = Entry(root, show= '*').place(x=270, y =300)

v.set("a default value")

login = Button(text = "Login").place(x = 270, y = 340)
register = Button(text = "Register a new user", commmand = newuser()).place( x = 240 , y = 430)



root.mainloop()


    






