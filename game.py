#Vernon Loh Jin Feng - IM02 - S10270739K
from random import randint
#------------------------Functions------------------------
def DisplayMainMenu():
    #Print out the UI for the Menu
    print("---------------- Welcome to Sundrop Caves! ----------------")
    print("You spent all your money to get the deed to a mine, a small")
    print("  backpack, a simple pickaxe and a magical portal stone.")
    print("")
    print("How quickly can you get the 500 GP you need to retire")
    print("  and live happily ever after?")
    print("-----------------------------------------------------------\n")
    print("--- Main Menu ----\n(N)ew game\n(L)oad saved game\n(V)iew LeaderBoard\n(Q)uit\n------------------")

def DisplayTownMenu():
    print(f"DAY {playerStats['Day']}\n----- Sundrop Town -----\n(B)uy stuff\nSee Player (I)nformation\nSee Mine (M)ap\n(E)nter mine\nSa(V)e game\n(S)ell Ores\n(Q)uit to main menu\n------------------------")

def SaveData():
    global currentSaveFile
    
    dataFile = open(saveFileName+str(currentSaveFile)+".txt", "w")

    saveFileDays.append(playerStats["Day"])
    for stat in playerStats.keys():
        dataFile.write(f"{stat}, {playerStats[stat]}\n")

    dataFile.write(f"map, {fogMap}\n")
    dataFile.write(f"location, {playerLocation}\n")

def LoadData(fileNumber):
    dataFile = open(saveFileName+str(fileNumber)+".txt", "r")
    
    global fogMap
    global playerLocation

    while True:
        variable = dataFile.readline().strip().split(", ", 1)
        if variable == [""]:
            break
        
        if variable[0] == "location":
            playerLocation = eval(variable[1])
        elif variable[0] in integerStats:
            playerStats[variable[0]] = eval(variable[1])
        elif variable[0] == "map":
            fogMap = eval(variable[1])
        elif variable[0] == "portal":
            playerStats[variable[0]] = eval(variable[1])
        elif variable[0] == "minerals":
            playerStats[variable[0]] = eval(variable[1])
        else:
            playerStats[variable[0]] = variable[1]

def DisplayShopMenu():
    #Print out the UI for the Menu
    print("\n----------------------- Shop Menu -------------------------")
    #Prevents Pickaxe display if pickaxe is alr maxed level and cannot be upgraded further
    if playerStats["pickaxe"] != 3:
        print(f"(P)ickaxe upgrade to Level {playerStats['pickaxe'] + 1} to mine {pickaxeDetails[playerStats["pickaxe"] + 1][1]} ore for {pickaxeDetails[playerStats["pickaxe"] + 1][0]} GP")
    if playerStats["Torch"] != 2:  
        print("(T)orch upgrade to level 2 to have 5x5 view port for 50 GP")  
    print(f"(B)ackpack upgrade to carry {playerStats['backpack'] + 2} items for {playerStats['backpack'] * 2} GP")
    print("(L)eave shop")
    print("-----------------------------------------------------------")
    print(f"GP:{playerStats["GP"]}")
    print("-----------------------------------------------------------")

def UpgradePickaxe():
    #Increase pickaxe Level
    playerStats["pickaxe"] += 1
    
    #Reduce GP for pickaxe upgrade costs
    playerStats["GP"] -= pickaxeDetails[playerStats["pickaxe"]][0]

    #Output Message
    print(f"Congratulations! You can now mine {pickaxeDetails[playerStats["pickaxe"]][1]}!\n")

def UpgradeBackpack():
    #Reduce GP first since cost of backpack is based on backpack size and when upgraded will incur additional costs to user
    playerStats["GP"] -= playerStats["backpack"] * 2

    #Increase pickaxe Level
    playerStats["backpack"] += 2

    #Output Message
    print(f"Congratulations! You can now carry {playerStats['backpack']} items!\n")

