import os,json,time

class File:
    """
    A class representing and managing all the files in an OS.

    VARIABLES:
    --- self.filesdict == for storing the details about all the files with filenames as keys.
        syntax: {"filename":{"filename":filename,"filetype":filetype,"filesize":filesize,"filerights":filerights}}

    """
    def __init__(self,filename = None,filetype = None ,rights = "---------"):
        self.filename = filename
        self.filetype = filetype
        self.rights = rights
        self.currentdirectory = os.getcwd()
        self.filesdata = "files_data.json"
        self.filesdict = {}
        self.loadFileDetails


    def createFile(self):
        print("Creating a new file...\n")
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
                newfile["filerights"] = filerights
                self.filesdict[f"{filename}"] = newfile
                self.saveFileDetails()

            print(f"File {filename} created successfully.")
        except FileExistsError:
            print("Exit code-1 | failed to create file as it already exists.")
        
        except Exception as e:
            print(f"Exit code-1 | failed to create file. {e}")

    def searchFile(self):
        print("Searching for a file...\n")
        self.loadFileDetails()
        inp_filename = input("Enter a filename to search # ")
        print("Searching...\n")
        time.sleep(1.5)
        if inp_filename in self.filesdict:
            print(f"File found with name {inp_filename}. Type m and press enter to show details # ")
            temp = input("")
            if temp == "m":
                self._displayFileDetails(inp_filename)
            else:
                return True
        else:
            print(f"File NOT found with name {inp_filename}.")
            return False


    def deleteFile(self):
        print("Deleting a file... ")
        self.loadFileDetails()
        inp_filename = input("Enter a filename to delete it OR 'cancel' to cancel to operation # ")
        if inp_filename != "cancel" and inp_filename in self.filesdict:
            try:
                del self.filesdict[inp_filename]
                print(f"Successfully deleted {inp_filename}")
            except:
                print("File deletion unsuccessful :(")
        
        else:
            print("Operation cancelled :|")
        
        




    def _displayFileDetails(self, filename):
        file_details = self.filesdict.get(filename, {})  # Get file details or an empty dictionary if not found
        # Iterate over keys and values and print them
        for key, value in file_details.items():
            print(f"{key}: {value}")

    


    def saveFileDetails(self):
        with open(self.filesdata, 'w') as file:
            json.dump(self.filesdict, file)
        
    def loadFileDetails(self):
        try:
            with open(self.filesdata, 'r') as file:
                self.filesdict = json.load(file)
        except FileNotFoundError:
            print(f"File '{self.filesdata}' not found. Creating a new one.")

        
file1 = File()
file1.createFile()
# file1.searchFile()
