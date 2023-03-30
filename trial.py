import numpy as np
import numpy.random as rnd
import random


def SeatingStrat(type):
    list_order = []
    if type == "backtofront":
        for i in range(30, 0, -1):
            cols = [col+1 for col in range(6)]
            for seat in range(6):
                j = int(random.sample(cols, 1)[0])
                list_order.append((i,j))
                remove = cols.index(j)
                cols.pop(remove)
    elif type == "backtofrontzone":
        zone1_seats = []
        zone2_seats = []
        zone3_seats = []
        zone4_seats = []
        zone5_seats = []
        zone6_seats = []
        for row in [1, 2, 3, 4, 5]:
            for col in range(6):
                zone1_seats.append((row, col + 1))
        for row in [6, 7, 8, 9, 10]:
            for col in range(6):
                zone2_seats.append((row, col + 1))
        for row in [11, 12, 13, 14, 15]:
            for col in range(6):
                zone3_seats.append((row, col + 1))
        for row in [16, 17, 18, 19, 20]:
            for col in range(6):
                zone4_seats.append((row, col + 1))
        for row in [21, 22, 23, 24, 25]:
            for col in range(6):
                zone5_seats.append((row, col + 1))
        for row in [26, 27, 28, 29, 30]:
            for col in range(6):
                zone6_seats.append((row, col + 1))
        while bool(zone6_seats) is True:
            choice = random.sample(zone6_seats, 1)[0]
            remove = zone6_seats.index(choice)
            list_order.append(choice)
            zone6_seats.pop(remove)
        while bool(zone5_seats) is True:
            choice = random.sample(zone5_seats, 1)[0]
            remove = zone5_seats.index(choice)
            list_order.append(choice)
            zone5_seats.pop(remove)
        while bool(zone4_seats) is True:
            choice = random.sample(zone4_seats, 1)[0]
            remove = zone4_seats.index(choice)
            list_order.append(choice)
            zone4_seats.pop(remove)
        while bool(zone3_seats) is True:
            choice = random.sample(zone3_seats, 1)[0]
            remove = zone3_seats.index(choice)
            list_order.append(choice)
            zone3_seats.pop(remove)
        while bool(zone2_seats) is True:
            choice = random.sample(zone2_seats, 1)[0]
            remove = zone2_seats.index(choice)
            list_order.append(choice)
            zone2_seats.pop(remove)
        while bool(zone1_seats) is True:
            choice = random.sample(zone1_seats, 1)[0]
            remove = zone1_seats.index(choice)
            list_order.append(choice)
            zone1_seats.pop(remove)
    elif type == "outsidein":
        window_seats = []
        middle_seats = []
        aisle_seats = []
        for row in range(30):
            for col in [1,6]:
                window_seats.append((row + 1, col))
        for row in range(30):
            for col in [2,5]:
                middle_seats.append((row + 1, col))
        for row in range(30):
            for col in [3,4]:
                aisle_seats.append((row + 1, col))
        while bool(window_seats) is True:
            choice = random.sample(window_seats, 1)[0]
            remove = window_seats.index(choice)
            list_order.append(choice)
            window_seats.pop(remove)
        while bool(middle_seats) is True:
            choice = random.sample(middle_seats, 1)[0]
            remove = middle_seats.index(choice)
            list_order.append(choice)
            middle_seats.pop(remove)
        while bool(aisle_seats) is True:
            choice = random.sample(aisle_seats, 1)[0]
            remove = aisle_seats.index(choice)
            list_order.append(choice)
            aisle_seats.pop(remove)
    elif type == "rotatingzone":
        zone1_seats = []
        zone2_seats = []
        zone3_seats = []
        zone4_seats = []
        zone5_seats = []
        zone6_seats = []
        for row in [1,2,3,4,5]:
            for col in range(6):
                zone1_seats.append((row, col+1))
        for row in [6,7,8,9,10]:
            for col in range(6):
                zone2_seats.append((row, col+1))
        for row in [11,12,13,14,15]:
            for col in range(6):
                zone3_seats.append((row, col+1))
        for row in [16,17,18,19,20]:
            for col in range(6):
                zone4_seats.append((row, col+1))
        for row in [21,22,23,24,25]:
            for col in range(6):
                zone5_seats.append((row, col+1))
        for row in [26,27,28,29,30]:
            for col in range(6):
                zone6_seats.append((row, col+1))
        while bool(zone6_seats) is True:
            choice = random.sample(zone6_seats, 1)[0]
            remove = zone6_seats.index(choice)
            list_order.append(choice)
            zone6_seats.pop(remove)
        while bool(zone1_seats) is True:
            choice = random.sample(zone1_seats, 1)[0]
            remove = zone1_seats.index(choice)
            list_order.append(choice)
            zone1_seats.pop(remove)
        while bool(zone5_seats) is True:
            choice = random.sample(zone5_seats, 1)[0]
            remove = zone5_seats.index(choice)
            list_order.append(choice)
            zone5_seats.pop(remove)
        while bool(zone2_seats) is True:
            choice = random.sample(zone2_seats, 1)[0]
            remove = zone2_seats.index(choice)
            list_order.append(choice)
            zone2_seats.pop(remove)
        while bool(zone4_seats) is True:
            choice = random.sample(zone4_seats, 1)[0]
            remove = zone4_seats.index(choice)
            list_order.append(choice)
            zone4_seats.pop(remove)
        while bool(zone3_seats) is True:
            choice = random.sample(zone3_seats, 1)[0]
            remove = zone3_seats.index(choice)
            list_order.append(choice)
            zone3_seats.pop(remove)
    elif type == "optimal":
        for i in range(30, 0, -2):
            cols = [col+1 for col in range(6)]
            for seat in range(6):
                j = int(random.sample(cols, 1)[0])
                list_order.append((i,j))
                remove = cols.index(j)
                cols.pop(remove)
        for i in range(29, 0, -2):
            cols = [col+1 for col in range(6)]
            for seat in range(6):
                j = int(random.sample(cols, 1)[0])
                list_order.append((i,j))
                remove = cols.index(j)
                cols.pop(remove)
    elif type == "pracoptimal":
        for i in range(30, 0, -2):
            cols = [col+1 for col in range(3)]
            for seat in range(3):
                j = int(random.sample(cols, 1)[0])
                list_order.append((i,j))
                remove = cols.index(j)
                cols.pop(remove)
        for i in range(30, 0, -2):
            cols = [col+4 for col in range(3)]
            for seat in range(3):
                j = int(random.sample(cols, 1)[0])
                list_order.append((i,j))
                remove = cols.index(j)
                cols.pop(remove)
        for i in range(29, 0, -2):
            cols = [col+1 for col in range(3)]
            for seat in range(3):
                j = int(random.sample(cols, 1)[0])
                list_order.append((i,j))
                remove = cols.index(j)
                cols.pop(remove)
        for i in range(29, 0, -2):
            cols = [col+4 for col in range(3)]
            for seat in range(3):
                j = int(random.sample(cols, 1)[0])
                list_order.append((i,j))
                remove = cols.index(j)
                cols.pop(remove)
    elif type == "revpyramid":
        pass
    else:  # random
        seats = []
        for row in range(30):
            for col in range(6):
                seats.append((row+1, col+1))
        while bool(seats) is True:
            choice = random.sample(seats, 1)[0]
            remove = seats.index(choice)
            list_order.append(choice)
            seats.pop(remove)
    return list_order


print(SeatingStrat("random"))

print(SeatingStrat("outsidein"))

rows = [[(row+1,col+1) for col in range(6)] for row in range(30)]
#print(rows)
#print(random.randint(1, len(rows)))