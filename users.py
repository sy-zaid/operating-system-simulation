class User:
    def __init__(self,userid=1,username='admin',userpassword= 'admin',userrights=7):
        self.userid = userid
        self.username = username
        self.userpassword = userpassword
        self.userrights = userrights
        self.usersdict = {'admin':{'userid':userid,'username':username,'userpassword':userpassword,'userrights':userrights}} # for all rights: 777 rwe-rwe-rwe 
        self.defaultid = 1

    def createUser(self):
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

    def getUsers(self):
        return self.usersdict
    
    def deleteUser(self,username,confirmation_password):
        user_dict = self.usersdict.get(username)
        if user_dict:
            if user_dict['userpassword'] == confirmation_password:
                del self.usersdict[username]
                print(f"{username} deleted successfully")
            else:
                print(f"Wrong password entered for {username}")
        else:
            print(f"{username} not found!")
        
    def updateRights(self,username,adminusername,adminpassword):
                

user = User()
user.createUser()
print(user.getUsers())
user.deleteUser('S','a')
print(user.getUsers())


    

