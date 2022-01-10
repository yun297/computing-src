#Zhu Yunsong 29
#2i2
#Q2_ZhuYunsong.py


def main():
	num = int(input("Enter your score: "))
	if (num > 74):
		print("Your grade is A1.")
	elif (num < 75 and num > 69):
		print("Your grade is A2.")
	elif (num < 70 and num > 64):
		print("Your grade is B3.")
	elif (num < 65 and num > 59):
		print("Your grade is B4.")
	elif (num < 60 and num > 54):
		print("Your grade is C5.")
	elif (num < 55 and num > 49):
		print("Your grade is C6.")
	elif (num < 49 and num > -1):
		print("You failed.")
	else:
		print("The score is invalid.")


main()
