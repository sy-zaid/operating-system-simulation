import os,time
from users import User

class OperatingSystemSimulation():
    def __init__(self):
        pass
    
    def login(self):
        print("\nEnter login credentials...")
        inp_username = input("Enter username OR 'admin' for admin-user OR 'cancel' to cancel operation # ")
        inp_password = input("Enter password # ")
        user = User()
        if inp_username in user.getUsers() and inp_username != 'cancel':
            print(f"\n----- Welcome {inp_username} :) -----\n")
            self.mainMenu()
        elif inp_username == 'cancel':
            self.lsScreen()
        else:
            print(f"\n{inp_username} not found :()")
        
    def signup(self):
        print("\nEnter signup credentials...")
        user = User()
        user.createNewUser()

    def lsScreen(self):
        print("\n------------------------- WELCOME TO ZAT -------------------------\n")
        print(f"1. Login to existing user\n2. Signup as a new user")
        lsinput = input("Enter your choice (1-2) OR 'shut' to shutdown the system # ")

        checkinp_dict = {'1':self.login(),'2':self.signup()}
        if lsinput == 'shut':
            print(f"\nShutting down...")
            time.sleep(3)
            return
        checkinp_dict[lsinput]
        
        

    def mainMenu(self):
        print(f"1. User Management\n2. Service Management\n3. Process Management\n4. Backup")
        first_input = input("Enter your choice(1-4 or 'home' to return home): ")
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

    
    def userManagement(self):
        print('You entered in User Management')
    
    def serviceManagement(self):
        print("Managing services...")
        
    def processManagement(self):
        print("Opening Task Manager...")
    
    def backup(self):
        print("Creating backup for files...")

if __name__ == "__main__":
    OS = OperatingSystemSimulation()
    OS.lsScreen()