#Displays relevant information from the playerstats dictionary
def DisplayPlayerInformation():
    print("\n----- Player Information -----")
    print(f"Name: {playerStats['name']}")
    print(f"Current position: {playerLocation}")
    print(f"Pickaxe level: {playerStats['pickaxe']} ({pickaxeDetails[playerStats["pickaxe"]][1]})")
    print(f"Gold: {playerStats['minerals']["G"]}")
    print(f"Silver: {playerStats['minerals']["S"]}")
    print(f"Copper: {playerStats['minerals']["C"]}")
    print(f"Portal position: ({playerStats['portal']})")
    print("------------------------------")
    print(f"Load: {playerStats["load"]} / {playerStats["backpack"]}")
    print("------------------------------")
    print(f"GP: {playerStats["GP"]}")
    print(f"Steps taken: {playerStats["steps"]}")
    print("------------------------------\n")
    return

def DisplayMap():
    #Map Border
    print("+------------------------------+")

    #Coordinates of current print to check if playerlocation or if portal is there to override the map
    skipCount = 0
    coordinates = [2, 2]
    for row in fogMap:
        if skipCount < 2:
            skipCount += 1
            continue
        if coordinates[1] >= mapWidth:
            break
        print("|", end="")
        skipCount = 0

        for col in row:
            if skipCount < 2:
                skipCount += 1
                continue
            
            if coordinates[0] >= mapLength + 2:
                break
            #Check if player is on the coordinates to print "M" instead
            if coordinates == playerLocation:
                print("M", end="")
            #Check if player's portal is on the coordinates to print "P" instead
            elif playerStats["portal"] == coordinates:
                print("P", end="")
            else:
                print(col, end="")
            
            #Increment to check all coordinates
            coordinates[0] += 1
        print("", end="|\n")
        
        #Increment
        coordinates[1] += 1
        #Reset as it is a new row
        coordinates[0] = 2

    #Map Border
    print("+------------------------------+\n")

def DisplayMineMenu():
    print(f"Day {playerStats['Day']}")
    DisplayMiniMap(playerStats["Torch"])
    print(f"Turns left: {playerTurns} Load: {playerStats['load']} / {playerStats['backpack']} Steps: {playerStats["steps"]}")
    print("(WASD) to move")
    print("(M)ap, (I)nformation, (P)ortal, (Q)uit to main menu")

def CheckArea(movementInput):
    global playerLocation
    global playerStats
    global playerTurns
    global playerChoice
    global nextLocation

    playerStats["steps"] += 1

    playerTurns -= 1

    nextLocation = playerLocation.copy()

    if playerChoice == "":
        print("Invalid Input, please re-enter")
        return False
    
    for i in range(len(playerLocation)):
        nextLocation[i] += movements[playerChoice.lower()][i]
    
    if map[nextLocation[1]][nextLocation[0]] == "#":
        print("Theres a wall, so you can't go that way.")
        return False
                    
def Move(movementInput):
    global nextLocation
    global movements
    global playerLocation
    global map

    if map[nextLocation[1]][nextLocation[0]] != " ":
        if playerStats["load"] == playerStats["backpack"]:
            print("You can't carry any more, so you can't go that way.")  
        elif playerStats["pickaxe"] < oreDescription[map[nextLocation[1]][nextLocation[0]]][4]:
            print("Your pickaxe level is too low, so you can't go that way to mine the ore.") 
        else:
            MineOre(map[nextLocation[1]][nextLocation[0]])
            playerLocation = nextLocation
    else:
        playerLocation = nextLocation
    
    print(map[playerLocation[1]][playerLocation[0]])
    map[playerLocation[1]][playerLocation[0]] = " "
    ClearFog(playerStats["Torch"])

