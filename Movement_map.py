import copy

ListofXcor = []  # list of lists of objects showing the visuals of the ma
ListofAttributes = []  # list of lists of secondary variables for specific locations on the map
Ucordinate = {"XCor": 0, "YCor": 0}  # user coordinates used to id the user location without altering the map
Size = {"XCor": 0, "YCor": 0}  # Size of the map, for simpler access to some parameters


def resetmap(ListofXcor, ListofAttributes, Ucordinate, XCor, YCor,
             Size):  # resets the map to specific parameters, all with 'Empty' tiles both for the map as well as the attribute map
    ListofXcor.clear()  # also used to generate a new empty map
    Size.update(
        {"XCor": XCor, "YCor": YCor})  # requires XCor and YCor to be int - make sure to test input for correct input
    i = 0
    while i < XCor:
        ListofXcor.append(["_"])
        ListofAttributes.append(["0"])
        j = 0
        while j < YCor:
            ListofXcor[i].append("_")
            ListofAttributes[i].append("0")
            j += 1
        i += 1
    Ucordinate.update({"XCor": round((XCor) / 2, 0),
                       "YCor": round((YCor) / 2, 0)})  # by choice the default places the user in the center


def printmap(ListofXcor, Ucordinate,
             Size):  # outputs a print of the map with the user placed in it, without altering the main map
    Mapwithuser = copy.deepcopy(ListofXcor)  # using a temp map since exp. map size is relative small
    i = 0
    userCorX = int(Ucordinate["XCor"])
    userCorY = int(Ucordinate["YCor"])
    Mapwithuser[userCorX][userCorY] = "X"
    while i < Size["XCor"]:
        b = str(Mapwithuser[i]).replace("[", "").replace("]", "").replace(" ", "").replace(",", "").replace("'",
                                                                                                            "")  # cleans the map to an easier to read space
        print(f"{b}")
        i += 1
    Mapwithuser.clear()


def changeuserCor(Size, Ucordinate, NewXCor,
                  NewYCor):  # used to place the user on a new tile with cor NewXCor and NewYCor
    if int(NewXCor) < Size["XCor"] - 1 and int(NewYCor) < Size["YCor"]:  # requres input to be int test before
        Ucordinate.update({"XCor": NewXCor, "YCor": NewYCor})
        print(f"User has been moved to X:{NewXCor}, Y:{NewYCor}")
    else:
        print(f"Cant move User to X:{NewXCor}, Y:{NewYCor} because its outside the map")


# Movementoptions of user

def moveup(Size, Ucordinate, ListofAttributes):
    if Ucordinate["XCor"] == 0:
        print("Cant move Up")
    else:
        if ListofAttributes[int(Ucordinate["XCor"]) - 1][int(Ucordinate["YCor"])] == "X":
            print("Cant move Up")
        else:
            a = Ucordinate["XCor"]
            Ucordinate.update({"XCor": a - 1})


def movedown(Size, Ucordinate, ListofAttributes):
    if Ucordinate["XCor"] == Size["XCor"] - 1:
        print("Cant move Down")
    else:
        if ListofAttributes[int(Ucordinate["XCor"]) + 1][int(Ucordinate["YCor"])] == "X":
            print("Cant move Down")
        else:
            a = Ucordinate["XCor"]
            Ucordinate.update({"XCor": a + 1})


def moveleft(Size, Ucordinate, ListofAttributes):
    if Ucordinate["YCor"] == 0:
        print("Cant move left")
    else:
        if ListofAttributes[int(Ucordinate["XCor"])][int(Ucordinate["YCor"]) - 1] == "X":
            print("Cant move left")
        else:
            a = Ucordinate["YCor"]
            Ucordinate.update({"YCor": int(a - 1)})


def moveright(Size, Ucordinate, ListofAttributes):
    if Ucordinate["YCor"] == Size["YCor"]:
        print("Cant move right")
    else:
        if ListofAttributes[int(Ucordinate["XCor"])][int(Ucordinate["YCor"]) + 1] == "X":
            print("Cant move right")
        else:
            a = Ucordinate["YCor"]
            Ucordinate.update({"YCor": int(a + 1)})


