import subprocess

class ApplicationOpener:
    
    """
    Choose an Application
    1. Google Chrome
    2. Microsoft Edge
    3. Task Manager
    Enter number 1/2/3:
    input-parameters:
            - choice: To choose between the applications 1/2/3
            - subprocess: It creates a process and runs it        
    """
    def open_application(self):
        print("Choose an Application\n1. Google Chrome\n2. Microsoft Edge\n3. Task Manager")
        choice = input("Enter number 1/2/3: ")
        if choice == "1":
            subprocess.run([r'C:\Program Files\Google\Chrome\Application\chrome.exe'])
        elif choice == "2":
            subprocess.run([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'])
        elif choice == "3":
            subprocess.run([r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\System Tools'])
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# ob = ApplicationOpener()
# ob.open_application()