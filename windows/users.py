import json
class User:
    """
    A class for creating and managing users.

    METHODS:
    - createNewUser() ---> creates a new user in the system (default is already created)
    - 
    """

    def __init__(self,userid=1,username='admin',userpassword= 'admin',userrights=7):
        self.userid = userid
        self.username = username
        self.userpassword = userpassword
        self.userrights = userrights
        self.filename = "./windows/users_data.json"

        try:
            with open(self.filename, 'r') as file:
                self.usersdict = json.load(file)
                pass
        except FileNotFoundError:
            print(f"File 'users_data.json' not found. Creating a new one.")
        self.defaultid = 1
        self.loadUsersFromFile()
        self.saveUsersToFile()

    def saveUsersToFile(self):
        with open(self.filename, 'w') as file:
            json.dump(self.usersdict, file)

    def loadUsersFromFile(self):
        try:
            with open(self.filename, 'r') as file:
                self.usersdict = json.load(file)
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Creating a new one.")

    def createNewUser(self):
        user = {}
        auto_id = self.defaultid + 1
        default_rights = 5
        username = str(input("Enter New User Name"))
        userpassword = str(input("Enter New User password: "))
        confirm_password = str(input("Confirm User password: "))
    
        if userpassword == confirm_password:
            user['userid'] = auto_id
            user['username'] = username
            user['userpassword'] = userpassword
            user['userrights'] = default_rights
            self.usersdict[f"{username}"] = user
            self.saveUsersToFile()

    def getUsers(self):
        return self.usersdict
    
    def getSpecifiedUser(self):
        self.loadUsersFromFile()

        return self.usersdict.get()
    
    def deleteUser(self):
        username = input("Enter username to delete: ")
        confirmation_password = input("Enter password: ")

        user_dict = self.usersdict.get(username)
        if user_dict:
            if user_dict['userpassword'] == confirmation_password:
                del self.usersdict[username]
                print(f"User {username} deleted successfully")
            else:
                print(f"Wrong password entered for {username}")
        else:
            print(f"{username} not found!")
        self.saveUsersToFile()
        
    def updateUserType(self,username,adminusername,adminpassword,userrights):
        user_dict = self.usersdict[username]
        admin = self.usersdict['admin']
        if adminusername == admin['username'] and adminpassword == admin['userpassword']:
            user_dict['userrights'] = userrights
        self.saveUsersToFile()
        

        

# user = User()
# user.createNewUser()
# print(user.getUsers())
# user.deleteUser()
# # user.updateUserType('s','admin','admin',7)
# print(user.getUsers())


    

