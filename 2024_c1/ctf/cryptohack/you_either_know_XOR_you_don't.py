from pwn import xor

hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

key = xor(bytes.fromhex(hex), "myXORkey".encode())

print(key)