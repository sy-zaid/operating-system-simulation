import os,json,time,shutil

class Folder:
    """
    A class representing and managing all the folders in an OS.

    VARIABLES:
    --- self.foldersdict == for storing the details about all the folders with folder names as keys.
        syntax: {"foldername":{"foldername": foldername, "folderpath": folderpath,"owner":currentuser,"folderrights": folderrights}}

    """
    def __init__(self, foldername=None,currentuser = None,rights="---------"):
        self.foldername = foldername
        self.currentuser = currentuser
        self.rights = rights
        self.currentdirectory = "./home"
        self.foldersdata = "./windows/folders_data.json"
        self.foldersdict = {}
        self.loadFolderDetails()
        self.saveFolderDetails()

    def createFolder(self):
        """
         This method provides a structured way to create folders
         within a directory, manage their details in a dictionary.
        
         Creating a new folder...
         Enter a folder name to create: (e.g. folder1) # Talha

         Folder Talha created successfully.

        """
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
            newfolder["owner"] = self.currentuser
            newfolder["folderrights"] = folderrights
            self.foldersdict[foldername] = newfolder
            self.saveFolderDetails()

            print(f"\nFolder {foldername} created successfully.")
        except FileExistsError:
            print("\nExit code-1 | failed to create folder as it already exists.")
        except Exception as e:
            print(f"\nExit code-1 | failed to create folder. {e}")

    def searchFolder(self):
        """
        Searches the desired folder.

                
        Searching for a folder...
        Enter a folder name to search #
        
        """
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
        """
        Lists all the existing folders down

        Below are all the folders created in OS

        Talha
        1. Files Services
        2. Folder Services
        3. Home
        Choose an option (1-3) #
        
        """
        print(f"\nBelow are all the folders created in OS")
        self.loadFolderDetails()
        for key in self.foldersdict:
            print(f"\n{key}")

    def deleteFolder(self):
        """
        This method is designed to delete a folder and
        remove its details from the foldersdict dictionary and storage.
        

        Deleting a folder...
        Enter a folder name to delete it OR 'cancel' to cancel the operation #
        
        The cancel will break operation.

        """

        print("\nDeleting a folder... ")
        self.loadFolderDetails()
        inp_foldername = input("Enter a folder name to delete it OR 'cancel' to cancel the operation # ")
        if inp_foldername != "cancel" and inp_foldername in self.foldersdict:
            try:
                os.rmdir(self.foldersdict[inp_foldername]["folderpath"])
                del self.foldersdict[inp_foldername]
                with open(self.foldersdata, 'w') as file:
                    json.dump(self.foldersdict, file)
                self.saveFolderDetails()
                print(f"\nSuccessfully deleted {inp_foldername} :)")
            except:
                print("\nFolder deletion unsuccessful :(")
        else:
            print("\nOperation cancelled :|")

    def changeFolderRights(self):
        """
        The changeFolderRights() method appears designed to modify
        the permissions (rights) of a folder stored in self.foldersdict.

        """
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
        # destination_directory = os.path.abspath(input("Enter the path to backups folder # "))
        destination_directory = './'
        try:
            # Create the destination directory if it doesn't exist
            os.makedirs(destination_directory, exist_ok=True)
            shutil.copytree(self.currentdirectory, os.path.join(destination_directory, 'backup')) # Copying folder with metadata
            print(f"\nBackup successfull! Folders backed up from {self.currentdirectory} to {destination_directory}")
        except Exception as e:
            print(f"\nBackup failed. Error: {e}")

    def _displayFolderDetails(self, foldername):
        """
        This method provides a way to present the details of a specified
        folder stored in the foldersdict dictionary.
        
        """

        folder_details = self.foldersdict.get(foldername, {})  # Get folder details or an empty dictionary if not found
        # Iterate over keys and values and print them
        for key, value in folder_details.items():
            print(f"{key}: {value}")
        

    def saveFolderDetails(self):
        """
         This method provides a structured way to update or create a folder containing
         folder details and handles potential exceptions that might occur during the process
        
         Functionalities:
            -Load Existing Data (if available)
            -Handling Folder Not Found
            -Update Data
            -Save Updated Data to File
        """
        
        try:
            with open(self.foldersdata, 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = {}  # Initialize with an empty dictionary if the file doesn't exist

        existing_data.update(self.foldersdict)  # Update existing data with new data

        with open(self.foldersdata, 'w') as file:
            json.dump(existing_data, file)

    def loadFolderDetails(self):
        """
        This method provides a structured approach to load
        previously saved folder details from a file into a dictionary
        
        Functionalities:
            -File reading
            -Loading Data
            -Handling not found
        """
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
