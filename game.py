#Vernon Loh Jin Feng - IM02 - S10270739K
from random import randint
#------------------------Functions------------------------
def DisplayMainMenu():
    print("---------------- Welcome to Sundrop Caves! ----------------")
    print("You spent all your money to get the deed to a mine, a small")
    print("  backpack, a simple pickaxe and a magical portal stone.")
    print("")
    print("How quickly can you get the 500 GP you need to retire")
    print("  and live happily ever after?")
    print("-----------------------------------------------------------\n")
    print("--- Main Menu ----\n(N)ew game\n(L)oad saved game\n(Q)uit\n------------------")

def DisplayTownMenu():
    print(f"DAY {playerStats['Day']}\n----- Sundrop Town -----\n(B)uy stuff\nSee Player (I)nformation\nSee Mine (M)ap\n(E)nter mine\nSa(V)e game\n(Q)uit to main menu\n------------------------")

def SaveData():
    return

def LoadData():
    return

def DisplayShopMenu():
    print("\n----------------------- Shop Menu -------------------------")
    if playerStats["pickaxe"] != 3:
        print(f"(P)ickaxe upgrade to Level {playerStats['pickaxe'] + 1} to mine {pickaxeDetails[playerStats["pickaxe"] + 1][1]} ore for {pickaxeDetails[playerStats["pickaxe"] + 1][0]} GP")
    print(f"(B)ackpack upgrade to carry {playerStats['backpack'] + 2} items for {playerStats['backpack'] * 2} GP")
    print("(L)eave shop")
    print("-----------------------------------------------------------")
    print(f"GP:{playerStats["GP"]}")
    print("-----------------------------------------------------------")
    return

def UpgradePickaxe():
    playerStats["pickaxe"] += 1
    playerStats["GP"] -= pickaxeDetails[playerStats["pickaxe"]][0]
    print(f"Congratulations! You can now mine {pickaxeDetails[playerStats["pickaxe"]][1]}!\n")

def UpgradeBackpack():
    playerStats["GP"] -= playerStats["backpack"] * 2
    playerStats["backpack"] += 2
    print(f"Congratulations! You can now carry {playerStats['backpack']} items!\n")

def DisplayPlayerInformation():
    print("\n----- Player Information -----")
    print(f"Name: {playerStats['name']}")
    #To be added
    print(f"Portal position: ({playerStats['portal']})")
    print(f"Pickaxe level: {playerStats['pickaxe']} ({pickaxeDetails[playerStats["pickaxe"]][1]})")
    print("------------------------------")
    print(f"Load: {playerStats["load"]} / {playerStats["backpack"]}")
    print("------------------------------")
    print(f"GP: {playerStats["GP"]}")
    print(f"Steps taken: {playerStats["steps"]}")
    print("------------------------------\n")
    return

def DisplayMap():
    coordinates = [0, 0]
    for row in fogMap:
        print("|", end="")
        for col in row:
            if coordinates == playerLocation:
                print("M", end="")
            elif playerStats["portal"] == coordinates:
                print("P", end="")
            else:
                print(col, end="")
            
            coordinates[0] += 1
        print("", end="|\n")
        coordinates[1] += 1
        coordinates[0] = 0

def DisplayMineMenu():
    return

def Move(movementInput):
    return

def UsePortalStone():
    return

def SellOres(playerStats):
    for i in range(playerStats["minerals"]["C"]):
        playerStats["GP"] += randint(1, 3)
    playerStats["minerals"]["C"] = 0

    for i in range(playerStats["minerals"]["S"]):
        playerStats["GP"] += randint(5, 8)
    playerStats["minerals"]["S"] = 0

    for i in range(playerStats["minerals"]["G"]):
        playerStats["GP"] += randint(10, 18)
    playerStats["minerals"]["G"] = 0

def saveMap():
    while True:
        colCount = 0
        fogRow = []
        row = []
        line = dataFile.readline()
        if line.strip() == "":
            break
        for letter in line:
            if colCount == 30:
                break
            if letter == "\n":
                letter = " "
            fogRow.append("?")
            row.append(letter)
            colCount += 1
        map.append(row)
        fogMap.append(fogRow)
    
