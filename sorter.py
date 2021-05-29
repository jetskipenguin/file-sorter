import shutil
import os

source = r'X:\Downloads'

# sorts file endings into folders
img = ['png', 'jpg', 'gif', 'jpeg', 'psd', 'tif']
img_folder = 'Image Files'

compressed = ['zip', 'rar', '7z']
compressed_folder = 'Compressed Files'

exe = ['exe', 'jar', 'msi']
exe_folder = 'Executable Files'

pdf = ['pdf']
pdf_folder = "PDF Files"

document = ['txt', 'docx', 'rtf', 'xlsx', 'ppt', 'log']
document_folder = 'Doc Files'

media = ['mp4', 'mp3']
media_folder = 'Media Files'


# returns a list of duplicate files
def get_duplicates(path1, path2):
    file_list1 = [file for file in os.listdir(path1)]
    file_list2 = [file for file in os.listdir(path2)]
    duplicate_list = []

    for x in file_list1:
        for y in file_list2:
            if x == y:
                duplicate_list.append(x)

    return duplicate_list


# allows for renaming of files in duplicate_list
def rename_duplicates(list1):
    for i in list1:
        new_name = input('Rename {} to a name not already taken (include file extension):\n'.format(i))
        os.rename(source + '\\' + i, source + '\\' + new_name)


# checks for duplicates in each folder and prompts the user to rename
img_dupes = get_duplicates(source, source + '\\' + img_folder)
rename_duplicates(img_dupes)

compressed_dupes = get_duplicates(source, source + '\\' + compressed_folder)
rename_duplicates(compressed_dupes)

exe_dupes = get_duplicates(source, source + '\\' + exe_folder)
rename_duplicates(exe_dupes)

pdf_dupes = get_duplicates(source, source + '\\' + pdf_folder)
rename_duplicates(pdf_dupes)

document_dupes = get_duplicates(source, source + '\\' + document_folder)
rename_duplicates(document_dupes)

media_dupes = get_duplicates(source, source + '\\' + media_folder)
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