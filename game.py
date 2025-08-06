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
    print("--- Main Menu ----\n(N)ew game\n(L)oad saved game\n(Q)uit\n------------------")

def DisplayTownMenu():
    print(f"DAY {playerStats['Day']}\n----- Sundrop Town -----\n(B)uy stuff\nSee Player (I)nformation\nSee Mine (M)ap\n(E)nter mine\nSa(V)e game\n(Q)uit to main menu\n------------------------")

def SaveData():
    return

def LoadData():
    return

def DisplayShopMenu():
    #Print out the UI for the Menu
    print("\n----------------------- Shop Menu -------------------------")
    #Prevents Pickaxe display if pickaxe is alr maxed level and cannot be upgraded further
    if playerStats["pickaxe"] != 3:
        print(f"(P)ickaxe upgrade to Level {playerStats['pickaxe'] + 1} to mine {pickaxeDetails[playerStats["pickaxe"] + 1][1]} ore for {pickaxeDetails[playerStats["pickaxe"] + 1][0]} GP")
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
    #Map Border
    print("+------------------------------+")

    #Coordinates of current print to check if playerlocation or if portal is there to override the map
    coordinates = [0, 0]
    for row in fogMap:
        print("|", end="")
        for col in row:
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
        coordinates[0] = 0

    #Map Border
    print("+------------------------------+\n")

def DisplayMineMenu():
    return

def Move(movementInput):
    return

def UsePortalStone():
    return

def SellOres(playerStats):
    #Sells each ore by generating a random price for each ore based on the amount of the ore the player has in his bag
    for i in range(playerStats["minerals"]["C"]):
        playerStats["GP"] += randint(1, 3)
    playerStats["minerals"]["C"] = 0

    #Sells each ore by generating a random price for each ore based on the amount of the ore the player has in his bag
    for i in range(playerStats["minerals"]["S"]):
        playerStats["GP"] += randint(5, 8)
    playerStats["minerals"]["S"] = 0

    #Sells each ore by generating a random price for each ore based on the amount of the ore the player has in his bag
    for i in range(playerStats["minerals"]["G"]):
        playerStats["GP"] += randint(10, 18)
    playerStats["minerals"]["G"] = 0

#Collect Map from .txt file and save in nested lists, where each element is the rows which contains a list of all elements
def saveMap():
    while True:
        #Count the amount of element per row, since cant use .strip(), there will be extra spaces which may not be part of the map
        colCount = 0
        #Used for keeping each row for both maps
        fogRow = []
        row = []

        #Read each line in dataFile
        line = dataFile.readline()
        if line.strip() == "":
            break
        for letter in line:
            #Max amount of element per row since map is 30 col 10 row
            if colCount == 30:
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

        #Add the row to map
        map.append(row)
        #Same here
        fogMap.append(fogRow)
    
def ClearFog():
    #Saves every coordinate to be cleared in the fog (U stands for upper, B for bottom, L for left and R for right)
    clearCoordinates = {"U": [playerLocation[0], playerLocation[1]-1], 
                        "B": [playerLocation[0], playerLocation[1]+1], 
                        "UR": [playerLocation[0]+1, playerLocation[1]-1], 
                        "UL": [playerLocation[0]-1, playerLocation[1]-1], 
                        "BR": [playerLocation[0] + 1, playerLocation[1]+1], 
                        "BL": [playerLocation[0] - 1, playerLocation[1]+1], 
                        "L": [playerLocation[0] - 1, playerLocation[1]], 
                        "R": [playerLocation[0] + 1, playerLocation[1]]}

    #Dont need clear since on the end! (No fog!) so uses player location (Should already be cleared)
    if playerLocation[0] == 0:
        clearCoordinates["UL"] = playerLocation
        clearCoordinates["BL"] = playerLocation
        clearCoordinates["L"] = playerLocation
    if playerLocation[0] == 29:
        clearCoordinates["UR"] = playerLocation
        clearCoordinates["BR"] = playerLocation
        clearCoordinates["R"] = playerLocation
    if playerLocation[1] == 0:
        clearCoordinates["UL"] = playerLocation
        clearCoordinates["UR"] = playerLocation
        clearCoordinates["U"] = playerLocation
    if playerLocation[1] == 9:
        clearCoordinates["BR"] = playerLocation
        clearCoordinates["BL"] = playerLocation
        clearCoordinates["B"] = playerLocation

    #Clear each fog by replacing "?" with true map value
    for fogs in clearCoordinates.values():
        fogMap[fogs[1]][fogs[0]] = map[fogs[1]][fogs[0]]
    
