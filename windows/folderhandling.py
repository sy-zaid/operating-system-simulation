import os,json,time,shutil

class Folder:
    """
    A class representing and managing all the folders in an OS.

    VARIABLES:
    --- self.foldersdict == for storing the details about all the folders with folder names as keys.
        syntax: {"foldername":{"foldername": foldername, "folderpath": folderpath, "folderrights": folderrights}}

    """
    def __init__(self, foldername=None, rights="---------"):
        self.foldername = foldername
        self.rights = rights
        # self.currentdirectory = os.getcwd()
        self.currentdirectory = "./home"
        self.foldersdata = "./windows/folders_data.json"
        self.foldersdict = {}
        self.loadFolderDetails()
        self.saveFolderDetails()

    def createFolder(self):
        self.loadFolderDetails()
        print("\nCreating a new folder...")
        foldername = input("Enter a folder name to create: (e.g. folder1) # ")
        folderrights = "rwx------"  # Default rights set here when creating a folder.
        newfolder = {}
        folderpath = os.path.join(self.currentdirectory, foldername)
        try:
            os.makedirs(folderpath)
            newfolder["foldername"] = foldername
            newfolder["folderpath"] = folderpath
            newfolder["folderrights"] = folderrights
            self.foldersdict[foldername] = newfolder
            self.saveFolderDetails()

            print(f"\nFolder {foldername} created successfully.")
        except FileExistsError:
            print("\nExit code-1 | failed to create folder as it already exists.")
        except Exception as e:
            print(f"\nExit code-1 | failed to create folder. {e}")

    def searchFolder(self):
        print("\nSearching for a folder...")
        self.loadFolderDetails()
        inp_foldername = input("Enter a folder name to search # ")
        print("\nSearching...")
        time.sleep(1.5)
        if inp_foldername in self.foldersdict:
            print(f"\nFolder found with name {inp_foldername} :) | Type 'm' and press enter to show details # ")
            temp = input("")
            if temp == "m":
                self._displayFolderDetails(inp_foldername)
            else:
                return True
        else:
            print(f"\nFolder NOT found with name {inp_foldername}. :()")
            return False

    def listFolders(self):
        self.loadFolderDetails()
        for key in self.foldersdict:
            print(f"\n{key}")

    def deleteFolder(self):
        print("\nDeleting a folder... ")
        self.loadFolderDetails()
        inp_foldername = input("Enter a folder name to delete it OR 'cancel' to cancel the operation # ")
        if inp_foldername != "cancel" and inp_foldername in self.foldersdict:
            try:
                os.rmdir(self.foldersdict[inp_foldername]["folderpath"])
                del self.foldersdict[inp_foldername]
                self.saveFolderDetails()
                print(f"\nSuccessfully deleted {inp_foldername} :)")
            except:
                print("\nFolder deletion unsuccessful :(")
        else:
            print("\nOperation cancelled :|")

    def changeFolderRights(self):
        print("\nChanging the rights of the folder...")
        self.loadFolderDetails()
        inp_foldername = input("Enter the folder name you want to change rights of OR 'cancel' to cancel the operation # ")

        if inp_foldername != "cancel" and inp_foldername in self.foldersdict:
            print(f"\nThe details for {inp_foldername} are:")
            self._displayFolderDetails(inp_foldername)
            inp_rights = input("Enter rights in rwxrwxrwx format # ")
            curfolder = self.foldersdict.get(inp_foldername)
            curfolder["folderrights"] = str(inp_rights)
            print(f"\nFolder {inp_foldername} rights updated successfully.")
            print(f"\nUpdated rights are:")
            self._displayFolderDetails(inp_foldername)
        else:
            print("\nOperation cancelled :| ")
    
    def backupAllFolders(self):
        
        """
        Backup all folders from the source directory to the destination directory.

        Parameters:
        - source_directory (str): The path to the source directory.
        - destination_directory (str): The path to the destination directory.
        """
        destination_directory = input("Enter the path to backups folder # ")
        try:
            # Create the destination directory if it doesn't exist
            os.makedirs(destination_directory, exist_ok=True)

            # List all folders in the source directory
            folders = [f for f in os.listdir(self.currentdirectory) if os.path.isdir(os.path.join(self.currentdirectory, f))]

            # Backup each folder to the destination directory
            for folder in folders:
                source_path = os.path.join(self.currentdirectory, folder)
                destination_path = os.path.join(destination_directory, folder)

                shutil.copy2(source_path, destination_path)  # Copy folder with metadata

            print(f"\nBackup successfull! Folders backed up from {self.currentdirectory} to {destination_directory}")
        except Exception as e:
            print(f"\nBackup failed. Error: {e}")

    def _displayFolderDetails(self, foldername):
        folder_details = self.foldersdict.get(foldername, {})  # Get folder details or an empty dictionary if not found
        # Iterate over keys and values and print them
        for key, value in folder_details.items():
            print(f"{key}: {value}")
        

    def saveFolderDetails(self):
        try:
            with open(self.foldersdata, 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = {}  # Initialize with an empty dictionary if the file doesn't exist

        existing_data.update(self.foldersdict)  # Update existing data with new data

        with open(self.foldersdata, 'w') as file:
            json.dump(existing_data, file)

    def loadFolderDetails(self):
        try:
            with open(self.foldersdata, 'r') as file:
                self.foldersdict = json.load(file)
        except FileNotFoundError:
            print(f"File '{self.foldersdata}' not found. Creating a new one. :)")

folder1 = Folder()
# folder1.createFolder()
# folder1.changeFolderRights()
# folder1.searchFolder()
folder1.backupAllFolders()
