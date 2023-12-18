class player:
    def __init__(self, first, last, age, pos, weight, feet, inches, college, salary):
        self.first = first
        self.last = last
        self.age = age
        self.pos = pos
        self.feet = feet
        self.inches = inches
        self.college = college
        self.weight = weight
        self.salary = salary

    def print_info(self):
        print(f'{self.first} {self.last}')
        print(f'    - Age: {self.age}')
        print(f'    - Position: {self.pos}')
        print(f'    - Weight: {self.weight}')
        print(f'    - Height: {self.feet} {self.inches}')
        print(f'    - College: {self.college}')
        print(f'    - Salary: {self.salary}')

    def print_name(self):
        print(f'{self.first} {self.last}')

    def print_age(self):
        print(f'{self.first} {self.last}... {self.age} years old')

    def print_pos(self):
        print(f'{self.first} {self.last}... {self.pos}')

    def print_weights(self):
        print(f'{self.first} {self.last}... {self.weight} lbs')

    def print_heights(self):
        print(f'{self.first} {self.last}... {self.feet}{self.inches}')

    def print_colleges(self):
        print(f'{self.first} {self.last}... {self.college}')

    def print_salaries(self):
        print(f'{self.first} {self.last}... {self.salary}')

try:
    file = open("lakersroster2023.tsv")

    print("Commands: ")
    print(" - show player names")
    print(" - show player ages")
    print(" - show player positions")
    print(" - show player weights")
    print(" - show player heights")
    print(" - show player colleges")
    print(" - show player salaries")
    print(" - show full stats")
    print(" - commands")
    print(" - finish (closes program) \n")
    user_guess = input("Enter Command: ").lower().strip()

    print("\n... Fetching Data ...\n")

    players = []
    playerdata = ''

    for x in file:
        playerdata = x.split()
        players.append(player(playerdata[0], playerdata[1], playerdata[3], playerdata[2], playerdata[6], playerdata[4],
                              playerdata[5], playerdata[7], playerdata[8]))

    while user_guess != 'finish':
        if user_guess == "show player names":
            for player in players:
                player.print_name()
        elif user_guess == "show player ages":
            for player in players:
                player.print_age()
        elif user_guess == "show player positions":
            for player in players:
                player.print_pos()
        elif user_guess == "show player weights":
            for player in players:
                player.print_weights()
        elif user_guess == "show player heights":
            for player in players:
                player.print_heights()
        elif user_guess == "show player colleges":
            for player in players:
                player.print_colleges()
        elif user_guess == "show player salaries":
            for player in players:
                player.print_salaries()
        elif user_guess == "show full stats":
            for player in players:
                player.print_info()
                print()
        elif user_guess == "commands":
            print("Commands: ")
            print(" - show player names")
            print(" - show player ages")
            print(" - show player positions")
            print(" - show player weights")
            print(" - show player heights")
            print(" - show player colleges")
            print(" - show player salaries")
            print(" - show full stats")
            print(" - commands")
            print(" - finish (closes program)")
        elif user_guess == "commands":
            print("\n... Closing File ...\n")
            file.close()
        else:
            print("Invalid Command")
            print(" - 'commands' for commands")

        user_guess = input("\nEnter Command: ").lower().strip()

        print("\n... Fetching Data ...\n")

except Exception as excpt:
    print("Issue Opening File | Error:", excpt)