def MineOre(ore):
    global playerStats
    global oreDescription

    nodeOresNo = randint(oreDescription[ore][0], oreDescription[ore][1])

    if playerStats["backpack"] - playerStats["load"] < nodeOresNo:
        print(f"You mined {nodeOresNo} piece(s) of {ore}.")
        print(f"...but you can only carry {playerStats["backpack"] - playerStats["load"]} more piece(s)!")
    
    playerStats["minerals"][ore] += min(nodeOresNo, (playerStats["backpack"] - playerStats["load"]))
    playerStats["load"] += min(nodeOresNo, (playerStats["backpack"] - playerStats["load"]))

def UsePortalStone():
    global playerTurns

    playerStats["portal"] = playerLocation
    playerStats["Day"] += 1
    print(playerTurns)
    playerTurns = 20
    print(playerTurns)

def SellOres(oreType, oreCount):
    global orePrices
    global playerStats

    oreIndexes = {"C": 0, "S": 1, "G": 2}

    print(f"You sold {oreCount} {oreDescription[oreType][5]} ore for {oreCount * orePrices[oreIndexes[oreType]]} GP.")

    playerStats["GP"] += oreCount * orePrices[oreIndexes[oreType]]
    playerStats["minerals"][oreType] -= oreCount
    playerStats["load"] -= oreCount
    print(f"You now have {playerStats["GP"]} GP!")

#Collect Map from .txt file and save in nested lists, where each element is the rows which contains a list of all elements
def saveMap():
    global map
    global fogMap
    
    dataFile = open("level1.txt","r")
    fogRow = []
    row = []

    map, fogMap = [], []
    for i in range(mapLength + 4):
        row.append("#")
    map.extend([row, row])
    fogMap.extend([row, row])

    fogMap = map.copy()
    while True:
        fogRow = []
        row = []
        #Count the amount of element per row, since cant use .strip(), there will be extra spaces which may not be part of the map
        colCount = 0
        #Used for keeping each row for both maps
        row.extend(["#", "#"])

        fogRow = row.copy()
        #Read each line in 
        line = dataFile.readline()
        if line.strip() == "":
            break
        for letter in line:
            #Max amount of element per row since map is 30 col 10 row
            if colCount == mapLength:
                break
            #If there is a glitch and not enough inserted col, \n will be use (First line only had 29 cols while others had 30)
            if letter == "\n":
                letter = " "
            
            #Generate the same size map in fog
            fogRow.append("?")

            #Insert true element into the map
            row.append(letter)
            #Increment
            colCount += 1

        row.extend(["#", "#"])
        fogRow.extend(["#", "#"])
        #Add the row to map
        map.append(row)
        #Same here
        fogMap.append(fogRow)

    row = []
    for i in range(mapLength + 4):
        row.append("#")
    map.extend([row, row])
    fogMap.extend([row, row])
    row = []

    for i in range(mapLength + 4):
        row.append("#")
    map.extend([row, row])
    fogMap.extend([row, row])

def ClearFog(torchlevel):
    global fogMap
    global map


    
    if torchlevel == 2:
        xDisplay = [playerLocation[0] - 2, playerLocation[0] + 2]
        yDisplay = [playerLocation[1] - 2, playerLocation[1] + 2]
    else:
        xDisplay = [playerLocation[0] - 1, playerLocation[0] + 1]
        yDisplay = [playerLocation[1] - 1, playerLocation[1] + 1]

    for i in range(yDisplay[0], yDisplay[1]+1):
        for f in range(xDisplay[0], xDisplay[1]+1):
            fogMap[i][f] = map[i][f]
    
def DisplayMiniMap(torchlevel):
    #Collects the Start and End value to print for minimap
    if torchlevel == 2:
        xDisplay = [playerLocation[0] - 2, playerLocation[0] + 2]
        yDisplay = [playerLocation[1] - 2, playerLocation[1] + 2]
    else:
        xDisplay = [playerLocation[0] - 1, playerLocation[0] + 1]
        yDisplay = [playerLocation[1] - 1, playerLocation[1] + 1]

    #Border
    print(f"+{(xDisplay[1] - xDisplay[0]) * "-"}+")
    for i in range(yDisplay[0], yDisplay[1]+1):
        print("|", end="")
        for f in range(xDisplay[0], xDisplay[1]+1):
            #place player in middle
            if[f, i] == playerLocation:
                print("M", end="")
                continue
            if[f, i] == playerStats["portal"]:
                print("M", end="")
                continue
            else:
                print(fogMap[i][f], end="")
        print("|", end="\n")
    #Border
    print(f"+{(xDisplay[1] - xDisplay[0]) * "-"}+\n")

