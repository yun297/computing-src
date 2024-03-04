# Question 1: bin_to_den - for loop

def bin_to_den(bin_num, den_num = 0):
    for i in range(len(bin_num)):
        if int(bin_num[i]) == 1:
            den_num += 2 ** (len(bin_num) - i - 1)
        else:
            continue
    return den_num

# Question 2: bin_to_den - while loop

def bin_to_den(bin_num, den_num = 0):
    i = 0
    while i < len(bin_num):
        if int(bin_num[i]) == 1:
            den_num += 2 ** (len(bin_num) - i - 1)
        i += 1
    return den_num

# Question 3: bin_to_den - recursion

def bin_to_den(bin_num, den_num = 0, i = 0):
    if i == len(bin_num):
        return den_num
    elif int(bin_num[i]) == 1:
        den_num += 2 ** (len(bin_num) - i - 1)
    return bin_to_den(bin_num, den_num, i + 1)

# Question 4: den_to_bin - while loop

def den_to_bin(den_num, bin_num = ""):
    while den_num > 0:
        remainder = den_num % 2
        bin_num = str(remainder) + bin_num
        den_num //= 2
    return bin_num

# Question 5: den_to_bin - recursion

def den_to_bin(den_num, bin_num = ""):
    if den_num == 0:
        return bin_num
    else:
        remainder = den_num % 2
        bin_num = str(remainder) + bin_num
        return den_to_bin(den_num // 2, bin_num)

# Question 6: value_to_symbol and symbol_to_value

valid_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def value_to_symbol(value):
    return valid_digits[value]

def symbol_to_value(symbol):
    return valid_digits.find(symbol)

# Question 7: any_to_den(any_num, base)

def any_to_den(any_num, base, den_num = 0):
    if any_num == "":
        return den_num
    else:
        last_digit = symbol_to_value(any_num[-1])
    return last_digit + base * any_to_den(any_num[:-1], base)

# Question 8: den_to_any(den_num, base)

def den_to_any(den_num, base, any_num = ""):
    if den_num == 0:
        return any_num
    else:
        any_num = value_to_symbol(den_num % base) + any_num # add the remainder to the left of the string
        return den_to_any(den_num // base, base, any_num)

# Question 9: bin_to_hex

def bin_to_hex(bin_num):
    den_num = bin_to_den(bin_num)
    return den_to_any(den_num, 16)

# Question 10: hex_to_bin

def hex_to_bin(hex_num):
    den_num = any_to_den(hex_num, 16)
    return den_to_bin(den_num)

# User Interface

def mainUI():
    
    invalidInput = True
    
    baseOptions = {
        "1": "Binary",
        "2": "Denary",
        "3": "Hex",
        "4": "Octal",
    }
     
    print("Welcome to the Number Converter!")
    
    while invalidInput:
        print("Select the base you want to convert FROM:")
        print()
        print("#---#--------#")
        print("| * | Base   |")
        print("#---#--------#")
        print("| 1 | Binary |")
        print("| 2 | Denary |")
        print("| 3 | Hex    |")
        print("| 4 | Octal  |")
        print("| 5 | Exit   |")
        print("#---#--------#")
        print()
        baseOption1 = input("Enter 1 - 5: ")
        print()
    
        if int(baseOption1) not in range(1, 6):
            print("Invalid input. Please try again.")
            print()
            invalidInput = True
        elif int(baseOption1) == 5:
            print("Thank you for using the Number Converter! Terminating program...")
            exit()
        else:
            invalidInput = False
            outputString = f"Selected: {baseOptions[baseOption1]}"
            print("#" + (len(outputString) + 2) * "-", end = "#\n")
            print(f"| Selected: {baseOptions[baseOption1]} |")
            print("#" + (len(outputString) + 2) * "-", end = "#\n")
            print()
            
    invalidInput = True
            
    while invalidInput:
    
        print("Select the base you want to convert TO:")
        print()
        print("#---#--------#")
        print("| * | Base   |")
        print("#---#--------#")
        print("| 1 | Binary |")
        print("| 2 | Denary |")
        print("| 3 | Hex    |")
        print("| 4 | Octal  |")
        print("| 5 | Exit   |")
        print("#---#--------#")
        print()
        baseOption2 = input("Enter 1 - 5: ")
    
        if int(baseOption2) not in range(1, 6):
            print("Invalid input. Please try again.")
            print()
            invalidInput = True
        elif int(baseOption2) == 5:
            print("Thank you for using the Number Converter! Terminating program...")
            exit()
        elif int(baseOption2) == int(baseOption1):
            print("You have selected the same base. Please try again.")
            print()
            invalidInput = True
        else:
            invalidInput = False
            print()
            outputString = f"Selected: {baseOptions[baseOption2]}"
            print("#" + (len(outputString) + 2) * "-", end = "#\n")
            print(f"| Selected: {baseOptions[baseOption2]} |")
            print("#" + (len(outputString) + 2) * "-", end = "#\n")
            print()
            
    outputString = f"Converting from base {baseOptions[baseOption1]} to base {baseOptions[baseOption2]}"
    print("#" + (len(outputString) + 2) * "-", end = "#\n")
    print(f"| Converting from base {baseOptions[baseOption1]} to base {baseOptions[baseOption2]} |")
    print("#" + (len(outputString) + 2) * "-", end = "#\n")
    
    print()
    
    tempDenNum = 0
    outputNum = ""
    inputNum = input(f"Enter a number in base {baseOptions[baseOption1]}: ")
    
    if baseOption1 == "1":
        if inputNum.count("0") + inputNum.count("1") != len(inputNum):
            print("Invalid input, binary number can only contain 1s and 0s. Please try again.")
            print()
            mainUI()
    elif baseOption1 == "2":
        if not inputNum.isdigit():
            print("Invalid input, denary number can only contain digits. Please try again.")
            print()
            mainUI()
    elif baseOption1 == "3":
        if inputNum.count("0") + inputNum.count("1") + inputNum.count("2") + inputNum.count("3") + inputNum.count("4") + inputNum.count("5") + inputNum.count("6") + inputNum.count("7") + inputNum.count("8") + inputNum.count("9") + inputNum.count("A") + inputNum.count("B") + inputNum.count("C") + inputNum.count("D") + inputNum.count("E") + inputNum.count("F") != len(inputNum):
            print("Invalid input, hexadecimal number can only contain digits and letters A - F. Please try again.")
            print()
            mainUI()
    elif baseOption1 == "4":
        if inputNum.count("0") + inputNum.count("1") + inputNum.count("2") + inputNum.count("3") + inputNum.count("4") + inputNum.count("5") + inputNum.count("6") + inputNum.count("7") != len(inputNum):
            print("Invalid input, octal number can only contain digits 0 - 7. Please try again.")
            print()
            mainUI()
        
    print()
    
    if baseOption1 == "1":
        tempDenNum = bin_to_den(inputNum)
    elif baseOption1 == "2":
        tempDenNum = int(inputNum)
    elif baseOption1 == "3":
        tempDenNum = any_to_den(inputNum, 16)
    elif baseOption1 == "4":
        tempDenNum = any_to_den(inputNum, 8)
        
    if baseOption2 == "1":
        outputNum = den_to_bin(tempDenNum)
    elif baseOption2 == "2":
        outputNum = str(tempDenNum)
    elif baseOption2 == "3":
        outputNum = den_to_any(tempDenNum, 16)
    elif baseOption2 == "4":
        outputNum = den_to_any(tempDenNum, 8)
    
    
    outputString = f"| Your number in base {baseOptions[baseOption2]} is: |"
    print("#" + (len(outputString) - 2) * "-" + "#-" + len(outputNum) * "-" + "-#")
    print(outputString + f" {outputNum} |")
    print("#" + (len(outputString) - 2) * "-" + "#-" + len(outputNum) * "-" + "-#")
    print()
    
    print("Thank you for using the Number Converter! Would you like to convert another number?")
    print()
    tryAgain = input("Enter Y to try again, or any other key to exit: ")
    
    if tryAgain.lower() == "y":
        print()
        mainUI()
    elif tryAgain.lower() != "y":
        print("Thank you for using the Number Converter! Terminating program...")
        exit()
    
mainUI()