import os.path                              #planning to use in checkmapfile(Mapname)

Dummylist = [["_","_","_"],["_","_","_"],["_","_","_"]]
Dummyattributelist = [["0","0","0"],["0","0","0"],["0","0","0"]]

def newsavemap(Maplist, Mapattributelist, Mapname):
    with open(f"mapdata/{Mapname}.txt", 'at') as Mapfile:
        i = 0
        while i < len(Maplist):
            Mapfile.write(f"{str(Maplist[i]).replace("[", "").replace("]", "").replace(" ", "").replace("'", "")}\n")
            i += 1
        Mapfile.write("Atr\n")                          #divider for later read for Mapattributelist
        j = 0
        while j < len(Mapattributelist):
            Mapfile.write(f"{str(Mapattributelist[j]).replace("[", "").replace("]", "").replace(" ", "").replace("'", "")}\n")
            j += 1

newsavemap(Dummylist, Dummyattributelist, "dummylist")

#def checkmapfile(Mapname):             #used to check if mapfile exists used before savemap, returns True of False
