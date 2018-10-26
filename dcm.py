from tkinter import *

import tkinter.messagebox
import os

root = Tk()

warning1 = StringVar()
warning2 = StringVar()

def checknewuser():
    if len(entry1.get()) > 4 and len(entry2.get()) > 4:
        with open('usernames.txt', 'a') as f1:
            f1.write(username)
            f1.write('\n')
        with open('passwords.txt', 'a') as f2:
            f2.write(password)
            f2.write('\n')
        entry1.delete(0, 'end')
        entry2.delete(0, 'end')
        warning1.set(username + " is registered")
        warning2.set("")

                    
    else:
        warning1.set("username and password must")
        warning2.set("be more than 4 charecters")


def newuser():
    password = entry2.get()
    username = entry1.get()

    if os.path.isfile('usernames.txt'):
        with open('usernames.txt') as f:
            size=sum(1 for _ in f)

            if size == 10:
                print("many users")

        

            else:
                checknewuser()


    else:
        checknewuser()




    

def login():
    password = entry2.get()
    username = entry1.get()
    with open('usernames.txt', 'r') as f1:
        users = f1.read().splitlines()
        
    with open('passwords.txt', 'r') as f2:
        passwords = f2.read().splitlines()
    if username in users:
        index1 = users.index(entry1.get())
        if passwords[index1] == entry2.get():
            warning1.set("logged in as " + entry1.get())
            root.destroy()
            root1 = Tk()

            root1.config(background="pink")
            root1.title(users[index1])

            welcome = Label(text = "Hello "+users[index1] , background="pink", fg="black" , font=('none', 25))
            welcome.grid(row = 0,column=0, sticky=W+E+N+S, columnspan=2, padx=15, pady=5)


            mode = Label(text = "Seclect Mode", background="pink").grid(row = 1, column = 0, stick = W)
            lowerrate = Label(text = "Seclect Lower Rate Limit", background="pink").grid(row = 2, column = 0, stick = W)
            upperrate = Label(text = "Seclect Upper Rate Limit", background="pink").grid(row = 3, column = 0, stick = W)
            ventricularamp = Label(text = "Seclect Ventricular Amplitude", background="pink").grid(row = 4, column = 0, stick = W)
            ventricularamp1 = Label(text = "(If OFF write 0)", background="pink").grid(row = 4, column = 3, stick = W)
            ventriculapulse = Label(text = "Select Ventricular Pulse Width", background="pink").grid(row = 5, column = 0, stick = W)

            modeentry = Entry(root1)
            modeentry.grid(row = 1, column = 2)

            lowerentry = Entry(root1)
            lowerentry.grid(row = 2, column = 2)

            upperentry = Entry(root1)
            upperentry.grid(row = 3, column = 2)

            ventricularamp = Entry(root1)
            ventricularamp.grid(row = 4, column = 2)

            ventricularpulse = Entry(root1)
            ventricularpulse.grid(row = 5, column = 2)

            def logout():
                root1.destroy()

            def help1():
                root2 = Toplevel()
                root2.config(background="pink")


                photo1 = PhotoImage(file="sc.png")
                label4 = Label(root2, image=photo1)
                label4.pack()

                welcome1 = Label(text = "How To Use" , background="pink", fg="black" , font=('none', 25))
                welcome1.grid(row = 0,column=0, sticky=W+E+N+S, columnspan=2, padx=15, pady=5)

                root2.mainloop()



            def parameters():
                low = lowerentry.get()
                int_a = int(low)
                

                high = upperentry.get()
                int_b = int(high)

                vent = ventricularamp.get()
                float_c = float(vent)

                pulse = ventricularpulse.get()
                float_d = float(pulse)

                k = True     

                if modeentry.get() == "voo" or modeentry.get() == "VOO" :
                    with open(users[index1]+'.txt', 'a') as f:
                        f.write(modeentry.get())
                        f.write('\n')
                        f.close()

                        

                else:
                            
                            
                    tkinter.messagebox.showinfo('Error', 'please enter a valid mode')
                    return
                            

                        
                        
                if  30 <= int_a <= 50 and int_a%5==0:
                    with open(users[index1]+'.txt', 'a') as f:
                        f.write(lowerentry.get())
                        f.write('\n')
                        f.close()
                            

                elif  50 < int_a <= 90:
                     with open(users[index1]+'.txt', 'a') as f:
                        f.write(lowerentry.get())
                        f.write('\n')
                        f.close()



                elif  90 < int_a <= 175 and int_a%5==0:
                    with open(users[index1]+'.txt', 'a') as f:
                        f.write(lowerentry.get())
                        f.write('\n')
                        f.close()

                else:
                    tkinter.messagebox.showinfo('Error', 'please enter a valid Lower Rate Limit')
                    os.remove(users[index1]+'.txt')
                    k = False
                    return
                            
                            
                            
                            
                            

                if  50 <= int_b <= 175 and int_b%5==0:
                    with open(users[index1]+'.txt', 'a') as f:
                        f.write(upperentry.get())
                        f.write('\n')
                        f.close()
                elif k:
                    os.remove(users[index1]+'.txt')
                    tkinter.messagebox.showinfo('Error', 'please enter a valid Upper Rate Limit')
                            
                    return

                else:
                            
                            
                    tkinter.messagebox.showinfo('Error', 'please enter a valid Upper Rate Limit')
                            

                if  float_c == 0:
                    with open(users[index1]+'.txt', 'a') as f:
                        f.write(ventricularamp.get())
                        f.write('\n')
                        f.close()                


                                
                elif  0.5 <= float_c <= 3.2:
                    with open(users[index1]+'.txt', 'a') as f:
                        f.write(ventricularamp.get())
                        f.write('\n')
                        f.close()


                elif  3.5 <= float_c <= 7.0 and float_c%0.5 ==0:
                    with open(users[index1]+'.txt', 'a') as f:
                        f.write(ventricularamp.get())
                        f.write('\n')
                        f.close()

                elif k:
                    os.remove(users[index1]+'.txt')
                    tkinter.messagebox.showinfo('Error', 'please enter a valid Ventricular Amplitude')
                            
                    return
                            

                else:
                            
                    tkinter.messagebox.showinfo('Error', 'please enter a valid Ventricular Amplitude')


                if  float_d == 0.05:
                    with open(users[index1]+'.txt', 'a') as f:
                        f.write(ventricularpulse.get())
                        f.write('\n')
                        f.close()                


                                
                elif  0.1 <= float_d <= 1.9:
                    with open(users[index1]+'.txt', 'a') as f:
                        f.write(ventricularpulse.get())
                        f.write('\n')
                        f.close()

                elif k:
                    os.remove(users[index1]+'.txt')
                    tkinter.messagebox.showinfo('Error', 'please enter a valid Ventricular Pulse Width')
                            
                    return


                else:
                            
                    tkinter.messagebox.showinfo('Error', 'please enter a valid Ventricular Pulse Width')


                        





                
                
                
               


            def checkinput():


                
                if os.path.isfile(users[index1]+'.txt'):
                    os.remove(users[index1]+'.txt')
                    parameters()
                    

                    

                else:
                    parameters()











            save = Button(text = "Save", command = checkinput)
            save.grid(row = 7, column = 2)

            logout = Button(text = "Logout", command = logout)
            logout.grid(row = 7, column = 3)

            help12 = Button(text = "How to Use ?", command = help1)
            help12.grid(row = 0, column = 3)
            












            root1.mainloop()

        else:
            warning1.set("Incorect username or password")
    else:
        warning1.set("Incorect username or password")
        
            
        


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

login = Button(text = "Login", command = login , bg="pink")
login.grid(row = 3,column=0, sticky=W+E+N+S, columnspan=2, padx=15, pady=5)
register = Button(text = "Register a new user", command = newuser, bg="pink")
register.grid(row = 4,column=0, sticky=W+E+N+S, columnspan=2, padx=15, pady=15)

label_3 = Label(textvariable=warning1, background="pink", fg="black")
label_3.grid(row = 5,column=0, sticky=W+E+N+S, padx=5, columnspan=2)
label_4 = Label(textvariable=warning2, background="pink", fg="black")
label_4.grid(row = 6,column=0, sticky=W+E+N+S, padx=5, columnspan=2)



root.mainloop()


    






