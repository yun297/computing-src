import socket 
from GuessingPairGame import GuessingPairGame

print("-------------------")
print("GUESSING PAIR GAME")
print("-------------------")
print()

game = GuessingPairGame()

my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 9876)) #1 mark - creating the socket with correct ip address and port number

board = my_socket.recv(1024).decode() #1 mark - receive the board cell values from the server program and decode it
#print(f"board: {board}")

game.set_board(board) #1 mark - setting the board cell values with the values received from the server program
game.print_board()

while True:
    #player guessing the 2 coordinates
    #1 mark - getting the first and second coordinate values from human player
    row_1 = int(input("INPUT first coordinates row number: "))
    col_1 = int(input("INPUT first coordinates column number: "))
    while game.valid_choice(row_1, col_1) == False:
        row_1 = int(input("INPUT first coordinates row number: "))
        col_1 = int(input("INPUT first coordinates column number: "))

    print()
    
    #getting the second coordinate values
    row_2 = int(input("INPUT second coordinates row number: "))
    col_2 = int(input("INPUT second coordinates column number: "))
    while game.valid_choice(row_2, col_2) == False or (row_1 == row_2 and col_1 == col_2): #1 mark - checking the validity of the user input and additional checking if the first and second user inputs are the same and prompt for re-input if needed 
        row_2 = int(input("INPUT second coordinates row number: "))
        col_2 = int(input("INPUT second coordinates column number: "))

    print()
    #print(f"Player chose: row 1: {row_1}, col 1: {col_1}, row 2: {row_2}, col 2: {col_2}")
    score = game.play_move(row_1, col_1, row_2, col_2) #1 mark - play move and display a suitable message (either no match or Its a match! You scored {score} points)
    #print(f"Score: {score}")
    if score > 0:
        print(f"Its a match! You scored {score} points")
    else:
        print("No match!")
    game.player_score = game.player_score + score #1 mark - adding to player score accordingly
    print(f"Player Score: {game.player_score}")
    print(f"Computer Score: {game.computer_score}")
    game.print_board()
    coordinates = str(row_1) + "," + str(col_1) + "," + str(row_2) + "," + str(col_2) 
    my_socket.sendall(coordinates.encode()) #1 mark - sending the user's selected cells' coordinates to server program
    if game.is_game_over() == True: #1 mark - checking if game is over after user input
        break

    #receive the 2 coordinates from computer player
    coordinates = my_socket.recv(1024).decode() 
    #print(coordinates)

    row_1, col_1, row_2, col_2 = coordinates.split(",")
    print(f"Computer chose: row 1: {row_1}, col 1: {col_1}, row 2: {row_2}, col 2: {col_2}")
    score = game.play_move(int(row_1), int(col_1), int(row_2), int(col_2)) #1 mark - receiving computer's move and play move accordingly and display a suitable message (either Computer has no match or Computer has a match! Computer scored {score} points)
    #print(f"Score: {score}")
    if score > 0:
        print(f"Its a match! Computer scored {score} points")
    else:
        print("Computer has no match!")
    game.computer_score = game.computer_score + score #1 mark - adding to computer score accordingly
    print(f"Player Score: {game.player_score}")
    print(f"Computer Score: {game.computer_score}")
    game.print_board()
    if game.is_game_over() == True: #1 mark - checking if game is over after computer input
        break

if game.player_score > game.computer_score: #1 mark - displaying relevant message at the end of the game
    print("You win!")
else:
    print("You lose!")
                                  
my_socket.close() #1 mark for closing the socket

print("-------------------")
print("GAME ENDED")
print("-------------------")
