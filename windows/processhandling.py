import subprocess
import time,easygui
import os

class TaskManager:
    def __init__(self):
        self._output_file = './windows/runningtasks.txt'
        self.killpid = None

    def runTasklist(self):
        # Running tasklist command and capture the output
        result = subprocess.run(['tasklist'], capture_output=True, text=True)

        with open(self._output_file, 'w') as file:
            file.write(result.stdout)

    def displayProcesses(self):
        # Read the content of the file and display it
        with open(self._output_file, 'r') as file:
            content = file.read()
            easygui.msgbox(content)

    def killProcess(self):
        try:
            self.killpid = easygui.enterbox("Enter PID to kill a process:", title="PID")
            if self.killpid:
                commandtokill = f"taskkill /F /PID {self.killpid}"
                subprocess.run(commandtokill)
                print(f"Process with PID {self.killpid} killed successfully :)\n")
                self.displayProcesses()

            else:
                return
            
        except:
            print(f"\nFailed to kill the process with PID: {self.killpid}")
            return 
    

       
tm = TaskManager()
tm.runTasklist()
tm.displayProcesses()
tm.killProcess()
    
