from binascii import unhexlify

# Given hex-encoded string
hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# Decode hex string to bytes
byte_data = unhexlify(hex_string)

# Iterate over all possible single byte keys (0 to 255)
for key in range(256):
    # XOR each byte with the current key
    decoded_bytes = bytes([b ^ key for b in byte_data])
    try:
        # Try to decode the resulting bytes to a string
        decoded_string = decoded_bytes.decode('utf-8')
        # If successful, print the key and the decoded string
        print(f"Key: {key}, Decoded String: {decoded_string}")
    except UnicodeDecodeError:
        # If decoding fails, just skip this key
        continue
