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
    #Print out the UI for the Town Menu
    print(f"DAY {playerStats['Day']}\n----- Sundrop Town -----\n(B)uy stuff\nSee Player (I)nformation\nSee Mine (M)ap\n(E)nter mine\nSa(V)e game\n(S)ell Ores\n(Q)uit to main menu\n------------------------")

def SaveData():
    #My save mechanic allows for multiple save files
    global currentSaveFile
    
    #Opens current/new save file for writing
    dataFile = open(saveFileName+str(currentSaveFile)+".txt", "w")

    #Append days first (Needed to print when loading so user can differentiate between savefiles) to local save which allows program to determine current save file when ran and each savefile days
    saveFileDays.append(playerStats["Day"])
    #Writes all of player's data to the txt file.
    for stat in playerStats.keys():
        dataFile.write(f"{stat}, {playerStats[stat]}\n")
    dataFile.write(f"map, {fogMap}\n")
    dataFile.write(f"location, {playerLocation}\n")

def LoadData(fileNumber):
    #Opens chosen save file for reading
    dataFile = open(saveFileName+str(fileNumber)+".txt", "r")
    
    global fogMap
    global playerLocation

    while True:
        #collects each variable as a list containing stat name and its value
        variable = dataFile.readline().strip().split(", ", 1)
        #Determines if its end of txt file 
        if variable == [""]:
            break
        
        #Uses eval() for special variables like int, list and dictionary to convert instead of saving as a string
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
            #Saves as string
            playerStats[variable[0]] = variable[1]

def DisplayShopMenu():
    #Print out the UI for the Menu
    print("\n----------------------- Shop Menu -------------------------")
    #Prevents Pickaxe display if pickaxe is alr maxed level and cannot be upgraded further
    if playerStats["pickaxe"] != 3:
        print(f"(P)ickaxe upgrade to Level {playerStats['pickaxe'] + 1} to mine {pickaxeDetails[playerStats["pickaxe"] + 1][1]} ore for {pickaxeDetails[playerStats["pickaxe"] + 1][0]} GP")
    #Same as pickaxe, prevents further upgrades that doesnt exist
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
    #Prints player info, satisfies requirements for printing in both mine and town menu
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

    #Since save map saves map with the walls "#" for easier minimap printing, we need to use a counter to skip first 2 rows and columns which only contains walls "#"
    skipCount = 0
    #To keep track of coords to print player "M" or portal "P" instead
    coordinates = [2, 2]
    for row in fogMap:
        #Skips "#"
        if skipCount < 2:
            skipCount += 1
            continue

        #if map is bigger than the width (Prevents printing of bottom walls)
        if coordinates[1] >= mapWidth + 2:
            break
        print("|", end="")
        skipCount = 0


        for col in row:
            #Skips "#"
            if skipCount < 2:
                skipCount += 1
                continue

            #if map is bigger than the width (Prevents printing of side walls)
            if coordinates[0] >= mapLength + 2:
                break
            #Check if player is on the coordinates to print "M" instead
            if coordinates == playerLocation:
                print("M", end="")
            #Check if player's portal is on the coordinates to print "P" instead
            elif playerStats["portal"] == coordinates:
                print("P", end="")
            else:
                #Prints map element
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
    #Prints minemenu
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

    #Uses a temp next location to check the location before moving and i learnt that if i dont use .copy() my playerlocation changes with the temp variable
    nextLocation = playerLocation.copy()

    #Input checking
    if playerChoice == "":
        print("Invalid Input, please re-enter")
        return False
    
    #Collects coordinates for next location
    for i in range(len(playerLocation)):
        nextLocation[i] += movements[playerChoice.lower()][i]
    
    #Checks for walls
    if map[nextLocation[1]][nextLocation[0]] == "#":
        print("Theres a wall, so you can't go that way.")
        return False

    #Checks for town to go back without stone
    if map[nextLocation[1]][nextLocation[0]] == "T":
        playerStats["Day"] += 1
        print("Going Back to Town")
        return "town"
                    