#Holds the number of save files and leaderboard
def LoadLocalSave():
    global leaderboard
    global currentSaveFile
    global saveFileDays
    dataFile = open("LocalSaveData.txt", "r")

    leaderboard = []
    while True:
        line = dataFile.readline().strip().split(", ")

        if line == [""]:
            break
        elif line[0] == "FileNo":
            currentSaveFile = int(line[1]) + 1
        elif "FileDay" in line[0]:
            saveFileDays.append(int(line[1]))
        else:
            line[3] = line[3].replace(",", "")
            leaderboard.append(line)

def SaveLocalSave():
    global leaderboard
    dataFile = open("LocalSaveData.txt", "w")

    dataFile.write(f"FileNo, {currentSaveFile}\n")
    for i in range(len(saveFileDays)):
        dataFile.write(f"FileDay{i + 1}, {saveFileDays[i]}\n")
    for player in leaderboard:
        for stat in player:
            dataFile.write(str(stat) + ", ")
        dataFile.write("\n")
    

#------------------------Variables------------------------
saveFileName = "saveFile"
currentSaveFile = 1
saveFileDays = []

#Game Item Stats
#Pickaxe details index 1 is price and 2 is unlocked ore
pickaxeDetails = {1: [0, "copper"], 2: [50, "silver"], 3: [150, "gold"]}
oreDescription = {"C": [1, 5, 1, 3, 1, "Copper"], "S": [1, 3, 5, 8, 2, "Silver"], "G": [1, 2, 10, 18, 3, "Gold"]}

#Player Stats
#track player location for everything (Map location etc)
playerLocation = [2, 2]
nextLocation = [2, 2]
#Easy access to access movement without the need of to many if-else
playerMovementKeys = "WwSsAaDd"
movements = {"w": [0, -1],  "s": [0, 1], "a": [-1, 0], "d":[1, 0] }
#Save choice for all interactions for easy if else statements
playerChoice = ""
playerTurns = 20

daycheck = 0

orePrices = [0, 0, 0]

nodePieces = 0

leaderboard = []

integerStats = ["Day", "GP", "backpack", "steps", "load", "pickaxe", "Torch"]
#All of player stats to be accessed
playerStats = {"name": "", 
               "Day": 1, 
               "GP": 500, 
               "backpack": 10, 
               "steps": 0, 
               "load": 0, 
               "minerals": {"C": 0, "S": 0, "G": 0}, 
               "pickaxe": 1, 
               "portal": [-1, -1], 
               "Torch": 1}

#Map layout for true map and fog
map = []
fogMap = []
mapWidth = 10
mapLength = 30
#------------------------Game Program------------------------
#Creates map which fogmap will be override if player has save data
saveMap()
LoadLocalSave()

