import random
import time
from time import sleep
import sys
menuChoice = ""
health = 10
accuracy = 3
defense = 7
damage = 3
attributeBuff = 0
gladiators = {}


class gladiator:

    name = ""
    specialty = ""
    win = 0

    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def setName(self, name):
        self.name = name

    def setSpecialty(self, specialty):
        self.specialty = specialty

    def getName(self):
        return self.name

    def getSpecialty(self):
        return self.specialty


# function for displaying strings one character at a time with delay
def printDelay(s):
    for x in s:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(.07)
    return ""


def playerAttack():
    attackRoll = 0
    global enemyHealth
    if enemyHealth > 0:
        if attributeBuff == 1:
            attackRoll = random.randint(4, 10)
            if attackRoll >= 7:
                enemyHealth = enemyHealth - 4
        elif attributeBuff == 2 or 3:
            attackRoll = random.randint(4, 10)
            if attackRoll >= 7:
                enemyHealth = enemyHealth - 3
        elif attributeBuff == 4:
            attackRoll = random.randint(5, 11)
            if attackRoll >= 7:
                enemyHealth = enemyHealth - 3
    elif enemyHealth >= 0:
        print()


# function for creating a gladiator with descriptions of the attribute increased by their specialty
def addGladiator(gladiators):
    if len(gladiators) > 0:
        printDelay("There is already a gladiator waiting for combat.")
        return None
    x = 0
    newName = str(input(printDelay("Name your gladiator: ")))
    print(printDelay("Your gladiator can be strong, hardy, or defensive. \n"))
    list1 = ["1: A strong gladiator deals damage +1.",
    "Damage is how much hurt they inflict.",
    "2: A hardy gladiator gains health +2.",
    "Health is how much damage your gladiator can sustain before being defeated.",
    "3: A defensive gladiator gains defense +1.",
    "Defense is how hard it is to get hit.",
    "4: An accurate gladiator gains accuracy +1.",
    "Accuracy is how easy it is to deal damage."]
    while x < len(list1):
        for x in range(len(list1)):
            print(printDelay(list1[x]))
            sleep(.5)
            x = x + 1
    specialty = str(input(printDelay("Declare your specialty by entering 1, 2, 3, or 4: ")))
    sleep(.5)
    gladiators[newName] = gladiator(newName, specialty)
    global attributeBuff
    attributeBuff = specialty
    print(printDelay("Your gladiator is ready for combat!"))
    sleep(.5)
    return gladiators


def combat():
    x = 0
    global turn
    turn = 0
    global enemyHealth
    enemyHealth = 10
    global enemyAccuracy
    enemyAccuracy = 3
    global enemyDefense
    enemyDefense = 7
    global enemyDamage
    enemyDamage = 3
    # possibly make the enemy list into a dictionary
    #to have different stats for each enemy
    enemyList = ["Krogthoul the Mighty",
             "Gourool the Bone-Masher",
             "Feakleur the Giant",
             "The Dire Lion",
             "S'Kartha the Great",
             "King D'Haru",
             "Tahkfon of Quickness"]
    enemy = random.choice(enemyList)
    list5 = ["The gates open to reveal your opponent...",
    enemy,
    " emerges from the darkness at the hush of the once roaring crowd."]
    while x < len(list5):
        for x in range(len(list5)):
            print(printDelay(list5[x]))
            sleep(.5)
            x = x + 1
    print(printDelay("Do you charge or stand firm awaiting their attack?"))
    starting = str(input(printDelay("Enter either charge or stand: ")))
    if starting == "charge":
        playerAttack()
        turn = turn + 1
    elif starting == "stand":
        print()
        



def viewGladiators(gladiators):
    if len(gladiators) > 0:
        for x in gladiators.keys():
            name = gladiators[x].getName()
            specialty = gladiators[x].getSpecialty()
            print(printDelay(("Name:", name, "\tSpecialty:", specialty, "\n")))
    else:
        printDelay("There are no gladiators to view.")
    return gladiators


def saveGladiators(gladiators, fileName):
    x = 0
    outFile = open(fileName, "wt")
    for x in gladiators.keys():
        name = gladiators[x].getName()
        specialty = gladiators[x].getSpecialty()
        win = gladiators[x].getWin()
        outFile.write(name + "," + specialty + "," + win + "\n")
    list3 = ["Saving...",
    "Data saved successfully"]
    while x < len(list3):
        for x in range(len(list3)):
            print(printDelay(list3[x]))
            sleep(2)
            x = x + 1

def loadGladiators(gladiators, fileName):
    if len(gladiators) > 0:
        printDelay("There is already a gladiator waiting for combat.")
        return None
    x = 0
    inFile = open(fileName, "rt")
    while True:
        inLine = inFile.readline()
        if not inLine:
            break
        inLine = inLine[:-1]
        name, specialty = inLine.split(",")
        gladiators[name] = gladiator(name, specialty)
    list4 = ["Loading..."
    "Data loaded successfully :)"]
    while x < len(list4):
        for x in range(len(list4)):
            print(printDelay(list4[x]))
            sleep(2)
            x = x + 1
    inFile.close()
    return gladiators


def retireGladiator(gladiators):
    retiree = str(input(printDelay("Which player would you like to remove? (names are case sensitive): ")))
    if retiree in gladiators:
        del gladiators[retiree]
        printDelay("The gladiator has been permanently retired.")
    else:
        printDelay(retiree + "has not been found")
    return gladiators


def menu():
    x = 0
    list2 = ["Welcome to the Arena.",
    "Enter 1 to create your gladiator.",
    "Enter 2 to begin combat.",
    "Enter 3 to view your gladiators.",
    "Enter 4 to save your record.",
    "Enter 5 to load a past gladiator.",
    "Enter 6 to retire a gladiator",
    "Enter 9 to exit."]
    while x < len(list2):
        for x in range(len(list2)):
            print(printDelay(list2[x]))
            sleep(.5)
            x = x + 1
    global menuChoice
    menuChoice = str(input(printDelay("Please enter an option from the menu to begin: ")))
    sleep(.5)


while menuChoice != "9":
    menu()
    if menuChoice == "1":
        addGladiator(gladiators)
        if attributeBuff == 1:
            damage = damage + 1
        elif attributeBuff == 2:
            health = health + 2
        elif attributeBuff == 3:
            defense = defense + 1
        elif attributeBuff == 4:
            accuracy = accuracy + 1
        else:
            ""
    elif menuChoice == "2":
        combat()
    elif menuChoice == "3":
        viewGladiators(gladiators)
    elif menuChoice =="4":
        fileName = str(input(printDelay("Please enter a file name to save to.")))
        saveGladiators(gladiators, fileName)
    elif menuChoice == "5":
        fileName = str(input(printDelay("Please enter a file name to load from.")))
        loadGladiators(gladiators, fileName)
    elif menuChoice =="6":
        retireGladiator(gladiators)
    else:
        printDelay("Your entry is invalid. Please try again.")
