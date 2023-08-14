import random


def get_mapping():
    f = open("ship_class_mapping.txt", "r")
    data = f.read().split("\n")[1:]
    f.close()

    data = list(map(lambda row: row.split(", "), data))
    ship_class_mapping = dict(
        map(lambda row: (row[0], (row[1], int(row[2]))), data))
    return ship_class_mapping


ship_class_mapping = get_mapping()
print(get_mapping())


# your code here
