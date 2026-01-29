# def loadmapfile(maplist, mapattributelist, size, ucordinates, mapname):
#     maplist = []
#     mapattributelist = []
#     size.update({"XCor": 0, "YCor": 0})
#     ucordinates.update({"XCor": 0, "YCor": 0})
#     with open(f"mapdata/{mapname}.txt", 'rt') as mapfile:
#         listfile = mapfile.read().splitlines()
#         readindex = 0  # used by loadmapfile to track at which point of the data it is in the map.txt file
#         for line in listfile:
#             if readindex == 0:
#                 if "Map" in line:
#                     readindex = 1
#                 else:
#                     mapsizereader = mapfile.read().split(",")
#                     print(mapsizereader)
#             else: