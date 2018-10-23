from tkinter import *
import tkinter.messagebox
#from tkinter.ttk import * # makes bottons look better

root = Tk()



def newuser():
    with open('usernames.txt', 'a') as f:
        f.write(entry1.get())
        f.write('\n')
        f.close()
        entry1.delete(0, 'end') # removes the text from entry after u press register


root.config(background="light blue")
root.geometry("500x500")
root.title("beatsronix")



welcome = Label(text = "Welcome to BeatTronix", background="light blue", font=('none', 25)).place(x = 100, y = 60)



label_1 = Label(text ="Username", background="light blue").place(x=207, y=277)
label_2 = Label(text ="Password", background="light blue").place(x = 210, y=300)

entry1 = Entry(root)
entry1.place(x=270, y =277)
entry2 = Entry(root, show= '*')
entry2.place(x=270, y =300)



login = Button(text = "Login", bg="light blue").place(x = 270, y = 340)
register = Button(text = "Register a new user", command = newuser, bg="light blue").place( x = 240 , y = 430)



root.mainloop()


    






