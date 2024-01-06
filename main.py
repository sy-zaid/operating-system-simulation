class OperatingSystemSimulation():
    def __init__(self):
        pass

    def mainMenu(self):
        print(f"1. User Management\n2.Service Management\n3.Process Management\n4.Backup")
        testinput = eval(input("Enter your choice(1-4): "))


if __name__ == "__main__":
    OS = OperatingSystemSimulation()
    OS.mainMenu()
