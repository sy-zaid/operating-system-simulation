import psutil

class TaskManager:
    def __init__(self):
        self.running_processes = []

    def display_processes(self):
        self.running_processes = [p for p in psutil.process_iter(['pid', 'name', 'status'])]
        # Display the list of processes

    def kill_process(self, pid):
        try:
            process = psutil.Process(pid)
            process.terminate()
            print(f"Process {pid} terminated.")
        except psutil.NoSuchProcess:
            print(f"Process {pid} not found.")

# Example usage:
task_manager = TaskManager()
task_manager.display_processes()
# task_manager.kill_process(1234)  # Replace 1234 with the actual PID
