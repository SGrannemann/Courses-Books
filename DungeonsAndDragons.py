from sys import exit
XP = 0
magic_weapon = False
professions = ['warrior', 'mage', 'thief']
character = ['class', XP, magic_weapon]

def inputNumber(message):
    while True:
        try:
            value = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return value
            break


def profession_choice():
    print("What is your class?")
    print("Are you a {}, {} or {}? ".format(professions[0], professions[1], professions[2]))
    choice = input("> ")

    if choice == "warrior":
        print("You are a strong warrior, wielding a mighty two-handed sword!")
        character[0] = 'warrior'
        #print(character[0])
        zombie_room()
    elif choice == "mage":
        print("You control the flow of the elements with your voice, wizard!")
        character[0] = 'mage'
        #print(character[0])
        zombie_room()
    elif choice == "thief":
        print("Your footsteps can hardly be heard...")
        character[0] = 'thief'
        #print(cahracter[0])
        zombie_room()
    else:
        print("You're a mongrel and get eaten.")
        start()

def start():
    print("You are an adventurer and stand outside a dungeon.")
    print("Upon entering, you realize this will be a dangerous, but potentially worthwile endeavor.")
    profession_choice()

def dead(reason):
    print(reason, "You failed!")
    exit(0)

def zombie_room():
    global XP
    print("You encounter a group of zombies standing between you and the next doors. What do you do?")
    print(""" You can...
    1. runaway!
    2. attack them with your sword
    3. throw a fireball into the group
    4. try to sneak around them to reach the door.
    """)
    #choice = input("> ")
    choice = inputNumber("What is your choice? ")

    if choice == 1:
        print("You are a bad adventurer!")
        start()

    elif choice == 2 and character[0] == 'warrior':

            print("You slice them to pieces. Well done!")
            XP += 10
            character[1] = XP
            #print(character[1])
            #print(XP)
            zombie_room_doors()
    elif choice == 3 and character[0] == 'mage':

            print("They burn to ashes before they can touch you!")
            XP += 10
            character[1] = XP
            #print(character[1])
            #print(XP)
            zombie_room_doors()
    elif choice == 4 and character[0] == 'thief':

            print("They are too dumb to recognize you.")
            XP += 10
            character[1] = XP
            #print(character[1])
            #print(XP)
            zombie_room_doors()
    else:
            dead("That was not a smart move!")

def zombie_room_doors():
    print("You see two doors. Take the left one or the right one?")
    choice_door = input("> ")
    if choice_door == "left":
        goblin_room()
    elif choice_door == "right":
        dragon_room()
    else:
        print("I don't know what you mean.")
        zombie_room_doors()

def goblin_room():
    global magic_weapon
    global XP

    print("You see two goblins guarding a treasure chest and a door.")
    print("""
    Your plan of action?
    1. Kill them with the sword!
    2. Kill them with fire!
    3. Kill them with being useless!
    4. Talk to them!
    """)
    choice = inputNumber("Your choice? ")

    if choice == 1 or choice == 2 or choice == 3:
        print("Well done. You open the chest and find a magic sword.")
        XP += 11
        magic_weapon = True
        for i in range(1, 3):
            if i == 1:
                character[i] = XP
                print("The experience is:", XP)
            #if i == 2:

            else:
                character[i] = True
                print("Do you have a magic weapon? ", magic_weapon)

        #print(character)
        dragon_room()
    else:
        dead("You dead, stupid!")
def dragon_room():
    print("You enter another room and right in front of you is a large dragon.")
    print("Are you prepared?")
    choice = input(" Attack or sneak back?")

    if choice == "attack" and character[2] == True and character[1] > 20:
        print("You slay the beast with your magical sword. Well done!")
        winner()
    elif 'sneak' in choice:
        print("You sneak back into the room with dead zombies.")
        zombie_room_doors()
    else:
        print("You attack, but the dragon is too strong.")
        dead("You die!")

def winner():
    print("************************************")
    print("You slaughtered all the peaceful creatures and gained a lot of nothing.")
    print("Well done!")
    print("************************************")
# Beginn des Programmablaufs
start()