def clearFog():
    clearCoordinates = {"U": [playerLocation[0], playerLocation[1]-1], 
                        "B": [playerLocation[0], playerLocation[1]+1], 
                        "UR": [playerLocation[0]+1, playerLocation[1]-1], 
                        "UL": [playerLocation[0]-1, playerLocation[1]-1], 
                        "BR": [playerLocation[0] + 1, playerLocation[1]+1], 
                        "BL": [playerLocation[0] - 1, playerLocation[1]+1], 
                        "L": [playerLocation[0] - 1, playerLocation[1]], 
                        "R": [playerLocation[0] + 1, playerLocation[1]]}

    #Dont need clear since on the end! (No fog!)
    if playerLocation[0] == 0:
        clearCoordinates["UL"] = playerLocation
        clearCoordinates["BL"] = playerLocation
        clearCoordinates["L"] = playerLocation
    elif playerLocation[0] == 29:
        clearCoordinates["UR"] = playerLocation
        clearCoordinates["BR"] = playerLocation
        clearCoordinates["R"] = playerLocation
    elif playerLocation[1] == 0:
        clearCoordinates["UL"] = playerLocation
        clearCoordinates["UR"] = playerLocation
        clearCoordinates["U"] = playerLocation
    elif playerLocation[1] == 9:
        clearCoordinates["BR"] = playerLocation
        clearCoordinates["BL"] = playerLocation
        clearCoordinates["B"] = playerLocation
    
    for fogs in clearCoordinates.values():
        fogMap[fogs[1]][fogs[0]] = map[fogs[1]][fogs[0]]


#------------------------Variables------------------------
dataFile = open("level1.txt", "r")

pickaxeDetails = {1: [0, "copper"], 2: [50, "silver"], 3: [150, "gold"]}
playerLocation = [10, 5]
playerChoice = ""
playerStats = {"name": "", "Day": 1, "GP": 0, "backpack": 10, 
                       "steps": 0, "load": 0, "minerals": {"C": 0, "S": 0, "G": 0}, "pickaxe": 1, "portal": [-1, -1]}

map = []
fogMap = []
#------------------------Game Program------------------------
saveMap()
clearFog()
DisplayMap()

while True:
    DisplayMainMenu()

    playerChoice = input("Your Choice? ")

    if playerChoice == "q" or playerChoice == "Q":
        #Exit out program
        break
    elif playerChoice == "L" or playerChoice == "l":
        LoadData()
    elif playerChoice == "N" or playerChoice == "n":
        #Refresh Player's Stats (New Account)
        playerStats = {"name": "", "Day": 1, "GP": 50, "backpack": 10, 
                       "steps": 0, "load": 0, "minerals": {"C": 0, "S": 0, "G": 0}, "pickaxe": 1, "portal": [-1, -1]}
        playerStats["name"] = input("Greetings, miner! What is your name? ")
        print(f"Pleased to meet you, {playerStats["name"]}. Welcome to Sundrop Town!\n")
    else:
        print("Inavalid Input, please re-enter your choice\n")
        continue
    
    while True:
        #------------------------Town Menu------------------------
        SellOres(playerStats)

        DisplayTownMenu()
        playerChoice = input("Your Choice? ")

        if playerChoice == "q" or playerChoice == "Q":
            #Back to main menu
            break
        elif playerChoice == "B" or playerChoice == "b":

            #------------------------Shop Menu------------------------
            while True:
                DisplayShopMenu()
                playerChoice = input("Your Choice? ")

                if (playerChoice == "p" or playerChoice == "P") and (playerStats["pickaxe"] != 3 and playerStats["GP"] >= pickaxeDetails[playerStats["pickaxe"] + 1][0]):
                    UpgradePickaxe()
                elif (playerChoice == "B" or playerChoice == "b") and (playerStats["GP"] > playerStats['backpack'] * 2):
                    UpgradeBackpack()
                elif playerChoice == "L" or playerChoice == "l":
                    print()
                    break
                else:
                    print("Invalid input or Not enough GP!\n")

        elif playerChoice == "I" or playerChoice == "i":
            DisplayPlayerInformation()
        elif playerChoice == "V" or playerChoice == "v":
            #TBA
            SaveData()
        elif playerChoice == "E" or playerChoice == "e":
            DisplayMineMenu()
        elif playerChoice == "M" or playerChoice == "m":
            DisplayMap()
        else:
            print("Inavalid Input, please re-enter your choice")
