from tkinter import *
import tkinter.messagebox
from user import user    #importing user
from users import users  #importing users
from tkinter import ttk
import os.path # library to check if a file exists in the computer
import json # library that writes and loads dictionarys to text files


    ###################################################
    #
    # Class loginwindow creates a tkinter object and desplayes 
    # the login screen. it has 2 buttons -login and regiister-
    # if login is sucessful it calls the class userwindow and 
    # destroys its self.
    # 
    #    
    ###################################################
class loginwindow(Tk):

   def __init__(self):
      super().__init__()

      self._users = users()
      
      self.title("BeatTronix")
      self.config(background="pink")
      self.resizable(False, False)

      self.welcome_label = Label(text = "BeatTronix", background="pink", fg="black" , font=('none', 25))
      self.welcome_label.grid(row = 0,column=0, sticky=W+E+N+S, columnspan=2, padx=15, pady=5)

      self.username_label = Label(text ="Username", background="pink", fg="black")
      self.username_label.grid(row = 1,column=0, sticky=W+E+N+S, padx=15, pady=5)
      self.password_label = Label(text ="Password", background="pink", fg="black")
      self.password_label.grid(row = 2,column=0, sticky=W+E+N+S, padx=15, pady=5)

      self.username_entry = Entry(self)
      self.username_entry.grid(row = 1,column=1, sticky=W+E+N+S, padx=15, pady=5)
      self.password_entry = Entry(self, show= '*')
      self.password_entry.grid(row = 2,column=1, sticky=W+E+N+S, padx=15, pady=5)

      self.login_button = Button(text = "Login", command = self.login , bg="pink")
      self.login_button.grid(row = 3,column=0, sticky=W+E+N+S, columnspan=2, padx=15, pady=5)
      self.register_button = Button(text = "Register a new user", command = self.newuser, bg="pink")
      self.register_button.grid(row = 4,column=0, sticky=W+E+N+S, columnspan=2, padx=15, pady=15)

      self.message1 = StringVar()
      self.message2 = StringVar()

      self.message1_label = Label(textvariable=self.message1, background="pink", fg="black")
      self.message1_label.grid(row = 5,column=0, sticky=W+E+N+S, padx=5, columnspan=2)
      self.message2_label = Label(textvariable=self.message2, background="pink", fg="black")
      self.message2_label.grid(row = 6,column=0, sticky=W+E+N+S, padx=5, columnspan=2)

      self.usernamee = self.username_entry.get()
   def usernamee(self):
      return self.usernamee

   def newuser(self):
      password = self.password_entry.get()
      username = self.username_entry.get() 
      if self._users.check_registeruser(username,password):
         self._users.create_user(username,password)
         self.username_entry.delete(0, 'end')
         self.password_entry.delete(0, 'end')
         self.message1.set(username + " is registered")
         self.message2.set("")
      else:
         self.message1.set("username and password must")
         self.message2.set("be more than 4 charecters")

   def login(self):
      password = self.password_entry.get()
      username = self.username_entry.get()
      if self._users.check_loginuser(username, password):
         self.message1.set("")
         self.username_entry.delete(0, 'end')
         self.password_entry.delete(0, 'end')
         self.destroy()
         userwindow(username)
      else:
         self.message1.set("Incorect username or password")


    ###################################################
    #
    # Class userwindow desplays an iterface for selecting the  
    # mode and parameters. it has a save button to save the 
    # selected parameters.
    #
    # Atributes:
    #    username: the username of the user
    #    
    ###################################################
class userwindow(Tk):

   def __init__(self, username):
      super().__init__()

      self._user = user(username)
      
      self.title("BeeeatTronix")
      self.config(background="pink")
      self.geometry("400x320")
      
      self.resizable(False, False)

      self.select_label = Label(text = username, background="pink", fg="black" , font=('none', 25))
      self.select_label.grid(row = 0,column=0, sticky=W+E+N+S, columnspan=4, padx=15, pady=5)

      self.mode_label = Label(text ="Mode", background="pink", fg="black")
      self.mode_label.grid(row = 1,column=0, sticky=W+E+N+S, padx=15, pady=5)
      
      self.mode = StringVar()
      self.cb = ttk.Combobox(self, values=(self._user.get_allmodes()), textvariable = self.mode )
      self.cb.grid(row = 1,column=1, sticky=W+E+N+S, padx=15, pady=5)

      self.select_button = Button(text = "select", command = self.on_select , bg="pink")
      self.select_button.grid(row = 1,column=2, sticky=W+E+N+S, padx=15, pady=5)
      self.comboboxvalues=[]

   def on_select(self):
      x = 0
      labels=[]
      comboboxs=[]
      self.comboboxvalues=[]
      self.head_label = Label(text ="Parameters:", background="pink", fg="black")
      self.head_label.grid(row = 2,column=0, sticky=W+E+N+S, columnspan=2, padx=15, pady=5)
      for i in self._user.get_allparameters(self.mode.get()):
         labels.append(Label(text = i, background="pink", fg="black"))
         labels[x].grid(row = (x+3),column=0, sticky=E+W+S,columnspan=2, padx=5, pady=5)

         self.comboboxvalues.append(StringVar())
         comboboxs.append(ttk.Combobox(self, values=(self._user.get_allvalues(i)), textvariable = self.comboboxvalues[x],width=5 ))
         comboboxs[x].grid(row = (x+3),column=2, sticky=W+S, padx=5, pady=5)
         comboboxs[x].current(0)

         self.update_values()
         
         x += 1
         
      self.save_button = Button(text = "save", command = self.save , bg="pink")
      self.save_button.grid(row = 100,column=3, sticky=W+E+N+S, padx=15, pady=15)

   def save(self):
      x=0
      for i in self._user.get_allparameters(self.mode.get()):
         self._user.set_value(self.mode.get(),i,self.comboboxvalues[x].get())
         x+=1
      self.update_values()

   def update_values(self):
      x=0
      values=[]
      for i in self._user.get_allparameters(self.mode.get()):
         values.append(Label(text = self._user.get_value(self.mode.get(),i), background="pink", fg="black"))
         values[x].grid(row = (x+3),column=3, sticky=W+E+S, padx=5, pady=5)
         x += 1
      

#
# runs the program
#
login = loginwindow()
        
login.mainloop()

      
        

        