while True:
    DisplayMainMenu()

    playerChoice = input("Your Choice? ")

    if playerChoice == "q" or playerChoice == "Q":
        #Exit out program
        break
    elif playerChoice == "L" or playerChoice == "l":
        LoadLocalSave()
        for i in range(currentSaveFile - 1):
            print(f"Data File Number {i + 1} --- {saveFileDays[i]} Days progress")
        while True:
            playerChoice = input("Enter the file save to load: ")
            if playerChoice.isdigit() == True:
                break
            else:
                print("Invalid input, re-enter your choice")
                continue

        LoadData(playerChoice)
    elif playerChoice == "N" or playerChoice == "n":
        #Refresh Player's Stats (New Account)
        playerStats = {"name": "", 
               "Day": 1, 
               "GP": 49, 
               "backpack": 10, 
               "steps": 0, 
               "load": 0, 
               "minerals": {"C": 60, "S": 20, "G": 1000}, 
               "pickaxe": 1, 
               "portal": [-1, -1],
               "Torch": 1}
        playerTurns = 20
        playerLocation = [2, 2]

        saveMap()
        #Clears starting fog around player
        ClearFog(playerStats["Torch"])

        #Collects player name to store
        playerStats["name"] = input("Greetings, miner! What is your name? ")
        print(f"Pleased to meet you, {playerStats["name"]}. Welcome to Sundrop Town!\n")
    elif playerChoice.lower() == "v":
        LBposition = 1
        print("Top players are:")
        for player in leaderboard:
            print(f"{LBposition}. {player[0]} - Days taken: {player[1]}, Steps taken: {player[2]}, GP earned: {player[3]}")
            LBposition += 1
        continue
    else:
        #Invalid inputs redirects back to display main menu again
        print("Invalid Input, please re-enter your choice\n")
        continue
    
    while True:
        #------------------------Town Menu------------------------
        if playerStats["GP"] >= 500:
            print(f"Woo-hoo! Well done, {playerStats['name']}, you have {playerStats['GP']} GP!")
            print("You now have enough to retire and play video games every day.")
            print(f"And it only took you {playerStats['Day']} days and {playerStats["steps"]} steps! You win!")

            position = 0
            print(leaderboard)
            if leaderboard == []:
                leaderboard.append([playerStats["name"], playerStats["Day"], playerStats["steps"], playerStats["GP"]])
            else:
                for player in leaderboard:
                    if int(player[1]) > playerStats["Day"]:
                        leaderboard.insert(position, [playerStats["name"], playerStats["Day"], playerStats["steps"], playerStats["GP"]])
                        if len(leaderboard) > 5:
                            leaderboard.pop(-1)
                            break
                    elif int(player[1]) == playerStats["Day"]:
                        if int(player[2]) > playerStats["steps"]:
                            leaderboard.insert(position, [playerStats["name"], playerStats["Day"], playerStats["steps"], playerStats["GP"]])
                            if len(leaderboard) > 5:
                                leaderboard.pop(-1)
                            break
                        elif int(player[2]) == playerStats["steps"]:
                            if int(player[3]) < playerStats["GP"]:
                                leaderboard.insert(position, [playerStats["name"], playerStats["Day"], playerStats["steps"], playerStats["GP"]])
                                if len(leaderboard) > 5:
                                    leaderboard.pop(-1)
                                break

                    if position + 1 == len(leaderboard) and len(leaderboard) < 5:
                        leaderboard.append([playerStats["name"], playerStats["Day"], playerStats["steps"], playerStats["GP"]])
                        break
                    position += 1
            SaveLocalSave()
            break

        DisplayTownMenu()
        playerChoice = input("Your Choice? ")

        if playerChoice == "q" or playerChoice == "Q":
            #Break out of loop to go back to main menu loop
            break
        elif playerChoice == "B" or playerChoice == "b":

            #------------------------Shop Menu------------------------
            while True:
                DisplayShopMenu()
                playerChoice = input("Your Choice? ")

                #Actions for each option, described in each functions
                if (playerChoice == "p" or playerChoice == "P") and (playerStats["pickaxe"] != 3 and playerStats["GP"] >= pickaxeDetails[playerStats["pickaxe"] + 1][0]):
                    UpgradePickaxe()
                elif (playerChoice == "B" or playerChoice == "b") and (playerStats["GP"] >= playerStats['backpack'] * 2):
                    UpgradeBackpack()
                elif (playerChoice == "T" or playerChoice == "t") and (playerStats["GP"] >= 50 and playerStats["Torch"]!= 2):
                    playerStats["Torch"] += 1
                    playerStats["GP"] -= 50
                elif playerChoice == "L" or playerChoice == "l":
                    #break out of loop to go back to town menu loop
                    print()
                    break
                else:
                    #handle input issues and GP issues
                    print("Invalid input or Not enough GP!\n")
        #Handles action based on inputs using if-else, more info check functions on what they do
        elif playerChoice == "I" or playerChoice == "i":
            DisplayPlayerInformation()
            continue
        elif playerChoice == "V" or playerChoice == "v":
            #TBA
            SaveData()
            SaveLocalSave()
            currentSaveFile += 1
            break
        elif playerChoice == "E" or playerChoice == "e":
            #------------------------Mine Menu------------------------
            print("---------------------------------------------------")
            print(f"{"Day " + str(playerStats['Day']):^50}")
            print("---------------------------------------------------")

            while True:
                if playerTurns == 0:
                    print("You are exhausted.")
                    print("You place your portal stone here and zap back to town.")
                    UsePortalStone()
                    break

                DisplayMineMenu()

                playerChoice = input("Action? ")

                #Actions for each option, described in each functions
                if playerChoice == "M" or playerChoice == "m":
                    print()
                    DisplayMap()
                elif playerChoice == "I" or playerChoice == "i":
                    print()
                    DisplayPlayerInformation()
                elif playerChoice == "P" or playerChoice == "p":
                    UsePortalStone()
                    break
                elif playerChoice == "Q" or playerChoice == "q":
                    #break out of loop to go back to menu loop
                    print()
                    break
                elif playerChoice in playerMovementKeys:
                    print("---------------------------------------------------")
                    if CheckArea(playerChoice) == False:
                        continue
                    else:
                        Move(playerChoice)
                else:
                    print("Invalid Input, please re-enter again")
        elif playerChoice == "M" or playerChoice == "m":
            DisplayMap()
            continue
        elif playerChoice.lower() == "s":
            currentOre = 0
            if daycheck < playerStats["Day"]:
                daycheck = playerStats["Day"]
                for ore in playerStats["minerals"].keys():
                    orePrices[currentOre] = randint(oreDescription[ore][2], oreDescription[ore][3])
                    currentOre += 1

            while True:
                currentOre = 0
                for ore in playerStats["minerals"].keys():
                    print(f"{oreDescription[ore][-1]} is selling for {orePrices[currentOre]} and you have {playerStats["minerals"][ore]} of it, type {ore} to sell")
                    currentOre += 1
                print(f"Leave")
                playerChoice = input("Choice?")

                print(playerChoice)
                if playerChoice.lower() == "c":
                    playerChoice = input("How many pieces (Type a number or all)? ")
                    if playerChoice.lower() == "all":
                        playerChoice = playerStats["minerals"]["C"]
                    else:
                        if playerStats["minerals"]["C"] < int(playerChoice):
                            print("Insufficient Ores please try again")
                        continue
                    SellOres("C", int(playerChoice))
                elif playerChoice.lower() == "s":
                    playerChoice = input("How many pieces(Type a number or all)? ")
                    if playerChoice.lower() == "all":
                        playerChoice = playerStats["minerals"]["S"]
                    else:
                        if playerStats["minerals"]["S"] < int(playerChoice):
                            print("Insufficient Ores please try again")
                        continue
                    SellOres("S", int(playerChoice))
                elif playerChoice.lower() == "g":
                    playerChoice = input("How many pieces(Type a number or all)? ")
                    if playerChoice.lower() == "all":
                        playerChoice = playerStats["minerals"]["G"]
                    else:
                        if playerStats["minerals"]["G"] < int(playerChoice):
                            print("Insufficient Ores please try again")
                        continue
                    SellOres("G", int(playerChoice))
                elif playerChoice.lower() == "l":
                    break
                else:
                    print("Invalid input, please re-enter")
                    continue
        else:
            print("Invalid Input, please re-enter your choice")

        if playerChoice == "Q" or playerChoice == "q":
            #To mainmenu in event of leaving during mining
            break