from Chords import Chords
import random
from time import sleep


def homepage():
    """displays main menu"""
    print("""    1. Show me specific chords
    2. Let's do some exercise
    3. Let's do a quiz
    4. Generate all chords to file
    5. Exit""")
    pick = input()
    match pick:
        case "1":
            showing_chords()
        case "2":
            exercise()
        case "3":
            quiz()
        case "4":
            generate_all_to_file()
        case "5":
            print("Goodbye!")
        case _:
            pass


def inserting_chords():
    """returns list of chords provided by the user"""
    moll_chords = {'c', 'd', 'e', 'f', 'g', 'a', 'h', 'b'}
    moll_chords_7 = {'c7', 'd7', 'e7', 'f7', 'g7', 'a7', 'h7', 'b7'}
    print("Write chords you want to see, separated with space")
    chords_all = input()
    chords_list = chords_all.split()
    for i in chords_list:
        if i in moll_chords:
            chords_list[chords_list.index(i)] = i.upper() + 'm'
        elif i in moll_chords_7:
            chords_list[chords_list.index(i)] = i[0].upper() + 'm' + '7'
    return chords_list


def showing_chords():
    """displays list of chords which user wants"""
    chords_list = inserting_chords()
    base = open('chords_base.txt', 'r')
    for i in chords_list:
        base.seek(0)
        while True:
            line = base.readline()
            if line != "":
                if i + " " in line:
                    chord = Chords()
                    chord.name = i
                    space_pos = line.rfind(" ")
                    chord.grip = {
                        1: [int(line[space_pos + 2]), int(line[space_pos + 3]), int(line[space_pos + 4]),
                            int(line[space_pos + 5])],
                        2: [int(line[space_pos + 8]), int(line[space_pos + 9]), int(line[space_pos + 10]),
                            int(line[space_pos + 11])],
                        3: [int(line[space_pos + 14]), int(line[space_pos + 15]), int(line[space_pos + 16]),
                            int(line[space_pos + 17])],
                        4: [int(line[space_pos + 20]), int(line[space_pos + 21]), int(line[space_pos + 22]),
                            int(line[space_pos + 23])]}
                    chord.display()
                    break
            else:
                print(f"Invalid chord. There is no chord '{i}' in database.")
                break
    base.close()
    homepage()


def exercise():
    print("""The program will display a random chord for selected time and then change to another.
Try not to get lost and play along!\n""")
    while True:
        qty_str = input("Number of chords to practice: (insert number) ")
        try:
            qty = int(qty_str)
        except ValueError as e:
            print("Invalid value. Insert a number. Error description: ", e)
        else:
            break
    while True:
        duration_str = input("Duration of displaying each chord: (insert number)")
        try:
            duration = int(duration_str)
        except ValueError as e:
            print("Invalid value. Insert a number. Error description: ", e)
        else:
            break
    for i in ['3', '2', '1', '0', "Go!"]:
        print(i)
        sleep(1)
    all_chords = all_chords_list()
    for i in range(qty):
        random_chord = random.choice(all_chords)
        random_chord.display()
        sleep(duration)
    homepage()


def all_chords_list():
    base = open("chords_base.txt", "r")
    all_chords = []
    while True:
        line = base.readline()
        if line == "":
            break
        space_pos = line.rfind(" ")
        chord = Chords()
        chord.name = line[:space_pos]
        chord.grip = {
            1: [int(line[space_pos + 2]), int(line[space_pos + 3]), int(line[space_pos + 4]), int(line[space_pos + 5])],
            2: [int(line[space_pos + 8]), int(line[space_pos + 9]), int(line[space_pos + 10]),
                int(line[space_pos + 11])],
            3: [int(line[space_pos + 14]), int(line[space_pos + 15]), int(line[space_pos + 16]),
                int(line[space_pos + 17])],
            4: [int(line[space_pos + 20]), int(line[space_pos + 21]), int(line[space_pos + 22]),
                int(line[space_pos + 23])]}
        all_chords.append(chord)
    base.close()
    return all_chords


def quiz():
    """displays random chords without a name, user has to answer which chord it is"""
    print("""You will see random chord without a name. After displaying each chord write which one it is.
The quiz has 5 questions. Good luck!\n""")
    input("Press enter to start the quiz...")
    good_answers = 0
    all_chords = all_chords_list()
    for i in range(5):
        random_chord = random.choice(all_chords)
        original_name = random_chord.name
        random_chord.name = ""
        random_chord.display()
        answer = input("This is chord: ")
        if answer == original_name:
            print("Great!\n")
            good_answers += 1
        else:
            print("Wrong\n")
    print(f"Your score is: {good_answers}/5.\n")
    homepage()


def generate_all_to_file():
    """generates all chords to file"""
    new_file = open("ukulele_all_chords.txt", 'w')
    base = open("chords_base.txt", "r")
    while True:
        line = base.readline()
        if line == "":
            break
        space_pos = line.rfind(" ")
        chord = Chords()
        chord.name = line[:space_pos]
        chord.grip = {
            1: [int(line[space_pos + 2]), int(line[space_pos + 3]), int(line[space_pos + 4]), int(line[space_pos + 5])],
            2: [int(line[space_pos + 8]), int(line[space_pos + 9]), int(line[space_pos + 10]),
                int(line[space_pos + 11])],
            3: [int(line[space_pos + 14]), int(line[space_pos + 15]), int(line[space_pos + 16]),
                int(line[space_pos + 17])],
            4: [int(line[space_pos + 20]), int(line[space_pos + 21]), int(line[space_pos + 22]),
                int(line[space_pos + 23])]}
        chord.generate(new_file)
    base.close()
    new_file.close()
    print("All chords have been exported to external file 'ukulele_all_chords.txt'\n")
    homepage()


print("Welcome! What would you like to do today?")
homepage()
