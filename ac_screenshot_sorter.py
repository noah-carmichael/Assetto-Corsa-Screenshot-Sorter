import os
import shutil
from tkinter.filedialog import askdirectory
from tkinter import messagebox


if not os.path.exists("screenshot sorter memory.txt"): # create new memory file

    path_main = askdirectory(title="Select Main Assetto Corsa folder", initialdir=r'C:')
    # print(path_main)
    path_screens = askdirectory(title="Select screenshot folder", initialdir=r'C:')
    # print(path_screens)
    path_place = askdirectory(title="Select where to store new folders", initialdir=path_screens)

    path_main = path_main.replace("/","\\")
    path_screens = path_screens.replace("/","\\")
    path_place = path_place.replace("/","\\")

    sort_way = messagebox.askyesno("Select sorting method","Sort by Car (recommended)? Click 'No' to sort by track instead") # true = car, false = track
    if sort_way == True:
        sort_way = "Car"
    else:
        sort_way = "Track"

    with open("screenshot sorter memory.txt", "w", encoding="utf-8") as f:
        f.write(path_main+"\n"+path_screens+"\n"+path_place+"\n"+sort_way)

else: # read a previously created memory file
    f = open("screenshot sorter memory.txt", "r")
    path_main = f.readline().strip()
    path_screens = f.readline().strip()
    path_place = f.readline().strip()
    sort_way = f.readline()
    f.close()




# file_list=os.listdir(path_screens) # Get file names from directory, old code that includes folders

os.chdir(path_screens)
file_list = [f for f in os.listdir(path_screens) if os.path.isfile(f)]
file_list.remove("screenshot sorter memory.txt")
# print(file_list)
# print()

# sort by car:
if sort_way == "Car":
    for i in file_list:
        for b in os.listdir(path_main+"\\content\\cars"): # find the name of the car
            b.replace(" ", "_") # screenshots always replace spaces with underscores and uppercase with lowercase
            car_string_length = len(b)
        

            if i[11:11+car_string_length] == b.lower(): # 11 = bypass Screenshot_

                if not os.path.exists(path_place+f"\\{b}"): # create a new folder if there isn't already one
                    os.mkdir(path_place+f"\\{b}")
                shutil.move(path_screens+f"\\{i}", path_place+f"\\{b}\\{i}")

                break # go on to next screenshot



# sort by track:
else: 
    tracklist = []
    for c in os.listdir(path_main+"\\content\\tracks"): # find name of track
        c.replace(" ", "_")
        tracklist.append(c.lower())
                    
    for i in file_list:
        for b in os.listdir(path_main+"\\content\\cars"): # find the name of the car
            b.replace(" ", "_") # screenshots always replace spaces with underscores and uppercase with lowercase
            car_string_length = len(b)
        
            for track in tracklist:
                if i[11+car_string_length:11+car_string_length+len(track)] == track: # 11 = bypass Screenshot_

                    if not os.path.exists(path_place+f"\\{track}"): # create a new folder if there isn't already one
                        os.mkdir(path_place+f"\\{track}")
                    shutil.move(path_screens+f"\\{i}", path_place+f"\\{track}\\{i}")

                    break # go on to next screenshot
            else:
                continue
            break