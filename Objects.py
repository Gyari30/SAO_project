import numpy as np
import numpy.random as rnd
import random


def BoardingStrat(type):
    list_order = []
    if type == "backtofront":
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
        zone1_seats = []
        zone2_seats = []
        zone3_seats = []
        zone4_seats = []
        zone5_seats = []
        zone6_seats = []
        zone7_seats = []
        zone8_seats = []
        zone9_seats = []
        zone10_seats = []
        zone11_seats = []
        zone12_seats = []
        for row in range(30, 0, -2):
            zone1_seats.append((row, 1))
        for row in range(30, 0, -2):
            zone2_seats.append((row, 6))
        for row in range(29, 0, -2):
            zone3_seats.append((row, 1))
        for row in range(29, 0, -2):
            zone4_seats.append((row, 6))
        for row in range(30, 0, -2):
            zone5_seats.append((row, 2))
        for row in range(30, 0, -2):
            zone6_seats.append((row, 5))
        for row in range(29, 0, -2):
            zone7_seats.append((row, 2))
        for row in range(29, 0, -2):
            zone8_seats.append((row, 5))
        for row in range(30, 0, -2):
            zone9_seats.append((row, 3))
        for row in range(30, 0, -2):
            zone10_seats.append((row, 4))
        for row in range(29, 0, -2):
            zone11_seats.append((row, 3))
        for row in range(29, 0, -2):
            zone12_seats.append((row, 4))
        while bool(zone1_seats) is True:
            choice = random.sample(zone1_seats, 1)[0]
            remove = zone1_seats.index(choice)
            list_order.append(choice)
            zone1_seats.pop(remove)
        while bool(zone2_seats) is True:
            choice = random.sample(zone2_seats, 1)[0]
            remove = zone2_seats.index(choice)
            list_order.append(choice)
            zone2_seats.pop(remove)
        while bool(zone3_seats) is True:
            choice = random.sample(zone3_seats, 1)[0]
            remove = zone3_seats.index(choice)
            list_order.append(choice)
            zone3_seats.pop(remove)
        while bool(zone4_seats) is True:
            choice = random.sample(zone4_seats, 1)[0]
            remove = zone4_seats.index(choice)
            list_order.append(choice)
            zone4_seats.pop(remove)
        while bool(zone5_seats) is True:
            choice = random.sample(zone5_seats, 1)[0]
            remove = zone5_seats.index(choice)
            list_order.append(choice)
            zone5_seats.pop(remove)
        while bool(zone6_seats) is True:
            choice = random.sample(zone6_seats, 1)[0]
            remove = zone6_seats.index(choice)
            list_order.append(choice)
            zone6_seats.pop(remove)
        while bool(zone7_seats) is True:
            choice = random.sample(zone7_seats, 1)[0]
            remove = zone7_seats.index(choice)
            list_order.append(choice)
            zone7_seats.pop(remove)
        while bool(zone8_seats) is True:
            choice = random.sample(zone8_seats, 1)[0]
            remove = zone8_seats.index(choice)
            list_order.append(choice)
            zone8_seats.pop(remove)
        while bool(zone9_seats) is True:
            choice = random.sample(zone9_seats, 1)[0]
            remove = zone9_seats.index(choice)
            list_order.append(choice)
            zone9_seats.pop(remove)
        while bool(zone10_seats) is True:
            choice = random.sample(zone10_seats, 1)[0]
            remove = zone10_seats.index(choice)
            list_order.append(choice)
            zone10_seats.pop(remove)
        while bool(zone11_seats) is True:
            choice = random.sample(zone11_seats, 1)[0]
            remove = zone11_seats.index(choice)
            list_order.append(choice)
            zone11_seats.pop(remove)
        while bool(zone12_seats) is True:
            choice = random.sample(zone12_seats, 1)[0]
            remove = zone12_seats.index(choice)
            list_order.append(choice)
            zone12_seats.pop(remove)
    elif type == "pracoptimal":
        zone1_seats = []
        zone2_seats = []
        zone3_seats = []
        zone4_seats = []
        for row in range(30, 0, -2):
            for col in [1, 2, 3]:
                zone1_seats.append((row, col))
        for row in range(30, 0, -2):
            for col in [4, 5, 6]:
                zone2_seats.append((row, col))
        for row in range(29, 0, -2):
            for col in [1, 2, 3]:
                zone3_seats.append((row, col))
        for row in range(29, 0, -2):
            for col in [4, 5, 6]:
                zone4_seats.append((row, col))
        while bool(zone1_seats) is True:
            choice = random.sample(zone1_seats, 1)[0]
            remove = zone1_seats.index(choice)
            list_order.append(choice)
            zone1_seats.pop(remove)
        while bool(zone2_seats) is True:
            choice = random.sample(zone2_seats, 1)[0]
            remove = zone2_seats.index(choice)
            list_order.append(choice)
            zone2_seats.pop(remove)
        while bool(zone3_seats) is True:
            choice = random.sample(zone3_seats, 1)[0]
            remove = zone3_seats.index(choice)
            list_order.append(choice)
            zone3_seats.pop(remove)
        while bool(zone4_seats) is True:
            choice = random.sample(zone4_seats, 1)[0]
            remove = zone4_seats.index(choice)
            list_order.append(choice)
            zone4_seats.pop(remove)
    elif type == "revpyramid":
        zone1_seats = []
        zone2_seats = []
        zone3_seats = []
        zone4_seats = []
        zone5_seats = []
        zone6_seats = []
        # Zone 1
        for row in range(15, 30):
            for col in [1, 6]:
                zone1_seats.append((row + 1, col))
        # Zone 2
        for row in range(7, 15):
            for col in [1, 6]:
                zone2_seats.append((row + 1, col))
        for row in range(23, 30):
            for col in [2, 5]:
                zone2_seats.append((row + 1, col))
        # Zone 3
        for row in range(0, 7):
            for col in [1, 6]:
                zone3_seats.append((row + 1, col))
        for row in range(15, 23):
            for col in [2, 5]:
                zone3_seats.append((row + 1, col))
        # Zone 4
        for row in range(23, 30):
            for col in [3, 4]:
                zone4_seats.append((row + 1, col))
        for row in range(7, 15):
            for col in [2, 5]:
                zone4_seats.append((row + 1, col))
        # Zone 5
        for row in range(0, 7):
            for col in [2, 5]:
                zone5_seats.append((row + 1, col))
        for row in range(15, 23):
            for col in [3, 4]:
                zone5_seats.append((row + 1, col))
        # Zone 6
        for row in range(0, 15):
            for col in [3, 4]:
                zone6_seats.append((row + 1, col))
        while bool(zone1_seats) is True:
            choice = random.sample(zone1_seats, 1)[0]
            remove = zone1_seats.index(choice)
            list_order.append(choice)
            zone1_seats.pop(remove)
        while bool(zone2_seats) is True:
            choice = random.sample(zone2_seats, 1)[0]
            remove = zone2_seats.index(choice)
            list_order.append(choice)
            zone2_seats.pop(remove)
        while bool(zone3_seats) is True:
            choice = random.sample(zone3_seats, 1)[0]
            remove = zone3_seats.index(choice)
            list_order.append(choice)
            zone3_seats.pop(remove)
        while bool(zone4_seats) is True:
            choice = random.sample(zone4_seats, 1)[0]
            remove = zone4_seats.index(choice)
            list_order.append(choice)
            zone4_seats.pop(remove)
        while bool(zone5_seats) is True:
            choice = random.sample(zone5_seats, 1)[0]
            remove = zone5_seats.index(choice)
            list_order.append(choice)
            zone5_seats.pop(remove)
        while bool(zone6_seats) is True:
            choice = random.sample(zone6_seats, 1)[0]
            remove = zone6_seats.index(choice)
            list_order.append(choice)
            zone6_seats.pop(remove)
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


