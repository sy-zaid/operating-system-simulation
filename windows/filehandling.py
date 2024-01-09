import os,json,time
import shutil

class File:
    """
    A class representing and managing all the files in an OS.

    VARIABLES:
    --- self.filesdict == for storing the details about all the files with filenames as keys.
        syntax: {"filename":{"filename":filename,"filetype":filetype,"filesize":filesize,"filepath":filepath,"owner":currentuser,filerights":filerights}}

    """
    def __init__(self,filename = None,filetype = None ,currentuser = None,rights = "---------"):
        self.filename = filename
        self.filetype = filetype
        self.currentuser = currentuser
        self.rights = rights
        self.currentdirectory = "./home"
        self.filesdata = "./windows/files_data.json"
        self.filesdict = {}
        self.loadFileDetails()
        self.saveFileDetails()


    def createFile(self):
        """
            Creates a file of user's choice
            
            Creating a new file...
            Enter a file name to create: (e.g. file1.txt) #
            
            """
        self.loadFileDetails()
        print("\nCreating a new file...")
        filename = input("Enter a file name to create: (e.g. file1.txt) # ")
        filetype = filename.split('.')[-1]
        filerights = "rwx------" #Default rights set here when creating a file.
        newfile = {}
        filepath = os.path.join(self.currentdirectory,filename)

        try:
            with open(filepath,'x'):
                newfile["filename"] = filename
                newfile["filetype"] = filetype
                newfile["filesize"] = os.path.getsize(filepath) #Gets the size of the current file.
                newfile["filepath"] = filepath
                newfile["owner"] = self.currentuser
                newfile["filerights"] = filerights
                self.filesdict[f"{filename}"] = newfile
                self.saveFileDetails()

            print(f"\nFile {filename} created successfully.")
        except FileExistsError:
            print("\nExit code-1 | failed to create file as it already exists.")
        
        except Exception as e:
            print(f"\nExit code-1 | failed to create file. {e}")

    def searchFile(self):
        """
        Searches for existing files 

        Searching for a file...
        Enter a filename to search #
        
        """
        print("\nSearching for a file...")
        self.loadFileDetails()
        inp_filename = input("Enter a filename to search # ")
        print("\nSearching...")
        time.sleep(1.5)
        if inp_filename in self.filesdict:
            print(f"\nFile found with name {inp_filename} :) | Type m and press enter to show details # ")
            temp = input("")
            if temp == "m":
                self._displayFileDetails(inp_filename)
            else:
                return True
        else:
            print(f"\nFile NOT found with name {inp_filename} :(")
            return False
    
    def listFiles(self):
        """
        This method lists down all the existing files.

         Below are all the files created in OS
        Home
        1. Files Services
        2. Folder Services
        3. Home
        Choose an option (1-3) #
        
        """
        print(f"\nBelow are all the files created in OS")
        self.loadFileDetails()
        for key in self.filesdict:
            print(f"\n{key}")


    def deleteFile(self):
        """
        This function deletes a file if exists, and "Cancel" will stop operation

        Deleting a file...
        Enter a filename to delete it OR 'cancel' to cancel the operation #

        """

        print("\nDeleting a file... ")
        self.loadFileDetails()
        inp_filename = input("Enter a filename to delete it OR 'cancel' to cancel the operation # ")
        if inp_filename != "cancel" and inp_filename in self.filesdict:
            try:
                file_path = os.path.join(self.filesdict.get(inp_filename)["filepath"])
                os.remove(file_path)
                del self.filesdict[inp_filename]
                with open(self.filesdata, 'w') as file:
                    json.dump(self.filesdict, file)
                self.saveFileDetails()
                print(f"\nSuccessfully deleted {inp_filename} :)")
            except:
                print("\nFile deletion unsuccessful :(")
        else:
            print("\nOperation cancelled :|")

    def changeFileRights(self):
        """
        This method interacts with the user to change
        the file rights within the self.filesdict dictionary
        and displays the updated information after the change is made.
        
        """
        print("\nChanging the rights of the file...")
        self.loadFileDetails()
        inp_filename = input("Enter the filename you want to change rights of OR 'cancel' to cancel the operation # ")
        
        if inp_filename != "cancel" and inp_filename in self.filesdict:
            print(f"\nThe details for {inp_filename} are:")
            self._displayFileDetails(inp_filename)
            inp_rights = input("Enter rights in rwxrwxrwx format # ")
            curfile = self.filesdict.get(inp_filename)
            curfile["filerights"] = str(inp_rights)
            print(f"\nFile {inp_filename} rights updated successfully.")
            print(f"\nUpdated rights are:")
            self._displayFileDetails(inp_filename)
        
        else:
            print("\nOperation cancelled :| ")

    def getCurrentUser(self):
        return self.currentuser
    
    def backupAllFiles(self):
        
        """
        Backup all files from the source directory to the destination directory.

        Parameters:
        - source_directory (str): The path to the source directory.
        - destination_directory (str): The path to the destination directory.
        """
        destination_directory = input("Enter the path to backups folder # ")
        try:
            # Create the destination directory if it doesn't exist
            os.makedirs(destination_directory, exist_ok=True)

            # List all files in the source directory
            files = [f for f in os.listdir(self.currentdirectory) if os.path.isfile(os.path.join(self.currentdirectory, f))]

            # Backup each file to the destination directory
            for file in files:
                source_path = os.path.join(self.currentdirectory, file)
                destination_path = os.path.join(destination_directory, file)

                shutil.copy2(source_path, destination_path)  # Copy file with metadata

            print(f"\nBackup successfull! Files backed up from {self.currentdirectory} to {destination_directory}")
        except Exception as e:
            print(f"\nBackup failed. Error: {e}")

        

    def _displayFileDetails(self, filename):
        file_details = self.filesdict.get(filename, {})  # Get file details or an empty dictionary if not found
        # Iterate over keys and values and print them
        for key, value in file_details.items():
            print(f"{key}: {value}")


    def saveFileDetails(self):
        try:
            with open(self.filesdata, 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = {}  # Initialize with an empty dictionary if the file doesn't exist
        
        existing_data.update(self.filesdict)  # Update existing data with new data

        with open(self.filesdata, 'w') as file:
            json.dump(existing_data, file)

        
    def loadFileDetails(self):
        """
        This function aims to load previously saved file details into the program
        """
        try:
            with open(self.filesdata, 'r') as file:
                self.filesdict = json.load(file)
        except FileNotFoundError:
            print(f"File '{self.filesdata}' not found. Creating a new one. :)")

        
# file1 = File()
# file1.createFile()
# # file1.changeFileRights()
# file1.deleteFile()
# file1.searchFile()