def Move(movementInput):
    global nextLocation
    global movements
    global playerLocation
    global map
    global fogMap

    #Check for backpack space if not empty
    if map[nextLocation[1]][nextLocation[0]] != " ":
        if playerStats["load"] == playerStats["backpack"]:
            print("You can't carry any more, so you can't go that way.")  
        elif playerStats["pickaxe"] < oreDescription[map[nextLocation[1]][nextLocation[0]]][4]:
            print("Your pickaxe level is too low, so you can't go that way to mine the ore.") 
        else:
            #mine ore
            MineOre(map[nextLocation[1]][nextLocation[0]])
            #Moves player
            playerLocation = nextLocation
    else:
        #Moves player
        playerLocation = nextLocation
    
    #Mines if theres an ore
    map[playerLocation[1]][playerLocation[0]] = " "
    ClearFog(playerStats["Torch"])

def MineOre(ore):
    global playerStats
    global oreDescription

    #Random ore number which collects the range for randint from ore description
    nodeOresNo = randint(oreDescription[ore][0], oreDescription[ore][1])

    #Check if player back cant hold all the ores mined
    if playerStats["backpack"] - playerStats["load"] < nodeOresNo:
        print(f"You mined {nodeOresNo} piece(s) of {ore}.")
        print(f"...but you can only carry {playerStats["backpack"] - playerStats["load"]} more piece(s)!")
    
    #Adds ore based on player back pack (min ensure that if player backpack no space (AKA smaller) will add that instead or if ore amount is lesser)
    playerStats["minerals"][ore] += min(nodeOresNo, (playerStats["backpack"] - playerStats["load"]))
    playerStats["load"] += min(nodeOresNo, (playerStats["backpack"] - playerStats["load"]))

def UsePortalStone():
    global playerTurns

    #Places portal on location
    playerStats["portal"] = playerLocation
    #Increases day
    playerStats["Day"] += 1
    #resets turns
    playerTurns = 20

#Sell ore based on ore types and count
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
    #Map for replacements with fogmap, changes because if player mines ore and it doesnt change, the fogmap will have ore again based on my clear fog logic
    global map
    #Player's map
    global fogMap
    #For node replacements which should not change
    global replenishMapCopy
    
    #opens map
    dataFile = open("level1.txt","r")

    fogRow = []
    row = []

    #Resets map
    map, fogMap = [], []

    #Adds the map walls "#"
    for i in range(mapLength + 4):
        row.append("#")
    map.extend([row, row])
    fogMap.extend([row, row])
    replenishMapCopy.extend([row, row])

    fogMap = map.copy()
    while True:
        fogRow = []
        row = []
        #Count the amount of element per row, since cant use .strip(), there will be extra spaces which may not be part of the map
        colCount = 0

        #Adds the map walls "#"
        row.extend(["#", "#"])
        fogRow = row.copy()
        
        #Read each line in datafile
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

        #Adds the map walls "#"
        row.extend(["#", "#"])
        fogRow.extend(["#", "#"])
        #Add the row to map
        map.append(row)
        replenishMapCopy.append(row)
        #Same here
        fogMap.append(fogRow)

    #Adds the map walls "#"
    row = []
    for i in range(mapLength + 4):
        row.append("#")
    map.extend([row, row])
    fogMap.extend([row, row])
    replenishMapCopy.extend([row, row])
    
    row = []

def ClearFog(torchlevel):
    global fogMap
    global map

    #Collects the Start and End value to replace "?" with true map value (if else for torch level)
    if torchlevel == 2:
        xDisplay = [playerLocation[0] - 2, playerLocation[0] + 2]
        yDisplay = [playerLocation[1] - 2, playerLocation[1] + 2]
    else:
        xDisplay = [playerLocation[0] - 1, playerLocation[0] + 1]
        yDisplay = [playerLocation[1] - 1, playerLocation[1] + 1]

    #Replaces each value with to clear fog
    for i in range(yDisplay[0], yDisplay[1]+1):
        for f in range(xDisplay[0], xDisplay[1]+1):
            fogMap[i][f] = map[i][f]
    
