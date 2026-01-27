ListofXcor = []
ListofAttributes = []
Ucordinate = {"XCor":0 , "YCor":0}
Size = {"XCor":0 , "YCor":0}

def resetmap(ListofXcor, ListofAttributes,Ucordinate,XCor,YCor,Size):
    ListofXcor.clear()
    Size.update({"XCor":XCor, "YCor":YCor})
    i = 0
    while i < XCor-1:
        ListofXcor.append(["_"])
        #ListofAttributes.append(["0"])
        j = 0
        while j < YCor-1:
            ListofXcor[i].append("_")
            # ListofAttributes[j].append("0")
            j += 1
        i +=1
    Ucordinate.update({"XCor":round((XCor-1)/2, 0), "YCor":round((YCor-1)/2, 0)})

def printmap(ListofXcor, Ucordinate, Size):
    Mapwithuser = ListofXcor.copy()
    i = 0
    x = int(Ucordinate["XCor"])
    y = int(Ucordinate["YCor"])
    a = Mapwithuser[x]
    a[y] = "X"
    while i < Size["XCor"]-1:
        b = str(Mapwithuser[i]).replace("[","").replace("]","").replace(" ","").replace(",","").replace("'","")
        print(f"{b}\n")
        i += 1
    Mapwithuser.clear()


def changeuserCor(Size,Ucordinate,NewXCor,NewYCor):
    try:
        if int(NewXCor) < Size["XCor"] and int(NewYCor) < Size["YCor"]:
            Ucordinate.update({"XCor":NewXCor, "YCor":NewYCor})
            print(f"User has been moved to X:{NewXCor}, Y:{NewYCor}")
        else:
            print(f"Cant move User to X:{NewXCor}, Y:{NewYCor} because its outside the map")
    except:
        print("An Error has Occurred target coordinates must be Integers")

# def moveleft(Size,Ucordinate):
#     if Ucordinate["XCor"] == 0:
#         print("Cant move Left")
#     else:
#         a = Ucordinate["XCor"]
#         Ucordinate.update({"XCor": a-1})
#
# def moveright(Size,Ucordinate):
#     if Ucordinate["XCor"] == Size["XCor"]:
#         print("Cant move Right")
#     else:
#         a = Ucordinate["XCor"]
#         Ucordinate.update({"XCor" : a+1 })
#
#
# def moveup(Size,Ucordinate):
#     if Ucordinate["YCor"] == 0:
#         print("Cant move Up")
#     else:
#         a = Ucordinate["YCor"]
#         Ucordinate.update({"YCor" : int(a+1)})
#
# def movedown(Size,Ucordinate):
#     if Ucordinate["YCor"] == Size["YCor"]:
#         print("Cant move Down")
#     else:
#         a = Ucordinate["YCor"]
#         Ucordinate.update({"YCor": int(a-1)})
#
# def movementinterface(Size,Ucordinate):
#     x = input("Directional keys are W/S/A/D enter T to pause one turn")
#     match x.upper():
#         case "W":
#             moveup(Size,Ucordinate)
#             printmap(ListofXcor, Ucordinate, Size)
#             movementinterface(Size, Ucordinate)
#         case "S":
#             movedown(Size,Ucordinate)
#             printmap(ListofXcor, Ucordinate, Size)
#             movementinterface(Size, Ucordinate)
#         case "A":
#             moveleft(Size,Ucordinate)
#             printmap(ListofXcor, Ucordinate, Size)
#             movementinterface(Size, Ucordinate)
#         case "D":
#             moveright(Size,Ucordinate)
#             printmap(ListofXcor, Ucordinate, Size)
#             print(Ucordinate)
#             movementinterface(Size, Ucordinate)
#         case "T":
#             printmap(ListofXcor, Ucordinate, Size)
#             print("You Rested for one turn")
#             movementinterface(Size,Ucordinate)
#         case _:
#             print("Not a valid input, try again")
#             movementinterface(Size,Ucordinate)




resetmap(ListofXcor, ListofAttributes, Ucordinate,11,22, Size)
changeuserCor(Size,Ucordinate,3,17)
printmap(ListofXcor,Ucordinate, Size)
changeuserCor(Size,Ucordinate,4,9)
printmap(ListofXcor,Ucordinate, Size)
k = 0
while k < Size["XCor"]-1:
    print(f"{ListofXcor[k]}\n")
    k += 1
print(Ucordinate)
# movementinterface(Size,Ucordinate)