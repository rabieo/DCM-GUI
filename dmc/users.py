import os.path
import json


class users:
    def __init__(self):
        self._username_list = []
        self._password_list = []

        ## loads the usernames of all the users
        ## from usernames.txt to _username_list
        if os.path.isfile('usernames.txt'):
            with open('usernames.txt', 'r') as file1:
                a = file1.read()
                self._username_list = json.loads(a)
        else:
            with open('usernames.txt', 'w') as file2:
                file2.write(json.dumps(self._username_list))

        ## loads the passwords of all the users
        ## from passwords.txt to _password_list
        if os.path.isfile('passwords.txt'):
            with open('passwords.txt', 'r') as file3:
                a = file3.read()
                self._password_list = json.loads(a)
        else:
            with open('passwords.txt', 'w') as file4:
                file4.write(json.dumps(self._password_list))
                
                

    def create_user(self, username, password):
        self._username_list.append(username)
        self._password_list.append(password)
        self.update_users()

    def check_registeruser(self, username, password):
        if len(username) > 4 and len(password) > 4:
            if username in self._username_list:
                index = self._username_list.index(username)
                if password == self._password_list[index]:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return False

    def check_loginuser(self, username, password):
        if username in self._username_list:
            index = self._username_list.index(username)
            if password == self._password_list[index]:
                return True
            else:
                return False
        else:
            return False

    def update_users(self):
        with open('usernames.txt', 'w') as file1:
                file1.write(json.dumps(self._username_list))
        with open('passwords.txt', 'w') as file2:
                file2.write(json.dumps(self._password_list))


    def get_allusers(self):
        return self._username_list

    def num_of_users(self):
        return len(self._username_list)

    def delete_user(self, username):
        return