# IF IT DOES NOT WORK WITH DICTIONARIES, WE NEED TO CODE THIS AS AN OBJECT
def PassengerGenerator(deltaT, row, seat):
    # Simulated parameters
    enter_time = random.uniform(1, 5)  # time spent by lining up and entering the airplane
    has_luggage = rnd.choice((1, 0), p=[0.8, 0.2])  # logical if person has a luggage (1-yes, 0-no)
    if has_luggage==1:
        luggage_stash = random.uniform(6, 30)  # seconds spent with luggage stash
    else:
        luggage_stash = 0
    walkspeed = random.uniform(0.27, 0.44)  # meter per second

    # Calculated attributes and containing these attributes
    walking_time = (0.7112/walkspeed) * (row + 3)
    dict_res = {
        "board_time_cum": 0,
        "pass_start_relative": deltaT,
        "pass_end_relative": deltaT,
        "row_arrival_relative": deltaT,
        "row": row,
        "seat": seat,
        "has_luggage": has_luggage,
        "walkspeed": walkspeed,
        "unit_walktime": 0.7112/walkspeed,
        "aisle_pos": 0,
        "timespent": {
            "entrance": enter_time,
            "walking": walking_time,
            "waiting": 0,
            "luggage_stash": luggage_stash,
            "seating_time": 0,
            "standup": 0
        }
    }
    return dict_res


