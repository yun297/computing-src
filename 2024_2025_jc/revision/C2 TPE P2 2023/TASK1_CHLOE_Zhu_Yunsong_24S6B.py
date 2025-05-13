import socket
user = socket.socket()
user.connect(('127.0.0.1',3036))

print("Connected to server.")
nugget_count = 0

while True:
    data = b''
    while b'\n' not in data:
        data += user.recv(1024)
    msg = data.decode().strip()
    
    if msg == "end":
        print("You win")
        break
    else:
        nugget_count = int(msg)
        print(f"There are {nugget_count} nuggets left.")
    
        take_nuggets = int(input("How many to take? "))
        
        while take_nuggets > nugget_count and take_nuggets not in [1, 2, 3]:
            take_nuggets = int(input("How many to take? "))

    nugget_count -= take_nuggets
    
    if nugget_count == 0:
        user.sendall(b'end\n')
        print("You lose.")
        break
    else:
         user.sendall(f"{str(nugget_count)}\n".encode())