def movementinterface(Size, Ucordinate, ListofXcor, ListofAttributes):
    x = input(
        "Directional keys are \033[0;32mW/S/A/D\033[0m enter \033[0;34mT\033[0m to pause one turn, \033[0;31mExit\033[0m to end the Program")
    match x.upper():
        case "W":
            moveup(Size, Ucordinate, ListofAttributes)
            printmap(ListofXcor, Ucordinate, Size)
            print(f"You are at a {ListofXcor[int(Ucordinate["XCor"])][int(Ucordinate["YCor"])]}")
            movementinterface(Size, Ucordinate, ListofXcor, ListofAttributes)
        case "S":
            movedown(Size, Ucordinate, ListofAttributes)
            printmap(ListofXcor, Ucordinate, Size)
            print(f"You are at a {ListofXcor[int(Ucordinate["XCor"])][int(Ucordinate["YCor"])]}")
            movementinterface(Size, Ucordinate, ListofXcor, ListofAttributes)
        case "A":
            moveleft(Size, Ucordinate, ListofAttributes)
            printmap(ListofXcor, Ucordinate, Size)
            print(f"You are at a {ListofXcor[int(Ucordinate["XCor"])][int(Ucordinate["YCor"])]}")
            movementinterface(Size, Ucordinate, ListofXcor, ListofAttributes)
        case "D":
            moveright(Size, Ucordinate, ListofAttributes)
            printmap(ListofXcor, Ucordinate, Size)
            print(f"You are at a {ListofXcor[int(Ucordinate["XCor"])][int(Ucordinate["YCor"])]}")
            movementinterface(Size, Ucordinate, ListofXcor, ListofAttributes)
        case "T":
            printmap(ListofXcor, Ucordinate, Size)
            print(f"You Rested for one turn at a {ListofXcor[int(Ucordinate["XCor"])][int(Ucordinate["YCor"])]}")
            movementinterface(Size, Ucordinate, ListofXcor, ListofAttributes)
        case "EXIT":
            print("Bye~")
        case _:
            print("Not a valid input, try again")
            movementinterface(Size, Ucordinate, ListofXcor, ListofAttributes)


def Alterlocation(Size, ListofXcor, ListofAttributes, XCor, YCor, NewTerrainType):
    if XCor > Size["XCor"] or XCor < 0:
        print("X Coordinate has to within the confines of the map ")
    else:
        if YCor > Size["YCor"] or YCor < 0:
            print("Y Coordinate has to within the confines of the map ")
        else:
            print(f"Tile at X: {XCor}, Y: {YCor} has been changed from {ListofXcor[XCor][YCor]} to {NewTerrainType}")
            ListofXcor[XCor][YCor] = NewTerrainType
            i = 0
            UpdateAttributelist(Size, ListofXcor, ListofAttributes)
            while i < len(ListofXcor):
                print(
                    str(ListofXcor[i]).replace("[", "").replace("]", "").replace(" ", "").replace(",", "").replace("'",
                                                                                                                   ""))
                i += 1


def Lookat(Size, ListofXcor, ListofAttributes, XCor, YCor):
    if XCor > Size["XCor"] or XCor < 0:
        print("X Coordinate to look at has to within the confines of the map ")
    else:
        if YCor > Size["YCor"] or YCor < 0:
            print("Y Coordinate to look at has to within the confines of the map ")
        else:
            return ListofXcor[XCor][YCor]


def UpdateAttributelist(Size, ListofXcor, ListofAttributes):
    i = 0
    while i < len(ListofXcor):
        j = 0
        while j < len(ListofXcor[i]):
            x = ListofXcor[i][j]
            match x:
                case "_":
                    ListofAttributes[i][j] = "0"
                case "T":
                    ListofAttributes[i][j] = "1"
                case "A":
                    ListofAttributes[i][j] = "1"
                case "~":
                    ListofAttributes[i][j] = "2"
                case "O":
                    ListofAttributes[i][j] = ListofAttributes[i][j]
                case "B":
                    ListofAttributes[i][j] = "X"
                case _:
                    ListofAttributes[i][j] = "X"
            j += 1
        i += 1


###Controle Block
resetmap(ListofXcor, ListofAttributes, Ucordinate, 9, 19, Size)
printmap(ListofXcor, Ucordinate, Size)
Alterlocation(Size, ListofXcor, ListofAttributes, 4, 5, "A")
Alterlocation(Size, ListofXcor, ListofAttributes, 4, 2, "T")
Alterlocation(Size, ListofXcor, ListofAttributes, 0, 0, "~")
Alterlocation(Size, ListofXcor, ListofAttributes, 0, 1, "~")
Alterlocation(Size, ListofXcor, ListofAttributes, 0, 2, "~")
Alterlocation(Size, ListofXcor, ListofAttributes, 1, 0, "~")
Alterlocation(Size, ListofXcor, ListofAttributes, 1, 1, "~")
Alterlocation(Size, ListofXcor, ListofAttributes, 1, 2, "~")
Alterlocation(Size, ListofXcor, ListofAttributes, 3, 6, "B")
print(f" You see {Lookat(Size, ListofXcor, ListofAttributes, 4, 5)} at X:4 Y:5")
print(Size)
# UpdateAttributelist(Size,ListofXcor,ListofAttributes)
# print(Ucordinate)
# changeuserCor(Size,Ucordinate,3,7)
# printmap(ListofXcor,Ucordinate, Size)
# print(Ucordinate)
# changeuserCor(Size,Ucordinate,4,9)
# printmap(ListofXcor,Ucordinate, Size)
# print(Ucordinate)
# k = 0
# while k < Size["XCor"] - 1:
#     print(f"{ListofXcor[k]}\n")
#     k += 1
# l = 0
# while l < Size["XCor"]:
#     print(f"{ListofAttributes[l]}\n")
#     l += 1
# print(Ucordinate)
movementinterface(Size, Ucordinate, ListofXcor, ListofAttributes)
