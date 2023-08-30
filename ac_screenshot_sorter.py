import os
import shutil
from tkinter.filedialog import askdirectory

if not os.path.exists("screenshot sorter memory.txt"): # create new memory file

    path_main = askdirectory(title="Select Main Assetto Corsa folder", initialdir=r'C:')
    # print(path_main)
    path_screens = askdirectory(title="Select screenshot folder", initialdir=r'C:')
    # print(path_screens)
    path_place = askdirectory(title="Select where to store new folders", initialdir=path_screens)

    path_main = path_main.replace("/","\\")
    path_screens = path_screens.replace("/","\\")
    path_place = path_place.replace("/","\\")
    with open("screenshot sorter memory.txt", "w", encoding="utf-8") as f:
        f.write(path_main+"\n"+path_screens+"\n"+path_place)

else: # read a previously created memory file
    f = open("screenshot sorter memory.txt", "r")
    path_main = f.readline().strip()
    path_screens = f.readline().strip()
    path_place = f.readline()
    f.close()



# file_list=os.listdir(path_screens) # Get file names from directory, old code that includes folders

os.chdir(path_screens)
file_list = [f for f in os.listdir(path_screens) if os.path.isfile(f)]
file_list.remove("screenshot sorter memory.txt")
# print(file_list)
# print()

for i in file_list:
    for b in os.listdir(path_main+"\\content\\cars"): # find the name of the car
        b.replace(" ", "_") # screenshots always replace spaces with underscores and uppercase with lowercase
        car_string_length = len(b)
    

        if i[11:11+car_string_length] == b.lower(): # 11 = bypass Screenshot_

            if not os.path.exists(path_place+f"\\{b}"): # create a new folder if there isn't already one
                os.mkdir(path_place+f"\\{b}")
            shutil.move(path_screens+f"\\{i}", path_place+f"\\{b}\\{i}")

            break # go on to next screenshot