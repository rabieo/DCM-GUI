from tkinter import *
import tkinter.messagebox

root = Tk()

def newuser():
    with open('usernames.txt', 'a') as f:
        f.write(entry1.get())
        f.write('\n')
        f.close()
        entry1.delete(0, 'end') # removes the text from entry after u press register


root.config(background="pink")
root.title("beatsronix")



welcome = Label(text = "BeatTronix", background="pink", fg="black" , font=('none', 25))
welcome.grid(row = 0,column=0, sticky=W+E+N+S, columnspan=2, padx=15, pady=5)



label_1 = Label(text ="Username", background="pink", fg="black")
label_1.grid(row = 1,column=0, sticky=W+E+N+S, padx=15, pady=5)
label_2 = Label(text ="Password", background="pink", fg="black")
label_2.grid(row = 2,column=0, sticky=W+E+N+S, padx=15, pady=5)

entry1 = Entry(root)
entry1.grid(row = 1,column=1, sticky=W+E+N+S, padx=15, pady=5)
entry2 = Entry(root, show= '*')
entry2.grid(row = 2,column=1, sticky=W+E+N+S, padx=15, pady=5)

login = Button(text = "Login", bg="pink")
login.grid(row = 3,column=0, sticky=W+E+N+S, columnspan=2, padx=15, pady=5)
register = Button(text = "Register a new user", command = newuser, bg="pink")
register.grid(row = 4,column=0, sticky=W+E+N+S, columnspan=2, padx=15, pady=15)



root.mainloop()


    






