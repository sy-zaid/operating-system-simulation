import os,json

class File:
    def __init__(self,filename,filetype,rights = "---------"):
        self.filename = filename
        self.filetype = filetype
        self.rights = rights
        self.currentdirectory = os.getcwd()
        self.filesdict = {}


    def createFile(self):
        filename = input("Enter a file name to create: (e.g. file1.txt)")
        
        try:
            with open(os.path.join(self.currentdirectory,filename),'w'):
                pass
            print(f"File {filename} created successfully.")
        except:
            print("Exit code-1, failed to create file.")

        
