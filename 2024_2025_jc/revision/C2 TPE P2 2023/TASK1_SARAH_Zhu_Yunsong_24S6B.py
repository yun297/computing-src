import socket
my_socket = socket.socket()
my_socket.bind(('127.0.0.1',3036))
my_socket.listen()
user, addr = my_socket.accept()

print(f"Connected to client on {addr}.")

# Sarah states the number
nugget_count = int(input("How many nuggets? "))
# user.sendall(f"{str(nugget_count)}\n".encode())

while True:
    if nugget_count == 0:
        user.sendall(b'end\n')
        print("You lose.")
        break
    else:
        user.sendall(f"{str(nugget_count)}\n".encode())

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

# Complete the program  