import os, random

run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False

HP = 50
HPMAX = 50
ATK = 3
pot = 1
elix = 0
gold = 0
x = 0
y = 0

        #  x = 0       x = 1       x = 2       x = 3       x = 4       x = 5         x = 6
map = [["plains",   "plains",   "plains",   "plains",   "forest", "mountain",       "cave"],    # y = 0
       ["forest",   "forest",   "forest",   "forest",   "forest",    "hills",   "mountain"],    # y = 1
       ["forest",   "fields",   "bridge",   "plains",    "hills",   "forest",      "hills"],    # y = 2
       ["plains",     "shop",     "town",    "mayor",   "plains",    "hills",   "mountain"],    # y = 3
       ["plains",   "fields",   "fields",   "plains",    "hills", "mountain",   "mountain"]]    # y = 4

y_len = len(map)-1
x_len = len(map[0])-1

biom = {
    "plains": {
        "t": "PLAINS",
        "e": True},
    "forest": {
        "t": "WOODS",
        "e": True},
    "fields": {
        "t": "FIELDS",
        "e": False},
    "bridge": {
        "t": "BRIGE",
        "e": True},
    "town": {
        "t": "TOWN CENTRE",
        "e": False},
    "shop": {
        "t": "SHOP",
        "e": False},
    "mayor": {
        "t": "MAYOR",
        "e": False},
    "cave": {
        "t": "CAVE",
        "e": False},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True},
    "hills": {
        "t": "HILLS",
        "e": True,
    }
}

e_list = ["Goblin", "Orc", "Slime"]

mobs = {
    "Goblin": {
        "hp": 15,
        "at": 3,
        "go": 8
    },
    "Orc": {
        "hp": 35,
        "at": 5,
        "go": 18
    },
    "Slime": {
        "hp": 30,
        "at": 2,
        "go": 12
    },
    "Dragon": {
        "hp": 100,
        "at": 8,
        "go": 100
    }
}


def clear():
    os.system("cls")


def draw():
    print("xX--------------------xX")


def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    file = open("load.txt", "w")

    for item in list:
        file.write(item + "\n")
    file.close()


def heal(amount):
    global HP
    if HP + amount < HPMAX:
        HP += amount
    else:
        HP = HPMAX
    print(name + "'s HP refilled to " + str(HP) + "!")


def battle():
    global fight, play, run, HP, pot, elix, gold, boss

    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Dragon"
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]

    while fight:
        clear()
        draw()
        print("Defeat the " + enemy + "!")
        draw()
        print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
        print(name + "'s HP: " + str(HP) + "/" + str(HPMAX))
        print("POTIONS: " + str(pot))
        print("ELIXIR: " + str(elix))
        draw()
        print("1 - ATTACK")
        if pot > 0:
            print("2 - USE POTION (30HP)")
        if elix > 0:
            print("3 - USE ELIXIR (50HP)")
        draw()

        choice = input("# ")

        if choice == "1":
            hp -= ATK
            print(name + " dealt " + str(ATK) + " damage to the " + enemy + ".")
            if hp > 0:
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            input("> ")

        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(30)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            else:
                print("No potions!")
            input("> ")

        elif choice == "3":
            if elix > 0:
                elix -= 1
                heal(50)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            else:
                print("No elixirs!")
            input("> ")

        if HP <= 0:
            print(enemy + " defeated " + name + "...")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")

        if hp <= 0:
            print(name + " defeated the " + enemy + "!")
            draw()
            fight = False
            gold += g
            print("You've found " + str(g) + " gold!")
            if random.randint(0, 100) < 30:
                pot += 1
                print("You've found a potion!")
            if enemy == "Dragon":
                draw()
                print("Congratulations, you've finished the game!")
                boss = False
                play = False
                run = False
            input("> ")
            clear()


