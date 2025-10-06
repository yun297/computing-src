#Type your name here: 
import random

class GuessingPairGame:
	def __init__(self):
		self.board = self.create_board()
		self.revealed = self.create_revealed_board()
		self.player_score = 0
		self.computer_score = 0
    
	def create_board(self):
		board = []
		for row_index in range(2):
			row = []
			for column_index in range(4):
				row.append(-1)
			board.append(row)
		return board
    
	def create_revealed_board(self):
		revealed = []
		for row_index in range(2):
			row = []
			for column_index in range(4):
				row.append(False)
			revealed.append(row)
		return revealed
    
	#code the below function
	def populate_board(self):
		pass
    
	def set_board(self, values):
		values = values.split(",") 
		receivedboard = []
		index = 0
		for i in range(2):
			row = []
			for j in range(4):
				row.append(int(values[index])) 
				index = index + 1
			receivedboard.append(row)
		self.board = receivedboard
    
	def print_board(self):
		print("\nBoard:")
		for row_index in range(2):
			row_display = []
			for column_index in range(4):
				if self.revealed[row_index][column_index]:
					row_display.append(" " + str(self.board[row_index][column_index]) + " ")
				else:
					row_display.append(" X ")
			print("|".join(row_display))
		print()
		
	def board_in_string(self):
		result_string = ""
		for row in self.board:
			for value in row:
				result_string = result_string + str(value) + ","
		result_string = result_string[:-1]
		return result_string
	
	def valid_choice(self, row, column):
		valid = False
		if row >= 0 and row < 2 and column >= 0 and column < 4:
			if self.revealed[row][column] == False:
				valid = True
		return valid
    
	#code the below function
	def play_move(self, row1, column1, row2, column2):
		pass
    
	#code the below function  
	def is_game_over(self):
		pass