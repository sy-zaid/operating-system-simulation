import os,json

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
            with open(filepath,'w'):
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
        self.loadFileDetails()
        inp_filename = input("Enter a filename to search # ")
        if self.filesdict[inp_filename]:
            print(f"File found with name {inp_filename}. Type m to show details # ")
            temp = input("")
        

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
