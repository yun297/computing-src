from binascii import unhexlify
from pwn import xor

# Given hex values
key1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key2_key1_hex = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_key3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_key1_key3_key2_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# Convert hex to bytes
key1 = unhexlify(key1_hex)
key2_key1 = unhexlify(key2_key1_hex)
key2_key3 = unhexlify(key2_key3_hex)
flag_key1_key3_key2 = unhexlify(flag_key1_key3_key2_hex)

# Calculate KEY2 by XORing key2_key1 with key1
key2 = xor(key2_key1, key1)

# Calculate KEY3 by XORing key2_key3 with key2
key3 = xor(key2_key3, key2)

# Calculate FLAG by XORing flag_key1_key3_key2 with key1, key3, and key2
flag = xor(flag_key1_key3_key2, key1, key3, key2)

# Print the FLAG in the required format
print(flag.decode())