def shop():
    global buy, gold, pot, elix, ATK

    while buy:
        clear()
        draw()
        print("Welcome to the shop!")
        draw()
        print("GOLD: " + str(gold))
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str(elix))
        print("ATK: " + str(ATK))
        draw()
        print("1 - BUY POTION (30HP) - 5 GOLD")
        print("2 - BUY ELIXIR (MAXHP) - 8 GOLD")
        print("3 - UPGRADE WEAPON (+2ATK) - 10 GOLD")
        print("4 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            if gold >= 5:
                pot += 1
                gold -= 5
                print("You've bought a potion!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "2":
            if gold >= 8:
                elix += 1
                gold -= 8
                print("You've bought an elixir!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "3":
            if gold >= 10:
                ATK += 2
                gold -= 10
                print("You've upgraded your weapon!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "4":
            buy = False


def mayor():
    global speak, key

    while speak:
        clear()
        draw()
        print("Hello there, " + name + "!")
        if ATK < 10:
            print("You're not strong enough to face the dragon yet! Keep practicing and come back later!")
            key = False
        else:
            print("You might want to take on the dragon now! Take this key but be careful with the beast!")
            key = True

        draw()
        print("1 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            speak = False


def cave():
    global boss, key, fight

    while boss:
        clear()
        draw()
        print("Here lies the cave of the dragon. What will you do?")
        draw()
        if key:
            print("1 - USE KEY")
        print("2 - TURN BACK")
        draw()

        choice = input("# ")

        if choice == "1":
            if key:
                fight = True
                battle()
        elif choice == "2":
            boss = False



while run:
    while menu:
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")

        if rules:
            print("I'm the creator of this game and these are the rules.")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")

        if choice == "1":
            clear()
            name = input("# What's your name, hero? ")
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    elix = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    clear()
                    print("Welcome back, " + name + "!")
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Corrupt save file!")
                    input("> ")
            except OSError:
                print("No loadable save file!")
                input("> ")
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        save()  # autosave
        clear()

        if not standing:
            if biom[map[y][x]]["e"]:
                if random.randint(0, 100) < 30:
                    fight = True
                    battle()

        if play:
            draw()
            print("LOCATION: " + biom[map[y][x]]["t"])
            draw()
            print("NAME: " + name)
            print("HP: " + str(HP) + "/" + str(HPMAX))
            print("ATK: " + str(ATK))
            print("POTIONS: " + str(pot))
            print("ELIXIRS: " + str(elix))
            print("GOLD: " + str(gold))
            print("COORD:", x, y)
            draw()
            print("0 - SAVE AND QUIT")
            if y > 0:
                print("1 - NORTH")
            if x < x_len:
                print("2 - EAST")
            if y < y_len:
                print("3 - SOUTH")
            if x > 0:
                print("4 - WEST")
            if pot > 0:
                print("5 - USE POTION (30HP)")
            if elix > 0:
                print("6 - USE ELIXIR (50HP)")
            if map[y][x] == "shop" or map[y][x] == "mayor" or map[y][x] == "cave":
                print("7 - ENTER")
            draw()

            dest = input("# ")

            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == "1":
                if y > 0:
                    y -= 1
                    standing = False
            elif dest == "2":
                if x < x_len:
                    x += 1
                    standing = False
            elif dest == "3":
                if y < y_len:
                    y += 1
                    standing = False
            elif dest == "4":
                if x > 0:
                    x -= 1
                    standing = False
            elif dest == "5":
                if pot > 0:
                    pot -= 1
                    heal(30)
                else:
                    print("No potions!")
                input("> ")
                standing = True
            elif dest == "6":
                if elix > 0:
                    elix -= 1
                    heal(50)
                else:
                    print("No elixirs!")
                input("> ")
                standing = Tru
            elif dest == "7":
                if map[y][x] == "shop":
                    buy = True
                    shop()
                if map[y][x] == "mayor":
                    speak = True
                    mayor()
                if map[y][x] == "cave":
                    boss = True
                    cave()
            else:
                standing = True

