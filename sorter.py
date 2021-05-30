'''
KNOWN ERROR: Don't rename a duplicate to another duplicate in the same file, the program won't detect it and there will be an error
'''
import shutil
import os

source = os.getcwd()
source_files = [file for file in os.listdir(source)]

class folder:
    # creates class attributes
    def __init__(self, files, name):
        self.count = 0
        self.files = files
        self.name = name
        self.path = source + "\\" + name

    # creates folder if it does not exist
    def check_folder(self):
        if(self.path.replace(source, '').strip('\\') not in source_files):
            os.mkdir(self.name)
            print("Created {} Folder".format(self.name))

    # returns duplicates
    def check_duplicates(self):
        file_list = [file for file in os.listdir(self.path)]
        duplicate_list = []

        # finds files in source with same name as those in folder
        for x in os.listdir(source):
            for y in file_list:
                if x == y:
                    duplicate_list.append(x)

        return duplicate_list
    
    def move_files(self):
        for file in source_files:
            for i in self.files:
                if(file.endswith(i)):
                    shutil.move(file, self.path)
                    self.count += 1

folders = []

# adds folder objects to folders list
folders.append(folder(['png', 'jpg', 'gif', 'jpeg', 'psd', 'tif'], "Image Files"))
folders.append(folder(['zip', 'rar', '7z'], "Compressed Files"))
folders.append(folder(['exe', 'jar', 'msi'], "Exe Files"))
folders.append(folder(['pdf'], "PDF Files"))
folders.append(folder(['txt', 'docx', 'rtf', 'xlsx', 'ppt', 'log'], "Documents"))
folders.append(folder(['mp4', 'mp3'], "Media Files"))

duplicates = []

# creates necessary folders and finds files with duplicate names
for folder in folders:
    folder.check_folder()
    folder.check_duplicates()
    duplicates.append(folder.check_duplicates())

# prompts user input to rename dupes
count = 0
for file in duplicates:
    # makes sure list isn't empty
    if file:
        new_name = input('Rename {} to a name not already taken (include file extension):\n'.format(file[count]))
        os.rename(source + '\\' + file[count], source + '\\' + new_name)

# move files to appropriate folder
for folder in folders:
    folder.move_files()

# print number of files moved
for folder in folders:
    print("Successfully moved {} files to ".format(folder.count) + folder.name + " folder")
