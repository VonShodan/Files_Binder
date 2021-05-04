import os
import time
import shutil

from datetime import datetime


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

print("Hello in Photo Segregate by Date'or !")
folder = r'D:\PROJEKTY\PYTHON\Segregator_Plikow\Testowe_zdjecia'
# Tworzymy date_folders która przechowuje dane na temat czasu utworzenia plikow
date_files = {}
date_folders = []
# do zmiennej list_of_files wpajamy liste plików (typ list)
list_of_files = os.listdir(folder)
# dla kazdej cześci listy :
for src in list_of_files:
    # tutaj dodajemy do adresu folderu nazwę pliku, by miec pelny adres
    full_src = os.path.join(folder, src)
    if os.path.isfile(full_src):
        # time.ctime przelicza sekundy na %a %b %d %H:%M:%S %Y
        date_of_birth_file = time.ctime(os.stat(full_src).st_mtime)
        # tutaj tworzymy datetimeobjecta w typie datetime
        datetimeobject = datetime.strptime(date_of_birth_file, '%a %b %d %H:%M:%S %Y')
        # konwertujemy na chciane :D
        newformat = datetimeobject.strftime('%Y - %m')
        date_files[src] = newformat
        # poniżej sprawdzamy, czy date_folders puste - jezeli tak to dodajemy
        # newformat,
        # jeszcze nizej sprawedzanie, czy nie ma newformata w date_folders
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
