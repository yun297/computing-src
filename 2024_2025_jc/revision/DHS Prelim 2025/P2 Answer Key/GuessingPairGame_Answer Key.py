import random

class GuessingPairGame:
	#Provided
	def __init__(self):
		self.board = self.create_board()
		self.revealed = self.create_revealed_board()
		self.player_score = 0
		self.computer_score = 0
    
	# Provided	
	def create_board(self):
		#this is to generate the default board of size 2 x 4
		board = []
		for row_index in range(2):
			row = []
			for column_index in range(4):
				row.append(-1)
			board.append(row)
		return board
    
	# Provided
	def create_revealed_board(self):
		revealed = []
		for row_index in range(2):
			row = []
			for column_index in range(4):
				row.append(False)
			revealed.append(row)
		return revealed
    
	# Student to code [4 marks]
	def populate_board(self):
		#this is for populating the board by inserting the number pairs into the board
		row_col_chosen_list = []
		numbers_chosen = []
		random_row = -1
		random_column = -1
		random_num = -1

		# 4 pairs of 2 sets
		for i in range(4):
			#choosing random number
			while True:
				random_num = random.randint(1, 9) # 1 mark - generating random number
				if random_num not in numbers_chosen: #1 mark - ensuring that unique numbers are chosen for all pairs
					numbers_chosen.append(random_num)
					break

			#2 marks - insert the chosen random number into the board twice (must ensure no overriding of cells that have already been filled)
			for i in range(2):
				while True:
					random_row = random.randint(0, 1)
					random_column = random.randint(0, 3)
					if (random_row,random_column) not in row_col_chosen_list:
						self.board[random_row][random_column] = random_num
						row_col_chosen_list.append((random_row,random_column))
						break
            
		print(f"Revealed Board: {self.board}") #only for the Server side to display for students to see and take reference
    
	# Provided
	def set_board(self, values):
		#print(f"values: {values}")
		values = values.split(",") 
		#print(f"length of values: {len(values)}")
		receivedboard = []
		index = 0
		for i in range(2):
			row = []
			for j in range(4):
				row.append(int(values[index])) 
				index = index + 1
			receivedboard.append(row)
		self.board = receivedboard
		#print(receivedboard) #to be removed - now needed to show the board values to test
    
	# Provided
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
		
	# Provided	
	def board_in_string(self):
		result_string = ""
		for row in self.board:
			for value in row:
				result_string = result_string + str(value) + ","
		result_string = result_string[:-1]
		return result_string
	
	# Provided
	def valid_choice(self, row, column):
		valid = False
        
		if row >= 0 and row < 2 and column >= 0 and column < 4:
			if self.revealed[row][column] == False:
				valid = True

		return valid
    
	#below assumes that the row and columns chosen are valid as the main code should have used valid_choice method to check beforehand
	# Student to code [3 marks]
	def play_move(self, row1, column1, row2, column2):
		#print(f"row1: {row1}, column1: {column1}, row2: {row2}, column2: {column2}")
		#print(f"self.board[row1][column1]: {self.board[row1][column1]}, self.board[row2][column2]: {self.board[row2][column2]}")
		if self.board[row1][column1] == self.board[row2][column2]: # 1 mark - checking if the 2 cells selected have the same value and if yes, change their revealed value to True
			self.revealed[row1][column1] = True
			self.revealed[row2][column2] = True
			return self.board[row1][column1] #1 mark - return the score if match
		else:
			return 0 #1 mark - return 0 if no match
    
	# Student to code [2 marks - return True when all cells are revealed and False otherwise]   
	def is_game_over(self):
		for row_index in range(2):
			for column_index in range(4):
				if self.revealed[row_index][column_index] == False:
					return False
		return True