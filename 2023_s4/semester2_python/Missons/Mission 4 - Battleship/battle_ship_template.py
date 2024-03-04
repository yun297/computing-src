import random, copy


def get_mapping():
    f = open(r"C:\Users\zhuyu\computing\2023_sec4\semester2_python\Missons\Mission 4 - Battleship\ship_class_mapping.txt", "r")
    data = f.read().split("\n")[1:]
    f.close()

    data = list(map(lambda row: row.split(", "), data))
    ship_class_mapping = dict(
        map(lambda row: (row[0], (row[1], int(row[2]))), data))
    return ship_class_mapping


ship_class_mapping = get_mapping()
# print(get_mapping())

# your code here

class Ship():
    def __init__(self, ship_class):
        self._ship_class = ship_class
        coordinate = []
        
    # Accessor
    
    def get_class(self):
        return self._ship_class
    
    def get_abbr(self):
        return ship_class_mapping[self._ship_class][0]
    
    def get_size(self):
        return ship_class_mapping[self._ship_class][1]
    
    def check_sunk(self, coordinate):
        return coordinate in self._coordinate
 
class Board():
    def __init__(self, board = None, guess_board = None):
        self._board = board or [[" " for i in range(10)] for j in range(10)]
        self._guess_board = guess_board or [[" " for i in range(10)] for j in range(10)]
        self._ship_list = []

    def add_ship(self, ship, coordinate = None, orientation = None, depth = 0):
        
        temp_board = copy.deepcopy(self._board)
        coordinate_list = []
        
        coordinate = coordinate or [random.randint(0, 9), random.randint(0, 9)]
        orientation = orientation or random.randint(0, 1)
        
        try:
            if orientation == 0:
                for i in range(ship.get_size()):
                    if temp_board[coordinate[0]][coordinate[1] + i] != " ":
                        raise Exception
                    temp_board[coordinate[0]][coordinate[1] + i] = ship.get_abbr()
                    coordinate_list.append([coordinate[0], coordinate[1] + i])
            
            elif orientation == 1:
                for i in range(ship.get_size()):
                    if temp_board[coordinate[0] + i][coordinate[1]] != " ":
                        raise Exception
                    temp_board[coordinate[0] + i][coordinate[1]] = ship.get_abbr()
                    coordinate_list.append([coordinate[0] + i, coordinate[1]])
        
            self._board = temp_board
            ship._coordinate = coordinate_list
            self._ship_list.append(ship)
                        
        except:
            if depth < 10:
                self.add_ship(ship, None, None, depth + 1)
            else:
                print("Cannot add ship")
                print("Please restart the game")
                raise Exception("Cannot add ship")
            
    
    def display_board(self, guess_mode = False):
        numbers = "0123456789"
        alphabets = "ABCDEFGHIJ"
        print("    " + "   ".join(numbers))
        for i in range(10):
            print("  " + "+---" * 10 + "+") 
            print(alphabets[i] + " | " + " | ".join(self._guess_board[i] if guess_mode == True else self._board[i]) + " |")
        print("  " + "+---" * 10 + "+")
        
    
    def generate_new_game():
        # add ships to board
        board = Board()
        print("The following ships have entered the battlefield:")
        
        for ship_class in ship_class_mapping:
            # add 1-3 ships of each class
            generate_amount = random.randint(1, 3)
            for i in range(generate_amount):
                board.add_ship(Ship(ship_class))
            print(f"{ship_class} ({ship_class_mapping[ship_class][1]}): {generate_amount}")
        
        
        return board

    def guess(self, row: int, col: int):
        if self._guess_board[row][col] != " ":
            return False
        elif self._board[row][col] == " ":
            self._guess_board[row][col] = "X"
            return True
        else:
            self._board[row][col] = self._guess_board[row][col]
            return True
    
    def power_guess(self, row: int, col: int):
        if self._guess_board[row][col] != " ":
            return False
        elif self._board[row][col] == " ":
            self._guess_board[row][col] = "X"
            return True
        else:
            for ship in self._ship_list:
                if [row, col] in ship._coordinate:
                    self._board[row][col] = self._guess_board[row][col]
            return True
    
    def chcek_win(self):
        for ship in self._ship_list:
            if ship.check_sunk() == False:
                return False
        return True
    
def ui():
    print("+{}+\n| Welcome to Battleship! |\n+{}+".format("-" * 24, "-" * 24), end = "\n\n")
    board = Board.generate_new_game()
    
    print("\nHere is your board:", end = "\n\n")
    board.display_board()
    
    print("\nHere is your opponent's board (guess board):", end = "\n\n")
    board.display_board(True)
    
    print("\nLet's start the game!", end = "\n\n")
    print("Choose an option below:", end = "\n\n")
    print("+{}+{}+".format("-" * 3, "-" * 14))
    print("| 1 | Normal Guess |")
    print("| 2 | Power Guess  |")
    print("| 3 | Show Answer  |")
    print("| 4 | Restart Game |")
    print("| 5 | Exit Game    |")
    print("+{}+{}+".format("-" * 3, "-" * 14), end = "\n\n")
    
    user_choice = input("Enter your choice: ")
    
    if user_choice == "1":
        print("You have chosen Normal Guess")
        user_coordinate = input("Enter the coordinate you want to guess (e.g. A1): ")
        # map user_coordinate to row and col
        user_row = ord(user_coordinate[0]) - 65
        user_col = int(user_coordinate[1])
        
        if board.guess(user_row, user_col) == True:
            print("You have guessed {} correctly!".format(user_coordinate))
        else:
            print("You have guessed {} wrongly!".format(user_coordinate))
        
        print("\nHere is your board:", end = "\n\n")
        board.display_board()
        
        print("\nHere is your opponent's board (guess board):", end = "\n\n")
        board.display_board(True)
        
        if board.chcek_win() == True:
            print("You have won the game!")
        else:
            print("The game continues...")
    
    elif user_choice == "2":
        print("You have chosen Power Guess")
        user_coordinate = input("Enter the coordinate you want to guess (e.g. A1): ")
        # map user_coordinate to row and col
        user_row = ord(user_coordinate[0]) - 65
        user_col = int(user_coordinate[1])
        
        if board.power_guess(user_row, user_col) == True:
            print("You have guessed {} correctly!".format(user_coordinate))
        else:
            print("You have guessed {} wrongly!".format(user_coordinate))
        
        print("\nHere is your board:", end = "\n\n")
        board.display_board()
        
        print("\nHere is your opponent's board (guess board):", end = "\n\n")
        board.display_board(True)
        
        if board.chcek_win() == True:
            print("You have won the game!")
        else:
            print("The game continues...")
    
    elif user_choice == "3":
        print("You have chosen Show Answer")
        print("\nHere is your board:", end = "\n\n")
        board.display_board()
        
        print("\nHere is your opponent's board (guess board):", end = "\n\n")
        board.display_board(True)
        
        if board.chcek_win() == True:
            print("You have won the game!")
        else:
            print("The game continues...")
        
    elif user_choice == "4":
        print("You have chosen Restart Game")
        ui()
        
    elif user_choice == "5":
        print("You have chosen Exit Game")
        print("Thanks for playing!")
        return
    
ui()