def DisplayMiniMap(torchlevel):
    #Collects the Start and End value to print for minimap(if else for torch level)
    if torchlevel == 2:
        xDisplay = [playerLocation[0] - 2, playerLocation[0] + 2]
        yDisplay = [playerLocation[1] - 2, playerLocation[1] + 2]
    else:
        xDisplay = [playerLocation[0] - 1, playerLocation[0] + 1]
        yDisplay = [playerLocation[1] - 1, playerLocation[1] + 1]

    #Border
    print(f"+{(xDisplay[1] - xDisplay[0] + 1) * "-"}+")
    for i in range(yDisplay[0], yDisplay[1]+1):
        print("|", end="")
        #prints mini map
        for f in range(xDisplay[0], xDisplay[1]+1):
            #place player in middle
            if[f, i] == playerLocation:
                print("M", end="")
                continue
            #If got portal with 3x3 or 5x5
            if[f, i] == playerStats["portal"]:
                print("P", end="")
                continue
            else:
                print(fogMap[i][f], end="")
        print("|", end="\n")
    #Border
    print(f"+{(xDisplay[1] - xDisplay[0] + 1) * "-"}+\n")

#Holds the number of save files and leaderboard
def LoadLocalSave():
    global leaderboard
    global currentSaveFile
    global saveFileDays
    dataFile = open("LocalSaveData.txt", "r")

    #Saves the stat "Days" in each save file for better identification by user to decide which save file to load
    saveFileDays = []
    #Each top player on leaderboard
    leaderboard = []

    while True:
        line = dataFile.readline().strip().split(", ")

        #Check if end
        if line == [""]:
            break
        #Check if it holds the currentSaveFile number
        elif line[0] == "FileNo":
            currentSaveFile = int(line[1])
        #Check if it holds the no of days for the specific save files
        elif "FileDay" in line[0]:
            saveFileDays.append(int(line[1]))
        else:
            #Appends each leaderboard player to leaderboard
            line[3] = line[3].replace(",", "")
            leaderboard.append(line)
    
    #Prepares for next save file (Required to check since 1st savefile will have 0 element in savefiledays so if keep adding, will become 2 and 0 which become out of index)
    if currentSaveFile == len(saveFileDays):
        currentSaveFile += 1

def SaveLocalSave():
    global leaderboard
    dataFile = open("LocalSaveData.txt", "w")

    #Writes current save file (Prevents overwriting when program reopened and saving happens)
    dataFile.write(f"FileNo, {currentSaveFile}\n")
    #Saves rest of data
    for i in range(len(saveFileDays)):
        dataFile.write(f"FileDay{i + 1}, {saveFileDays[i]}\n")
    for player in leaderboard:
        for stat in player:
            dataFile.write(str(stat) + ", ")
        dataFile.write("\n")
    
def replenishNodes():
    global fogMap
    global replenishMapCopy

    coordinates = [0, 0]
    for row in fogMap:
        coordinates[0] = 0
        for col in row:
            if col == " ":
                #20% mechanic
                random = randint(1, 5)
                #Replaces the empty field with the true field in replenishmapcopy
                if random == 1:
                    fogMap[coordinates[1]][coordinates[0]] = replenishMapCopy[coordinates[1]][coordinates[0]]      
            coordinates[0] += 1
        coordinates[1] += 1


#------------------------Variables------------------------
#Local saves variables
saveFileName = "saveFile"
currentSaveFile = 1
saveFileDays = []
leaderboard = []
integerStats = ["Day", "GP", "backpack", "steps", "load", "pickaxe", "Torch"]

