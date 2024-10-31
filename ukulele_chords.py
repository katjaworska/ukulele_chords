from Chords import Chords


def homepage():
    """displays main menu"""
    print("""    1. Show me specific chords
    2. Let's do some exercise
    3. Generate all chords to file
    4. Exit
    """)
    pick = input()
    match pick:
        case "1":
            showing_chords()
        case "2":
            exercise()
        case "3":
            generate_all_to_file()
        case "4":
            print("Goodbye!")
        case _:
            pass


def showing_chords():
    """displays list of chords which user wants"""
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
    base = open('chords_base.txt', 'r')
    for i in chords_list:
        base.seek(0)
        while True:
            line = base.readline()
            if line != "":
                if i + "" in line:
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
    print("Sorry, no functionality yet\n")
    homepage()
    pass


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
