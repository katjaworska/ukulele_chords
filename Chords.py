class Chords:
    name = ""
    grip = {}

    def display(self):
        """displays a single chord"""
        frets = [1, 2, 3, 4]
        strings = ['G', 'C', 'E', 'A']
        print(f"** {self.name} **\n_______")
        for fret in frets:
            i = 0
            for _ in strings:
                if self.grip[fret][i] == 1 and i != 3:
                    print("O_", end="")
                elif self.grip[fret][i] == 1 and i == 3:
                    print("O")
                elif self.grip[fret][i] == 0 and i != 3:
                    print("|_", end="")
                else:
                    print("|")
                i += 1
        print()

    def generate(self, file):
        """generates a single chord to file"""
        frets = [1, 2, 3, 4]
        strings = ['G', 'C', 'E', 'A']
        file.write(f"** {self.name} **\n_______\n")
        for fret in frets:
            i = 0
            list1 = []
            for _ in strings:
                if self.grip[fret][i] == 1 and i != 3:
                    list1.append("O_")
                elif self.grip[fret][i] == 1 and i == 3:
                    list1.append("O")
                elif self.grip[fret][i] == 0 and i != 3:
                    list1.append("|_")
                else:
                    list1.append("|")
                i += 1
            list1.append("\n")
            file.writelines(list1)
        file.writelines("\n")