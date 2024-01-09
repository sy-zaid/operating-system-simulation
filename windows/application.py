import subprocess
from processhandling import TaskManager
class ApplicationOpener:
    """
    A Class for opening the applications and task manager.
    Choose an Application
    1. Google Chrome
    2. Microsoft Edge
    3. Task Manager
    Enter number 1/2/3:

    input-parameters:
            - choice: To choose between the applications 1/2/3

    subprocess: It creates a process and runs it.
    """
    def open_application(self):
        print("Choose an Application to Open:\n1. Google Chrome\n2. Microsoft Edge\n3. Task Manager")
        choice = input("Choose an option (1-3) OR type 'cancel' to cancel the operation # ")  # User will input the respective number
        if choice == "1": # Will compare the input
            subprocess.run([r'C:\Program Files\Google\Chrome\Application\chrome.exe']) # Will run the application
        elif choice == "2":
            subprocess.run([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'])
        elif choice == "3":
            TM = TaskManager()
            subprocess.run(TM.displayProcesses())
        elif choice == 'cancel':
            return
            

# ob = ApplicationOpener()
# ob.open_application()