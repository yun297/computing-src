plaintext = "ATTACK HCI FROM THE EAST AT EIGHT"
key = 3

def encrypt(input, key):
    encrypted = ""
    for char in input:
        if ord(char) >= ord("A") and ord(char) <= ord("Z"):
            if ord(char) + key >= ord("Z"):
                encrypted += chr(ord(char) + key - 26)
            else:
                encrypted += chr(ord(char) + key)
        else:
            encrypted += char
        
    return encrypted

def decrypt(input, key):
    decrypted = ""
    for char in input:
        if ord(char) >= ord("A") and ord(char) <= ord("Z"):
            if ord(char) - key < ord("A"):
                decrypted += chr(ord(char) - key + 26)
            else:
                decrypted += chr(ord(char) - key)
        else:
            decrypted += char
        
    return decrypted
    
print(decrypt("ynkooejcpdanqxeykjrbdofgkq", 3))