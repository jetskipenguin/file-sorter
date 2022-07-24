import shutil
import os

source = os.getcwd()

class folder:
    # creates class attributes
    def __init__(self, files, name):
        self.count = 0
        self.files = [file for file in os.listdir(source)]
        self.name = name
        self.path = source + "\\" + name

    # creates folder if it does not exist
    def check_folder(self):
        if(self.path.replace(source, '').strip('\\') not in self.files):
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

        # flatten list and return
        return duplicate_list
    
    def move_files(self):
        for file in os.listdir(source):
            for i in self.files:
                if(file.endswith(i)):
                    shutil.move(file, self.path)
                    self.count += 1

folders = []

# adds folder objects to folders list
folders.append(folder(['png', 'jpg', 'gif', 'jpeg', 'psd', 'tif', 'jfif'], "Image Files"))
folders.append(folder(['zip', 'rar', '7z'], "Compressed Files"))
folders.append(folder(['exe', 'jar', 'msi'], "Exe Files"))
folders.append(folder(['pdf'], "PDF Files"))
folders.append(folder(['txt', 'docx', 'rtf', 'xlsx', 'ppt', 'log', 'pptx'], "Documents"))
folders.append(folder(['mp4', 'mp3'], "Media Files"))

duplicates = []

# creates necessary folders and finds files with duplicate names
for folder in folders:
    folder.check_folder()
    duplicates.append(folder.check_duplicates())

# prompts user input to rename dupes
print(duplicates)
count = 0
for file in duplicates:
    if file:
        name = file[count].split('.')[0]
        extension = file[count].split('.')[1]
        for num in range(1, 10000):
            new_name = name + f'({num}).' + extension
            if new_name not in os.listdir(source):
                os.rename(source + '\\' + file[count], source + '\\' + new_name)
                break
        count += 1

# move files to appropriate folder
for folder in folders:
    folder.move_files()

# print number of files moved
for folder in folders:
    print("Successfully moved {} files to ".format(folder.count) + folder.name + " folder")
