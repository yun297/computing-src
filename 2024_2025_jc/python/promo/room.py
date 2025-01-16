import random

def generate_room():
    room = []

    for i in range(10):
        row = []
        for j in range(10):
            row.append(random.choice([0, 1]))
            
        room.append(row)

    return room

def count_occupied(room):
    count = 0
    for i in room:
        for j in i:
            if j == 1:
                count += 1
    
    return count

room = [
    [1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 1]
] # full column: 2, 5

def count_full_cols(room):
    col_sums = [0] * 10

    for i in room:
        for j in range(len(i)):
            col_sums[j] += i[j]
            
    full_cols = []

    for i in range(len(col_sums)):
        if col_sums[i] == 10:
            full_cols.append(i)
            
    return full_cols

def count_full_rows(room):
    full_rows = []

    for i in range(len(room)):
        if 0 not in room[i]:
            full_rows.append(i)
            
    return full_rows

# print(count_full_cols(room)) # [2, 5]

# room1 = generate_room()

# print(count_full_cols(room1)) # []

def check_main_diag(room):
    for i in range(len(room)):
        if room[i][i] == 0:
            return False

    return True

def check_anti_diag(room):
    for i in range(len(room)):
        if room[i][9 - i] == 0:
            return False

    return True