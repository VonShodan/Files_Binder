import os
import time
import shutil
from datetime import datetime

date_files = {}
date_folders = []
list_of_files = []
folder = ""


def check_and_add(lst_to_check, thing):
    perm = True
    for e in lst_to_check:
        if e == thing:
            perm = False
    if perm:
        lst_to_check.append(thing)
    return lst_to_check


def make_dir_from_lst(lst_of_names, place_of_folders):

    for folder_name in lst_of_names:
        dir_ = folder_name
        parent_dir = place_of_folders
        path = os.path.join(parent_dir, dir_)
        try:
            os.mkdir(path)
        except FileExistsError:
            print("Chyba sie zagalopowales, bo taki folderek już istenieje!")
    return


print("Hello in File Binder !")
input_error = 0
while input_error == 0:
    input_error = 1
    print(r"Example of link to folder: C:\Users\Dziki_ryk\Desktop\My_photos")
    folder = input("Please, put here link to folder with your files! : ")
    try:
        list_of_files = os.listdir(folder)
    except FileNotFoundError:
        print("Problem with your folder address, please check and try again ")
        input_error = 0
# for the anyone part of list:
for src in list_of_files:
    # here we join file name to fille address
    full_src = os.path.join(folder, src)
    if os.path.isfile(full_src):
        # time.ctime converse seconds to %a %b %d %H:%M:%S %Y format
        date_of_birth_file = time.ctime(os.stat(full_src).st_mtime)
        # here we create datetimeobject in datetime type
        datetimeobject = datetime.strptime(date_of_birth_file, '%a %b %d %H:%M:%S %Y')
        # converting to format what we need :D
        newformat = datetimeobject.strftime('%Y - %m')
        date_files[src] = newformat
        # below checking if date_folders is empty - if yes, we add newformat
        # even lower checking, if value of newformat exist in date_folders
        if len(date_folders) == 0:
            date_folders.append(newformat)
        else:
            date_folders = check_and_add(date_folders, newformat)

make_dir_from_lst(date_folders, folder)

for my_file in date_files:
    full_src = os.path.join(folder, my_file)
    if os.path.isfile(full_src):
        dst = os.path.join(folder, date_files[my_file])
        shutil.move(full_src, dst)

print("Done! Bye! <3")
