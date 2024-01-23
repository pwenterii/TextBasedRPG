import random

global characterName
global characterRace
global characterClass
global characterStats

global races
global classes
global stats

races = ["Human", "Half-Elf", "Elf", "Half-Ork"]
classes = ["Fighter", "Ranger", "Wizard", "Rouge"]
stats = ["Strength", "Dexterity", "Constitution", "Wisdom", "Intelegence", "Charisma"]

def nameSetup():
    #introduction
    print("Hello! Welcome to ---- Text Bases RPG")

    #sets characters name
    characterName = input ('Name your character: ')
    characterName = str(characterName)
    print(f"Your character's name is now: {characterName}")

def raceSetup():
    #sets characters race
    print("Select a race for your character from the options bellow.")
    for x in range(len(races)):
        print(f"{x+1}. {races[x]}")
    race = input()
    race = int(race)

    #checks input
    if (race >= len(races) +1 or race <= 0):
        print("incorrect input made")
    else:
        print(f"Your character is now a {races[race-1]}")
        characterRace = races[race-1]

def classSetup():
    print("Select a class for your character from the options bellow")
    for x in range(len(classes)):
        print(f"{x+1}. {classes[x]}")
    charClass= input()
    charClass = int(charClass)

    #checks input
    if (charClass >= len(classes)+1 or charClass <=0):
        print("incorrect input made")
    else:
        print(f"Your character's class is now: {classes[charClass-1]}")
        characterClass = classes[charClass-1]

def statsSetup():
    characterStats = []
    print("Here are your character's stats:")
    for x in range(len(stats)):
        a = random.randint(1,6)
        b = random.randint(1,6)
        c = random.randint(1,6)
        result = a + b + c
        print(f"{stats[x]}: {result}")
        characterStats.append(result)

def characterCreation():
    nameSetup()
    raceSetup()
    classSetup()
    statsSetup()