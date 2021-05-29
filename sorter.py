import shutil
import os

source = os.getcwd()
source_files = [file for file in os.listdir(source)]

# sorts file endings into folders
img = ['png', 'jpg', 'gif', 'jpeg', 'psd', 'tif']
img_folder = source + "\\Image Files"

compressed = ['zip', 'rar', '7z']
compressed_folder = source + "\\Compressed Files"

exe = ['exe', 'jar', 'msi']
exe_folder = source + "\\Exe Files"

pdf = ['pdf']
pdf_folder = source + "\\PDF Files"

document = ['txt', 'docx', 'rtf', 'xlsx', 'ppt', 'log']
document_folder = source + "\\Documents"

media = ['mp4', 'mp3']
media_folder = source + "\\Media Files"


# returns a list of duplicate files
def get_duplicates(path):
    file_list2 = [file for file in os.listdir(path)]
    duplicate_list = []

    for x in source_files:
        for y in file_list2:
            if x == y:
                duplicate_list.append(x)

    return duplicate_list

# allows for renaming of files in duplicate_list
def rename_duplicates(list1):
    for i in list1:
        new_name = input('Rename {} to a name not already taken (include file extension):\n'.format(i))
        os.rename(source + '\\' + i, source + '\\' + new_name)

# creates necessary folders
if(img_folder.replace(source, '').strip('\\') not in source_files):
    os.mkdir(img_folder)
    print("Created Image Folder")

if(compressed_folder.replace(source, '').strip('\\') not in source_files):
    os.mkdir(compressed_folder)
    print("Created Compressed Files Folder")

if(exe_folder.replace(source, '').strip('\\') not in source_files):
    os.mkdir(exe_folder)
    print("Created Exe Folder")

if(pdf_folder.replace(source, '').strip('\\') not in source_files):
    os.mkdir(pdf_folder)
    print("Created PDF Folder")

if(document_folder.replace(source, '').strip('\\') not in source_files):
    os.mkdir(document_folder)
    print("Created Documents Folder")

if(media_folder.replace(source, '').strip('\\') not in source_files):
    os.mkdir(media_folder)
    print("Created Media Folder")


# checks for duplicates in each folder and prompts the user to rename
img_dupes = get_duplicates(img_folder)
rename_duplicates(img_dupes)

compressed_dupes = get_duplicates(compressed_folder)
rename_duplicates(compressed_dupes)

exe_dupes = get_duplicates(exe_folder)
rename_duplicates(exe_dupes)

pdf_dupes = get_duplicates(pdf_folder)
rename_duplicates(pdf_dupes)

document_dupes = get_duplicates(document_folder)
rename_duplicates(document_dupes)

media_dupes = get_duplicates(media_folder)
rename_duplicates(media_dupes)

img_count = 0
compressed_count = 0
exe_count = 0
pdf_count = 0
document_count = 0
media_count = 0

# moves files to correct folder based on file ending
for file in os.listdir(source):
    for i in img:
        if file.endswith(i):
            shutil.move(file, source + '\\' + img_folder)
            img_count += 1

    for i in compressed:
        if file.endswith(i):
            shutil.move(file, source + '\\' + compressed_folder)
            compressed_count += 1

    for i in exe:
        if file.endswith(i):
            shutil.move(file, source + '\\' + exe_folder)
            exe_count += 1

    for i in pdf:
        if file.endswith(i):
            shutil.move(file, source + '\\' + pdf_folder)
            pdf_count += 1

    for i in document:
        if file.endswith(i):
            shutil.move(file, source + '\\' + document_folder)
            document_count += 1

    for i in media:
        if file.endswith(i):
            shutil.move(file, source + '\\' + media_folder)
            media_count += 1

print('Successfully moved {} image files'.format(img_count))
print('Successfully moved {} compressed files'.format(compressed_count))
print('Successfully moved {} exe files'.format(exe_count))
print('Successfully moved {} pdf files'.format(pdf_count))
print('Successfully moved {} doc files'.format(document_count))
print('Successfully moved {} media files'.format(media_count))