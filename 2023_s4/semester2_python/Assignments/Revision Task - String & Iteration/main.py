def fooDNA(s1, s2):
    pairings = {
        "A": "T",
        "G": "C",
        "T": "A",
        "C": "G"
    }

    for i in range(len(s1)):
        nuc1 = s1[i]
        nuc2 = s2[i]
        if pairings[nuc1] != nuc2:
            return False

    return True


def foo15(s):
    for i in range(len(s)):
        tempSum = 0
        count = i
        while tempSum <= 15 and count < len(s):
            tempSum += int(s[count])
            count += 1
            if tempSum == 15:
                return True
    return False


def fooSPR(P1, P2):
    score = 0
    for i in range(len(P1)):
        if P1[i] == "P" and P2[i] == "R":
            score += 1
        elif P1[i] == "R" and P2[i] == "S":
            score += 1
        elif P1[i] == "S" and P2[i] == "P":
            score += 1
        elif P2[i] == "P" and P1[i] == "R":
            score -= 1
        elif P2[i] == "R" and P1[i] == "S":
            score -= 1
        elif P2[i] == "S" and P1[i] == "P":
            score -= 1
    
    if score > 0:
        return "Player 1"
    elif score < 0:
        return "Player 2"
    elif score == 0:
        return "Draw"

# print(fooSPR("P","S"))

def fooSum2digits(s):
    temp = 0
    for i in range(2, len(s)):
        temp = int(s[i-1]) + int(s[i-2])
        if temp % 10 == int(s[i]):
            pass
        else:
            return False
    return True

# print(fooSum2digits("123583145"))

def encrypt(s):
    encoded = ""
    for char in s:
        encoded_char = chr((ord(char) - 65 + 3) % 26 + 65)
        encoded += encoded_char
    return encoded

def decrypt(s):
    decoded = ""
    for char in s:
        decoded_char = chr((ord(char) - 65 - 3) % 26 + 65)
        decoded += decoded_char
    return decoded

def is_saw_teeth(s):
    for i in range(1, len(s) - 1, 2):
        if (int(s[i]) > int(s[i - 1]) and int(s[i]) > int(s[i + 1])) or (int(s[i]) < int(s[i - 1]) and int(s[i]) < int(s[i + 1])):
            continue
        else:
            return False
    return True

def bin_to_dec(s):
    dec = 0
    for i in range(len(s)):
        if s[i] == "1":
            dec += int(2 ** (len(s) - i - 1))
    return dec