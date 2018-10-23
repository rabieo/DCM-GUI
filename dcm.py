from tkinter import *
import tkinter.messagebox

root = Tk()

warning1 = StringVar()
warning2 = StringVar()

def newuser():
    with open('usernames.txt', 'a') as f:
        password = entry2.get()
        username = entry1.get()
        if len(entry1.get()) > 4 and len(entry2.get()) > 4:
            f.write(entry1.get())
            f.write('\n')
            f.write(entry2.get())
            f.write('\n')
            f.close()
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')
            warning1.set(username + " is registered")
            warning2.set("")
        else:
            warning1.set("username and password must")
            warning2.set("be more than 4 charecters")
            
        


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

label_3 = Label(textvariable=warning1, background="pink", fg="black")
label_3.grid(row = 5,column=0, sticky=W+E+N+S, padx=5, columnspan=2)
label_4 = Label(textvariable=warning2, background="pink", fg="black")
label_4.grid(row = 6,column=0, sticky=W+E+N+S, padx=5, columnspan=2)



root.mainloop()


    






