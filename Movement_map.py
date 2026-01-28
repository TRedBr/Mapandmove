import copy

ListofXcor = []
ListofAttributes = []
Ucordinate = {"XCor":0 , "YCor":0}
Size = {"XCor":0 , "YCor":0}

def resetmap(ListofXcor, ListofAttributes,Ucordinate,XCor,YCor,Size):
    ListofXcor.clear()
    Size.update({"XCor":XCor, "YCor":YCor})
    i = 0
    while i < XCor:
        ListofXcor.append(["_"])
        #ListofAttributes.append(["0"])
        j = 0
        while j < YCor:
            ListofXcor[i].append("_")
            #ListofAttributes[j].append("0")
            j += 1
        i +=1
    Ucordinate.update({"XCor":round((XCor)/2, 0), "YCor":round((YCor)/2, 0)})

def printmap(ListofXcor, Ucordinate, Size):
    Mapwithuser = copy.deepcopy(ListofXcor)                                                                             #using a temp map since exp. map size is relative small
    i = 0
    x = int(Ucordinate["XCor"])
    y = int(Ucordinate["YCor"])
    Mapwithuser[x][y] = "X"
    while i < Size["XCor"]:
        b = str(Mapwithuser[i]).replace("[","").replace("]","").replace(" ","").replace(",","").replace("'","")
        print(f"{b}")
        i += 1
    Mapwithuser.clear()


def changeuserCor(Size,Ucordinate,NewXCor,NewYCor):
    if int(NewXCor) < Size["XCor"]-1 and int(NewYCor) < Size["YCor"]:
        Ucordinate.update({"XCor":NewXCor, "YCor":NewYCor})
        print(f"User has been moved to X:{NewXCor}, Y:{NewYCor}")
    else:
        print(f"Cant move User to X:{NewXCor}, Y:{NewYCor} because its outside the map")

def moveup(Size,Ucordinate):
    if Ucordinate["XCor"] == 0:
        print("Cant move Up")
    else:
        a = Ucordinate["XCor"]
        Ucordinate.update({"XCor": a-1})

def movedown(Size,Ucordinate):
    if Ucordinate["XCor"] == Size["XCor"]-1:
        print("Cant move Down")
    else:
        a = Ucordinate["XCor"]
        Ucordinate.update({"XCor" : a+1 })


def moveleft(Size,Ucordinate):
    if Ucordinate["YCor"] == 0:
        print("Cant move left")
    else:
        a = Ucordinate["YCor"]
        Ucordinate.update({"YCor" : int(a-1)})

def moveright(Size,Ucordinate):
    if Ucordinate["YCor"] == Size["YCor"]:
        print("Cant move right")
    else:
        a = Ucordinate["YCor"]
        Ucordinate.update({"YCor": int(a+1)})

def movementinterface(Size,Ucordinate,ListofXcor,ListofAttributes):
    x = input("Directional keys are W/S/A/D enter T to pause one turn, Exit to end the Program")
    match x.upper():
        case "W":
            moveup(Size,Ucordinate)
            printmap(ListofXcor, Ucordinate, Size)
            print(f"You are at a {ListofXcor[int(Ucordinate["XCor"])][int(Ucordinate["YCor"])]}")
            movementinterface(Size, Ucordinate,ListofXcor,ListofAttributes)
        case "S":
            movedown(Size,Ucordinate)
            printmap(ListofXcor, Ucordinate, Size)
            print(f"You are at a {ListofXcor[int(Ucordinate["XCor"])][int(Ucordinate["YCor"])]}")
            movementinterface(Size, Ucordinate,ListofXcor,ListofAttributes)
        case "A":
            moveleft(Size,Ucordinate)
            printmap(ListofXcor, Ucordinate, Size)
            print(f"You are at a {ListofXcor[int(Ucordinate["XCor"])][int(Ucordinate["YCor"])]}")
            movementinterface(Size, Ucordinate,ListofXcor,ListofAttributes)
        case "D":
            moveright(Size,Ucordinate)
            printmap(ListofXcor, Ucordinate, Size)
            print(f"You are at a {ListofXcor[int(Ucordinate["XCor"])][int(Ucordinate["YCor"])]}")
            movementinterface(Size, Ucordinate,ListofXcor,ListofAttributes)
        case "T":
            printmap(ListofXcor, Ucordinate, Size)
            print(f"You Rested for one turn at a {ListofXcor[int(Ucordinate["XCor"])][int(Ucordinate["YCor"])]}")
            movementinterface(Size,Ucordinate,ListofXcor,ListofAttributes)
        case "EXIT":
            print("Bye~")
        case _:
            print("Not a valid input, try again")
            movementinterface(Size,Ucordinate,ListofXcor,ListofAttributes)

def Alterlocation(Size,ListofXcor,ListofAttributes,XCor,YCor,NewTerrainType):
    if XCor > Size["XCor"] or XCor < 0:
        print("X Coordinate has to within the confines of the map ")
    else:
        if YCor > Size["YCor"] or YCor < 0:
            print("Y Coordinate has to within the confines of the map ")
        else:
            print(f"Tile at X: {XCor}, Y: {YCor} has been changed from {ListofXcor[XCor][YCor]} to {NewTerrainType}")
            ListofXcor[XCor][YCor] = NewTerrainType
            i = 0
            while i < len(ListofXcor):
                print(str(ListofXcor[i]).replace("[","").replace("]","").replace(" ","").replace(",","").replace("'",""))
                i += 1

def Lookat(Size,ListofXcor,ListofAttributes,XCor,YCor):
    if XCor > Size["XCor"] or XCor < 0:
        print("X Coordinate to look at has to within the confines of the map ")
    else:
        if YCor > Size["YCor"] or YCor < 0:
            print("Y Coordinate to look at has to within the confines of the map ")
        else:
            return ListofXcor[XCor][YCor]



resetmap(ListofXcor, ListofAttributes, Ucordinate,9,9, Size)
printmap(ListofXcor, Ucordinate, Size)
Alterlocation(Size,ListofXcor,ListofAttributes,4,5,"A")
Alterlocation(Size,ListofXcor,ListofAttributes,4,2,"T")
print(f" You see {Lookat(Size,ListofXcor,ListofAttributes,4,5)} at X:4 Y:5")
# print(Ucordinate)
# changeuserCor(Size,Ucordinate,3,7)
# printmap(ListofXcor,Ucordinate, Size)
# print(Ucordinate)
# changeuserCor(Size,Ucordinate,4,9)
# printmap(ListofXcor,Ucordinate, Size)
# print(Ucordinate)
# k = 0
# while k < Size["XCor"]-1:
#     print(f"{ListofXcor[k]}\n")
#     k += 1
# print(Ucordinate)
movementinterface(Size,Ucordinate,ListofXcor,ListofAttributes)