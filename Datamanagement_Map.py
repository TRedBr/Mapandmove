import os
import os.path

dummylist = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
dummyattributelist = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
dummycor = {"XCor": 1, "YCor": 2}
dummysize = {"XCor": 3, "YCor": 3}


# def newsavemap(maplist, mapattributelist, ucordinate, mapname, size): #supperflous
#     with open(f"mapdata/{mapname}.txt", 'at') as mapfile:
#         i = 0
#         mapfile.write("Size\n")
#         mapfile.write(f"{size["XCor"]}:{size["YCor"]}\n")
#         while i < len(maplist):
#             mapfile.write(f"{str(maplist[i]).replace("[", "").replace("]", "").replace(" ", "").replace("'", "")}\n")
#             i += 1
#         mapfile.write("Atr\n")  # divider for later read for mapattributelist
#         j = 0
#         while j < len(mapattributelist):
#             mapfile.write(
#                 f"{str(mapattributelist[j]).replace("[", "").replace("]", "").replace(" ", "").replace("'", "")}\n")
#             j += 1
#         mapfile.write("User\n")
#         mapfile.write(f"{ucordinate["XCor"]}:{ucordinate["YCor"]}\n")
#         mapfile.write("End")  # End point usable to stop reading
#         mapfile.close()


def checkmapfile(mapname):  # gives out true or false if .txt file with inserted variable as name exists
    if os.path.exists(
            f"mapdata/{mapname}.txt"):  # used before saving and reading out save files to make sure they are there
        return True
    else:
        return False


def overwritemapfile(maplist, mapattributelist, ucordinate, mapname, size):
    with open(f"mapdata/{mapname}.txt", 'wt') as mapfile:
        i = 0
        mapfile.write(f"{size["XCor"]},{size["YCor"]}\n")
        mapfile.write("Map\n")
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
        mapfile.write(f"{ucordinate["XCor"]},{ucordinate["YCor"]}\n")
        mapfile.write("End")  # End point usable to stop reading
        mapfile.close()



# controleblock
# newsavemap(dummylist, dummyattributelist, dummycor, "dummylist")

# with open(f"mapdata/dummylist.txt", 'rt') as mapfile:
#     listfile = mapfile.read().splitlines()
#     print(listfile)

# def checkmapfile(mapname):             #used to check if mapfile exists used before savemap, returns True of False
