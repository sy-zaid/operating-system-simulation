class OperatingSystemSimulation():
    def __init__(self):
        pass

    def mainMenu(self):
        print(f"1. User Management\n2.Service Management\n3.Process Management\n4.Backup")
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
    OS.mainMenu()
