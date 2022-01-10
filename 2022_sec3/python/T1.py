# Q1. Print all the numbers between 1-1000 that has at least two 00 in it.
# Eg. 100, 1000.
# Note that 1-1000 are integers.

# Q2. Given S1=”Hello World”, print S1 in reverse. => output: “dlroW olleH”.

string = "Hello World"
stringLength = len(string)
slicedString = string[stringLength::-1]
print(slicedString)


# Q3. Given S2=”second string”.
# Print only “erg” using S2.

S2 = "second string"
print(S2[1] + S2[9] + S2[12])

# Q4. Get a number from the user and print out all the even digits only.
# Eg input=2343, output=24.