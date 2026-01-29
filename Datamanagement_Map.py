import os
import os.path

dummylist = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
dummyattributelist = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
dummycor = {"XCor": 1,"YCor":2}


def newsavemap(maplist, mapattributelist, ucordinate, mapname):
    with open(f"mapdata/{mapname}.txt", 'at') as mapfile:
        i = 0
        while i < len(maplist):
            mapfile.write(f"{str(maplist[i]).replace("[", "").replace("]", "").replace(" ", "").replace("'", "")}\n")
            i += 1
        mapfile.write("Atr\n")  # divider for later read for mapattributelist
        j = 0
        while j < len(mapattributelist):
            mapfile.write(
                f"{str(mapattributelist[j]).replace("[", "").replace("]", "").replace(" ", "").replace("'", "")}\n")
            j += 1
        mapfile.write("User\n")
        mapfile.write(f"{str(ucordinate).replace("{", "").replace("}", "").replace(" ", "").replace("'", "")}\n")
        mapfile.write("End")  # End point usable to stop reading
        mapfile.close()


def checkmapfile(mapname):  # gives out true or false if .txt file with inserted variable as name exists
    if os.path.exists(
            f"mapdata/{mapname}.txt"):  # used before saving and reading out save files to make sure they are there
        return True
    else:
        return False


def overwritemapfile(maplist, mapattributelist, mapname):
    with open(f"mapdata/{mapname}.txt", 'wt') as mapfile:
        i = 0
        while i < len(maplist):
            mapfile.write(f"{str(maplist[i]).replace("[", "").replace("]", "").replace(" ", "").replace("'", "")}\n")
            i += 1
        mapfile.write("Atr\n")  # divider for later read for mapattributelist
        j = 0
        while j < len(mapattributelist):
            mapfile.write(
                f"{str(mapattributelist[j]).replace("[", "").replace("]", "").replace(" ", "").replace("'", "")}\n")
            j += 1
        mapfile.write("User\n")
        mapfile.write(f"{str(ucordinate).replace("{", "").replace("}", "").replace(" ", "").replace("'", "")}\n")
        mapfile.write("End")  # End point usable to stop reading
        mapfile.close()


# def loadmapfile(maplist, mapattributelist, size, ucordinates, mapname):
#     maplist = []
#     mapattributelist = []
#     size.update({"XCor":0,"YCor":0})
#     ucordinates.update({"XCor":0,"YCor":0})
#     with open(f"mapdata/{mapname}.txt", 'rt') as mapfile:
#         listfile = mapfile.read().splitlines()
#         loopcounter = 0
#         xlenght = 0
#         ylenght = 0
#         for entry in listfile:
#             if entry == 'Atr':
#                 loopcounter = 0
#                 break
#             elif entry == 'End':
#                 loopcounter = 0
#                 break
#             elif loopcounter == 255:
#                 loopcounter = 0
#                 break
#             else:
#                 xlenght += 1
#                 loopcounter += 1
#         for entry in listfile:
#             if loopcounter == 0:
#                 firstline = str(entry).replace("[", "").replace("]", "").replace(" ", "").replace("'", "").replace(",","")
#                 ylenght = len(firstline)
#                 loopcounter += 1
#             else:
#                 loopcounter = 0
#                 break
#         size.update({"XCor":xlenght,"YCor":ylenght})
#         i = 0
#         j = 0
#         while i < xlenght:
#             templist = []
#             while j < ylenght:     # WIP questionable if this long code makes sense for this might have to redo save file structure for easier read access



# controleblock
# newsavemap(dummylist, dummyattributelist, dummycor, "dummylist")

# with open(f"mapdata/dummylist.txt", 'rt') as mapfile:
#     listfile = mapfile.read().splitlines()
#     print(listfile)

# def checkmapfile(mapname):             #used to check if mapfile exists used before savemap, returns True of False