def DisplayMiniMap():
    #Collects the Start and End value to print for minimap
    xDisplay = [playerLocation[0] - 1, playerLocation[0] + 1]
    yDisplay = [playerLocation[1] - 1, playerLocation[1] + 1]

    #Border
    print("+---+")

    #If is at the top --> print 3 # for the top edge and put the starting to 0 (Prevent printing incorrect values , -1 will get value on the end of list)
    if yDisplay[0] < 0:
        yDisplay[0] = 0
        print("|###|")

    if yDisplay[1] > 9:
        yDisplay[1] = 9
    
    #if is at the most right, print # at the start for right edge wall and put starting to 0 (Prevent printing incorrect values)
    if xDisplay[0] < 0:
        xDisplay[0] = 0

        #for i in range will get the row position (e.g. 0 to 2 if y is 0 which prints first 2 row (Since the rop is a wall))
        #Need to add 1 to the end since in range stops before the end value
        for i in range(yDisplay[0], yDisplay[1]+1):
            print("|#", end="")

            #for in range will get the col position (e.g. 0 to 2 if x is 0 which will go after the "|#" since the side is a wall)
            #Need to add 1 to the end since in range stops before the end value
            for f in range(xDisplay[0], xDisplay[1]+1):
                #place player in middle
                if[f, i] == playerLocation:
                    print("M", end="")
                    continue
                print(fogMap[i][f], end="")
            print("|", end="\n")
    #Same as above but with the wall behind instead
    elif xDisplay[1] > 29:
        xDisplay[1] = 29
        for i in range(yDisplay[0], yDisplay[1] + 1):
            print("|", end="")
            for f in range(xDisplay[0], xDisplay[1]+1):
                #place player in middle
                if[f, i] == playerLocation:
                    print("M", end="")
                    continue
                print(fogMap[i][f], end="")
            print("#|", end="\n")
    #Same as above but without the wall
    else:
        for i in range(yDisplay[0], yDisplay[1]+1):
            print("|", end="")
            for f in range(xDisplay[0], xDisplay[1]+1):
                #place player in middle
                if[f, i] == playerLocation:
                    print("M", end="")
                    continue
                print(fogMap[i][f], end="")
            print("|", end="\n")
    
    #Since we altered the ydisplay, if the location is 8 then the ending 
    #would also be 9 which will print ### so instead we use the players location to determine the need for bottom wall
    if playerLocation[1] + 1 > 9:
        print("|###|")
    #Border
    print("+---+\n")

#------------------------Variables------------------------
#Map DataFile
dataFile = open("level1.txt", "r")

#Game Item Stats
#Pickaxe details index 1 is price and 2 is unlocked ore
pickaxeDetails = {1: [0, "copper"], 2: [50, "silver"], 3: [150, "gold"]}

#Player Stats
#track player location for everything (Map location etc)
playerLocation = [20, 3]

#Save choice for all interactions for easy if else statements
playerChoice = ""

#All of player stats to be accessed
playerStats = {"name": "", 
               "Day": 1, 
               "GP": 0, 
               "backpack": 10, 
               "steps": 0, 
               "load": 0, 
               "minerals": {"C": 0, "S": 0, "G": 0}, 
               "pickaxe": 1, 
               "portal": [-1, -1]}

#Map layout for true map and fog
map = []
fogMap = []

#------------------------Game Program------------------------


while True:
    DisplayMainMenu()

    playerChoice = input("Your Choice? ")

    if playerChoice == "q" or playerChoice == "Q":
        #Exit out program
        break
    elif playerChoice == "L" or playerChoice == "l":
        #To be added
        LoadData()
    elif playerChoice == "N" or playerChoice == "n":
        #Refresh Player's Stats (New Account)
        #Creates new map for player using level1.txt
        saveMap()

        #Clears starting fog around player
        ClearFog()

        #Collects player name to store
        playerStats["name"] = input("Greetings, miner! What is your name? ")
        print(f"Pleased to meet you, {playerStats["name"]}. Welcome to Sundrop Town!\n")
    else:
        #Invalid inputs redirects back to display main menu again
        print("Inavalid Input, please re-enter your choice\n")
        continue
    
    while True:
        #------------------------Town Menu------------------------
        SellOres(playerStats)

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
                elif (playerChoice == "B" or playerChoice == "b") and (playerStats["GP"] > playerStats['backpack'] * 2):
                    UpgradeBackpack()
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
        elif playerChoice == "V" or playerChoice == "v":
            #TBA
            SaveData()
        elif playerChoice == "E" or playerChoice == "e":
            DisplayMineMenu()
        elif playerChoice == "M" or playerChoice == "m":
            DisplayMap()
            continue
        else:
            print("Inavalid Input, please re-enter your choice")