def SeatingManager(arriving_passenger, seating_matrix):
    seat = arriving_passenger["seat"]
    row = arriving_passenger["row"]
    if seat==3 or seat==4:
        # Arriving has aisle seat
        aisle_seating = random.uniform(2, 5)  # Aisle seating time (aisle can be taken regardless of people already sitting in the row
        arriving_passenger["timespent"]["seating_time"] += aisle_seating
    elif seat==2 or seat==5:
        # Arriving has middle seat
        if seat==2:
            target_seat = 3
        else:
            target_seat = 4
        if bool(seating_matrix[row-1][target_seat-1]) is True:
            # Aisle seat is taken
            aisle_seating = random.uniform(2, 5)  # Standup time of the person in the aisle seat
            middle_seating = random.uniform(3, 6)  # middle seating time
            seating_matrix[row-1][target_seat-1]["timespent"]["standup"] += aisle_seating*2 + middle_seating
            arriving_passenger["timespent"]["seating_time"] += middle_seating+aisle_seating
        else:
            middle_seating = random.uniform(3, 6)  # middle seating time
            arriving_passenger["timespent"]["seating_time"] += middle_seating
    else:
        # Arriving has window seat
        if seat==1:
            target_middle = 2
            target_aisle = 3
        else:
            target_middle = 5
            target_aisle = 4
        if bool(seating_matrix[row - 1][target_aisle - 1]) is True:
            if bool(seating_matrix[row - 1][target_middle - 1]) is True:
                # Both aisle and middle are taken
                aisle_seating = random.uniform(2, 5)  # Standup time of the person in the aisle seat
                middle_seating = random.uniform(3, 6)  # Standup time of the person in the middle seat
                window_seating = random.uniform(4, 7)  # window seating time
                arriving_passenger["timespent"]["seating_time"] += window_seating + aisle_seating + middle_seating
                seating_matrix[row - 1][target_aisle - 1]["timespent"]["standup"] += aisle_seating*2 + middle_seating*2 + window_seating
                seating_matrix[row - 1][target_middle - 1]["timespent"]["standup"] += middle_seating * 2 + window_seating
            else:
                # Only aisle seat is taken
                aisle_seating = random.uniform(2, 5)  # Standup time of the person in the aisle seat
                window_seating = random.uniform(4, 7)  # window seating time
                seating_matrix[row - 1][target_aisle - 1]["timespent"]["standup"] += aisle_seating * 2 + window_seating
                arriving_passenger["timespent"]["seating_time"] += window_seating + aisle_seating
        else:
            if bool(seating_matrix[row - 1][target_middle - 1]) is True:
                # Only middle seat is taken
                middle_seating = random.uniform(3, 6)  # Standup time of the person in the middle seat
                window_seating = random.uniform(4, 7)  # window seating time
                seating_matrix[row - 1][target_middle - 1]["timespent"]["standup"] += middle_seating * 2 + window_seating
                arriving_passenger["timespent"]["seating_time"] += window_seating + middle_seating
            else:
                window_seating = random.uniform(4, 7)  # window seating time
                arriving_passenger["timespent"]["seating_time"] += window_seating
    # Sum up the boarding times
    passenger_totaltime = arriving_passenger["timespent"]["seating_time"] + arriving_passenger["timespent"]["luggage_stash"] + arriving_passenger["timespent"]["entrance"] + arriving_passenger["timespent"]["walking"] + arriving_passenger["timespent"]["waiting"]
    arriving_passenger["pass_end_relative"] += passenger_totaltime
    arriving_passenger["board_time_cum"] = passenger_totaltime
    # Seat the arriving into seating matrix
    seating_matrix[row - 1][seat - 1] = arriving_passenger
    # Seating completed


def WalkingImplement(aisle, ind_from, ind_to):
    passenger = aisle[ind_from][0]
    passenger["aisle_pos"] = ind_to
    walktime = passenger["unit_walktime"]
    aisle[ind_to][0] = passenger
    aisle[ind_from][0] = {}
    return aisle, walktime


def AisleManager(type):
    # Initialization
    aisle = np.full((34, 1), {})
    arrival_queue = BoardingStrat(type)
    TIME = 0
    # Initial boarding of first passenger
    aisle[0][0] = PassengerGenerator(TIME, arrival_queue[0][0], arrival_queue[0][1])
    aisle, walktime = WalkingImplement(aisle, 0, 1)
    TIME += aisle[0][0]["timespent"]["entrance"] + walktime
    arrival_queue.pop(0)

    return None


AisleManager("random")




# Initialization and magic numbers
aisle = np.full((35,1), {})
print(aisle[34][0])

aisle[20] = PassengerGenerator(2, 24, 3)
#print(aisle)

seating_matrix = np.full((30,6), {})

enter_time = random.randrange(1,6)
#print(enter_time)

walkspeed = random.uniform(0.27, 0.44)  # meter per second
#print(walkspeed)

lsit = [[2,3,4],
        [3,4,5],
        [4,5,6]]

#print(lsit[1][1])

t = [{}, {"e": 1}, {}]
#print(bool(t[0]))
#print(bool(t[1]))
#print(bool(t[2]))