# from random import randint

# tries = 0

# ans = randint (1,100)
# guess = int(input("Enter your guess: "))

# while guess != ans:
#     if guess < ans:
#         print("Your guess is too small!")
#     else:
#         print("Your guess is too large!")
#     tries += 1
#     guess = int(input("Enter your guess: "))

# print(f"{ans} is correct! No. of guesses: {tries}")

# mathematical and code-friendly method
students = int(input("How many students are there in total? "))

# initialise
football = 0

while students % 7 != 0:
  students -= 11
  football += 1

netball = students // 7

print(f"There should be {netball} teams and {football} teams")