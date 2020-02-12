import time
import random
import words
import sys


def print_pause(string):
    print(string)
    time.sleep(2)


def intro():
    print_pause("You wake up in a cave, feeling dizzy.")
    print_pause("You don't remember how you got here.")
    print_pause("You realize you're not wearing your sword "
                "and shield like you remembered")
    print_pause("All you have now is your hands to protect yourself.")
    print_pause("You walk forward and the path splits into "
                "3 different paths. West, north and east.")


def west(items, monster):
    if "sword" in items:
        print_pause("You see an open chest and realize "
                    "you've already been here and opened the chest.")

    else:
        print_pause("You walk west and see a golden chest")
        print_pause("You open the golden chest.")
        print_pause("You find the Kingslayer, the sword once held by Reza.")
        items.append("sword")

    print_pause("You walk back to the crosspath.")
    crosspath(items, monster)


def north(items, monster):
    print_pause("You walk north and see a big " + monster + ".")
    print_pause("Behind the " + monster + ", you "
                "see a light! You found the way out of the tunnel!")
    while True:
        print_pause("You must choose .. (1) fight "
                    "the " + monster + " or (2) walk "
                    "back to the crosspath")
        respond = input("What will it be: \n")
        if respond == "1":
            fight(items, monster)
        elif respond == "2":
            print_pause("You decide to walk back to the crosspath.")
            crosspath(items, monster)
        else:
            print_pause("Sorry, I didn't understand that.")


def east(items, monster):
    if "shield" in items:
        print_pause("You can see by the dead gobling and "
                    "the open chest, that you've been here.")
        print_pause("You walk back to the crosspath.")
        crosspath(items, monster)
    else:
        print_pause("You walk east and see a small goblin "
                    "protecting a golden chest.")
        print_pause("The goblin attacks you and you attack to "
                    "defend yourself.")
        print_pause("The goblin is no match for you. It dies quickly.")
        print_pause("You open the chest and find a steel shield, "
                    "forged in A'skara.")
        items.append("shield")
        print_pause("You walk back to the crosspath.")
        crosspath(items, monster)


def fight(items, monster):
    print_pause("You choose to fight!")
    if "sword" in items and "shield" not in items:
        print_pause("You managed to cut the " + monster + " with "
                    "your sword.")
        print_pause("The " + monster + " hits too hard. You "
                    "need a shield to defeat the the enemy")
        print_pause("The " + monster + " hits its final blow, "
                    "and you die ..")
        end_game("loss")
    elif "shield" in items and "sword" not in items:
        print_pause("You try your best, but your fist don't "
                    "do any hurt to the " + monster + ".")
        print_pause("Your shield protects a lot of the hits, "
                    "but is now breaking.")
        print_pause("The " + monster + " hits its final blow, "
                    "and you die ..")
        end_game("loss")
    elif "sword" in items and "shield" in items:
        print_pause("You fight the " + monster + " bravely.")
        print_pause("Fortunately, you're geared with a great "
                    "sword and shield.")
        print_pause("After exchanging blows with "
                    "the " + monster + ", you finally struck "
                    "the " + monster + " in the heart.")
        print_pause("The " + monster + " dies, and you walk out of the cave.")
        end_game("win")
    else:
        print_pause("You try to fight the " + monster + " but "
                    "you're no match.")
        print_pause("The " + monster + " hits you one time, and you die..")
        end_game("loss")


def end_game(result):
    if result == "win":
        print_pause("Congratulatins! You won!")
    elif result == "loss":
        print_pause("Unfortunately, you lost the game.")
    while True:
        respond = input("Do you want to play again?(y) or (n)").lower()
        if respond == "y":
            print_pause("Restarting game ..")
            start_game()
        elif respond == "n":
            print_pause("Thanks for playing. Goodbye!")
            sys.exit()
        else:
            print_pause("Sorry, I didn't understand.")


def crosspath(items, monster):
    respond = input("Which path to you want to choose?"
                    "(west, north or east)\n").lower()
    if respond == "west":
        west(items, monster)
    elif respond == "north":
        north(items, monster)
    elif respond == "east":
        east(items, monster)
    else:
        print_pause("Sorry, I didn't get that. Try again.")
        crosspath(items, monster)


def start_game():
    items = []
    monster = random.choice(words.random_monsters)
    intro()
    crosspath(items, monster)


start_game()
