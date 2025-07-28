#Vernon Loh Jin Feng - IM02 - S10270739K
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
    return

def UpgradeBackpack():
    return

def DisplayPlayerInformation():
    return

def DisplayMap():
    return

def DisplayMineMenu():
    return

def Move(movementInput):
    return

def UsePortalStone():
    return

#------------------------Variables------------------------
#------------------------PlayerStats------------------------
playerChoice = ""
playerStats = {"name": "", "Day": 0, }
#------------------------Game Program------------------------

while True:
    DisplayMainMenu()

    playerChoice = input("Your Choice? ")

    if playerChoice == "q" or playerChoice == "Q":
        #Exit out program
        break
    elif playerChoice == "L" or playerChoice == "l":
        LoadData()
    elif playerChoice == "N" or playerChoice == "n":
        playerStats["name"] = input("Greetings, miner! What is your name? ")
        print(f"Pleased to meet you, {playerStats["name"]}. Welcome to Sundrop Town!\n")
    else:
        print("Inavalid Input, please")
    
    while True:
        playerStats["Day"] += 1
        DisplayTownMenu()
        playerChoice = input("Your Choice? ")

        if playerChoice == "q" or playerChoice == "Q":
            #Back to main menu
            break
        elif playerChoice == "B" or playerChoice == "b":
            DisplayShopMenu()
        elif playerChoice == "I" or playerChoice == "i":
            DisplayPlayerInformation()
        elif playerChoice == "V" or playerChoice == "v":
            SaveData()
        elif playerChoice == "E" or playerChoice == "e":
            DisplayMineMenu()
        elif playerChoice == "M" or playerChoice == "m":
            DisplayMap()
        else:
            print("Inavalid Input, please re-enter your choice")
