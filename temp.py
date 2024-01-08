import os
import subprocess

class SimpleOS:
    def __init__(self):
        self.current_directory = os.getcwd()
        self.processes = []

    def display_menu(self):
        print("\nSimple OS Menu:")
        print("1. Create Folder")
        print("2. Create File")
        print("3. Change File Rights")
        print("4. Search Files")
        print("5. Create Process")
        print("6. Display Processes")
        print("7. Kill Process")
        print("8. Open Application")
        print("9. Share Data Between Processes")
        print("10. Execute Custom Program")
        print("11. Exit")

    def create_folder(self):
        folder_name = input("Enter folder name: ")
        os.makedirs(os.path.join(self.current_directory, folder_name))
        print(f"Folder '{folder_name}' created.")

    def create_file(self):
        file_name = input("Enter file name: ")
        with open(os.path.join(self.current_directory, file_name), 'w'):
            pass
        print(f"File '{file_name}' created.")

    def change_file_rights(self):
        file_name = input("Enter file name: ")
        os.chmod(os.path.join(self.current_directory, file_name), int(input("Enter new rights (in octal): "), 8))
        print(f"File rights changed for '{file_name}'.")

    def search_files(self):
        file_name = input("Enter file name to search: ")
        results = [file for file in os.listdir(self.current_directory) if file_name in file]
        print("Search results:")
        for result in results:
            print(result)

    def create_process(self):
        command = input("Enter command for the new process: ")
        process = subprocess.Popen(command, shell=True)
        self.processes.append(process)
        print(f"Process started with PID: {process.pid}")

    def display_processes(self):
        print("Active Processes:")
        for process in self.processes:
            print(f"PID: {process.pid}, Command: {process.args}")

    def kill_process(self):
        pid_to_kill = int(input("Enter PID to kill: "))
        try:
            process_to_kill = next(process for process in self.processes if process.pid == pid_to_kill)
            process_to_kill.terminate()
            self.processes.remove(process_to_kill)
            print(f"Process with PID {pid_to_kill} killed.")
        except StopIteration:
            print(f"No process found with PID {pid_to_kill}.")

    def open_application(self):
        app_name = input("Enter application name: ")
        subprocess.Popen(app_name)

    def share_data_between_processes(self):
        # Simplified example for data sharing
        data = input("Enter data to share: ")
        subprocess.Popen(['python', 'process1.py', data])

    def execute_custom_program(self):
        program_name = input("Enter program name: ")
        subprocess.Popen(['python', program_name])

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_folder()
            elif choice == '2':
                self.create_file()
            elif choice == '3':
                self.change_file_rights()
            elif choice == '4':
                self.search_files()
            elif choice == '5':
                self.create_process()
            elif choice == '6':
                self.display_processes()
            elif choice == '7':
                self.kill_process()
            elif choice == '8':
                self.open_application()
            elif choice == '9':
                self.share_data_between_processes()
            elif choice == '10':
                self.execute_custom_program()
            elif choice == '11':
                print("Exiting Simple OS. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    simple_os = SimpleOS()
    simple_os.run()
