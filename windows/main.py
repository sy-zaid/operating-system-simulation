import os,time
from users import User
from filehandling import File
from folderhandling import Folder
import threading

# For semaphores
buf = []
empty = threading.Semaphore(1)
full = threading.Semaphore(0)
mutex = threading.Lock()

class OperatingSystemSimulation():
    def __init__(self,currentuser = None):
        self.currentuser = currentuser
    

    def lsScreen(self):
        """
        A function to display the Login/SignUp Screen to the user.
        
        1. Login to existing user
        2. Signup as a new user

        input-parameters:
        - lsinput: To choose between login/signup
            -- shut: to shutdown

        """
        print("\n------------------------------------------------------------------\n")
        print("\n------------------------- WELCOME TO ZAT-OS -------------------------\n")
        print("\n------------------------------------------------------------------\n")
        print(f"1. Login to existing user\n2. Signup as a new user")
        lsinput = input("Enter your choice (1-2) OR 'shut' to shutdown the system # ")

        if lsinput == 'shut': # If user wants to shutdown the system.
            print(f"\nShutting down...")
            time.sleep(3) #Timer to shutdown
            return
        elif lsinput == '1': # If user wants to login
            self.login()
        elif lsinput == '2': # If user wants to signup
            self.signup()
        
        else:
            print(f"\nInvalid Input Choice, Please Retry...")
            self.lsScreen()
    def login(self):
        print("\nEnter login credentials...")
        inp_username = input("Enter username OR 'admin' for admin-user OR 'cancel' to cancel operation # ")
        inp_password = input("Enter password # ")
        user = User()
        if inp_username in user.getUsers() and inp_username != 'cancel': # Checks if username exists in json file | and if user doesn't cancels the operation.
            userdata = user.getUsers().get(inp_username) # "szaid": {"userid": 2, "username": "szaid", "userpassword": "abc", "userrights": 5}
            if userdata['userpassword'] == inp_password: # Compares userpassword with the input password.
                print(f"\n----- Welcome {inp_username} :) -----\n")
                self.currentuser = inp_username
                self.mainMenu()
            else:
                print(f"\nIncorrect password entered.")
                self.login()

        elif inp_username == 'cancel':
            self.lsScreen()
        else:
            print(f"\n{inp_username} not found :()")
        
    def signup(self):
        print("\nEnter signup credentials...")
        user = User()
        user.createNewUser()
        self.login()



        

    def mainMenu(self):
        print(f"1. User Management\n2. Service Management\n3. Process Management\n4. Backup")
        first_input = input("Enter your choice(1-4 or 'home' to return home | 'logout') # ")
        if first_input == '1':
            self.userManagement()
        
        elif first_input == '2':
            self.serviceManagement()
        
        elif first_input == '3':
            self.processManagement()
        
        elif first_input == '4':
            self.backup()
        
        elif str(first_input) and str(first_input) == 'home':
            self.mainMenu()

        elif str(first_input) and str(first_input) == 'logout':
            print(f"\nLogged Out...")
            self.lsScreen()

    
    def userManagement(self):
        print('You entered in User Management')
    
    def serviceManagement(self):
        """
        1. Files Services
        2. Folder Services
        3. Home
        """
        print(f"1. Files Services\n2. Folder Services\n3. Home")
        inp_opt = input("Choose an option (1-3) # ")
        if inp_opt == '1':
            self.servicesFileHandling()
        elif inp_opt == '2':
            self.servicesFolderHandling()
        elif inp_opt == 'home' or inp_opt == '3':
            self.mainMenu() 
    
    def servicesFileHandling(self):
        """
        1. List Files
        2. Delete a file
        3. Create a File
        4. Search a file
        5. Backup All Files
        """
        file = File(currentuser=self.currentuser)
        print(f"\nBelow are the services for file handling, please choose an option:\n1. List Files\n2. Delete a file\n3. Create a File\n4. Search a file\n5. Backup All Files ")
        inp_file = input("Choose an option (1-5) or 'home' to return Home # ")
        if inp_file == '1':
            file.listFiles()
        elif inp_file == '2':
            mutex.acquire() 
            file.deleteFile() # File deleted
            mutex.release() 
        elif inp_file == '3':
            mutex.acquire() 
            file.createFile()
            mutex.release()    
            time.sleep(1)
        elif inp_file == '4':
            file.searchFile()
        elif inp_file == '5':
            file.backupAllFiles()   
        
        self.serviceManagement()

        
    def servicesFolderHandling(self):
        """
        1. List Folders
        2. Delete a folder
        3. Create a Folder
        4. Search a folder
        5. Backup All Folder
        """
        folder = Folder(currentuser=self.currentuser)
        print(f"\nBelow are the services for folder handling, please choose an option:\n1. List Folder\n2. Delete a folder\n3. Create a Folder\n4. Search a folder\n5. Backup All Folders ")
        inp_folder = input("Choose an option (1-5) or 'home' to return Home # ")
        if inp_folder == 'home':
            self.mainMenu()
        elif inp_folder == '1':
            folder.listFolders()
        elif inp_folder == '2':
            folder.deleteFolder()
        elif inp_folder == '3':
            folder.createFolder()
        elif inp_folder == '4':
            folder.searchFolder()
        elif inp_folder == '5':
            folder.backupAllFolders()
        
        self.serviceManagement()

    def processManagement(self):
        print("Opening Task Manager...")
    
    def backup(self):
        print("Creating backup for files...")

if __name__ == "__main__":
    OS = OperatingSystemSimulation()
    OS.lsScreen()