#Game Item Stats
#Pickaxe details index 1 is price and 2 is unlocked ore
pickaxeDetails = {1: [0, "copper"], 2: [50, "silver"], 3: [150, "gold"]}
#Ore description and list is made as [Mining minimum, mining maximum, selling minimum, selling maximum, pickaxe need, level]
oreDescription = {"C": [1, 5, 1, 3, 1, "Copper"], "S": [1, 3, 5, 8, 2, "Silver"], "G": [1, 2, 10, 18, 3, "Gold"]}
orePrices = [0, 0, 0]
nodePieces = 0

#Player Stats
#track player location for everything (Map location etc)
playerLocation = [2, 2]
nextLocation = [2, 2]
#Save choice for all interactions for easy if else statements
playerChoice = ""
playerTurns = 20
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


#Input variables
#Easy access to access movement without the need of to many if-else
playerMovementKeys = "WwSsAaDd"
movements = {"w": [0, -1],  "s": [0, 1], "a": [-1, 0], "d":[1, 0] }
#Prevent misuse of nodereplenish and ore prices
daycheck = 0

#Map layout for true map and fog
map = []
replenishMapCopy = []
fogMap = []
mapWidth = 10
mapLength = 30
#------------------------Game Program------------------------
#Creates map which fogmap will be override if player has save data
saveMap()
#Loads savenumber and leaderboard
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
            playerChoice = input("Enter the file save to load or q to quit: ")
            if playerChoice.isdigit() == True:
                LoadData(playerChoice)
                break
            elif playerChoice == "q" or playerChoice == "Q":
                break
            else:
                print("Invalid input, re-enter your choice")
                continue
    elif playerChoice == "N" or playerChoice == "n":
        #Refresh Player's Stats (New Account)
        playerStats = {"name": "", 
               "Day": 1, 
               "GP": 400, 
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
    elif playerChoice == "v" or playerChoice == "V":
        if leaderboard == []:
            print("No one has completed the game!!\n")
            continue
        else:
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
        if playerStats["load"] > 0:
            playerStats["load"] = 0
            print("Ores has been moved to warehouse, check to sell")
        replenishCheck = 0
        if replenishCheck < playerStats["Day"]:
            replenishCheck = playerStats["Day"]
            replenishNodes()
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
                    flag = CheckArea(playerChoice)
                    if flag == False:
                        continue
                    elif flag == "town":
                        break
                    else:
                        Move(playerChoice)
                else:
                    print("Invalid Input, please re-enter again")
        elif playerChoice == "M" or playerChoice == "m":
            DisplayMap()
            continue
        elif playerChoice == "s" or playerChoice == "S":
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
                if playerChoice == "c" or playerChoice == "c":
                    playerChoice = input("How many pieces (Type a number or all)? ")
                    if playerChoice.lower() == "all":
                        playerChoice = playerStats["minerals"]["C"]
                    else:
                        if playerStats["minerals"]["C"] < int(playerChoice):
                            print("Insufficient Ores please try again")
                            continue
                    SellOres("C", int(playerChoice))
                elif playerChoice == "s" or playerChoice == "S":
                    playerChoice = input("How many pieces(Type a number or all)? ")
                    if playerChoice.lower() == "all":
                        playerChoice = playerStats["minerals"]["S"]
                    else:
                        if playerStats["minerals"]["S"] < int(playerChoice):
                            print("Insufficient Ores please try again")
                        continue
                    SellOres("S", int(playerChoice))
                elif playerChoice == "g" or playerChoice == "G":
                    playerChoice = input("How many pieces(Type a number or all)? ")
                    if playerChoice.lower() == "all":
                        playerChoice = playerStats["minerals"]["G"]
                    else:
                        if playerStats["minerals"]["G"] < int(playerChoice):
                            print("Insufficient Ores please try again")
                        continue
                    SellOres("G", int(playerChoice))
                elif playerChoice == "l" or playerChoice == "L":
                    break
                else:
                    print("Invalid input, please re-enter")
                    continue
        else:
            print("Invalid Input, please re-enter your choice")

        if playerChoice == "Q" or playerChoice == "q":
            #To mainmenu in event of leaving during mining
            break