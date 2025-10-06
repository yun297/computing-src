import socket, random
from GuessingPairGame import GuessingPairGame

print("-------------------")
print("GUESSING PAIR GAME")
print("-------------------")
print()

listen_socket = socket.socket() 
listen_socket.bind(('127.0.0.1', 9876)) 
listen_socket.listen()

print("Waiting for player to join")
print("---------------------------")
new_socket, addr = listen_socket.accept()

#create a new board and display
game = GuessingPairGame()
game.populate_board()
game.print_board()

#send the board's populated cell values to the client program
new_socket.sendall(game.board_in_string().encode())

while True:
    #receive the 2 coordinates from client player and do the necessary updates
    coordinates = new_socket.recv(1024).decode()
    row_1, col_1, row_2, col_2 = coordinates.split(",")
    print(f"Player chose: row 1: {row_1}, col 1: {col_1}, row 2: {row_2}, col 2: {col_2}")
    score = game.play_move(int(row_1), int(col_1), int(row_2), int(col_2))
    game.player_score = game.player_score + score
    print(f"Player Score: {game.player_score}")
    print(f"Computer Score: {game.computer_score}")
    game.print_board()
    if game.is_game_over() == True:
        break

    #computer player randomly choosing 2 coordinates 
    #getting the first coordinate values
    row_1 = random.randint(0, 1)
    col_1 = random.randint(0, 3)
    while game.valid_choice(row_1, col_1) == False:
        row_1 = random.randint(0, 1)
        col_1 = random.randint(0, 3)

    #getting the second coordinate values
    row_2 = random.randint(0, 1)
    col_2 = random.randint(0, 3)
    while game.valid_choice(row_2, col_2) == False or (row_1 == row_2 and col_1 == col_2):
        row_2 = random.randint(0, 1)
        col_2 = random.randint(0, 3)

    print(f"Computer chose: row 1: {row_1}, col 1: {col_1}, row 2: {row_2}, col 2: {col_2}")
    score = game.play_move(row_1, col_1, row_2, col_2)
    game.computer_score = game.computer_score + score
    print(f"Player Score: {game.player_score}")
    print(f"Computer Score: {game.computer_score}")
    game.print_board()
    coordinates = str(row_1) + "," + str(col_1) + "," + str(row_2) + "," + str(col_2) 
    new_socket.sendall(coordinates.encode())
    if game.is_game_over() == True:
        break

if game.player_score > game.computer_score:
    print("Player win!")
else:
    print("Player lose!")
new_socket.close()

listen_socket.close()

print("-------------------")
print("GAME ENDED")
print("-------------------")
