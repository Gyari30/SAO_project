import numpy as np
import numpy.random as rnd
import random


def SeatingStrat(type):
    list_order = []
    if type == "backtofront":
        for i in range(30, -1):
            print(i)
    elif type == "outsidein":
        pass
    elif type == "rotatingzone":
        pass
    elif type == "optimal":
        pass
    elif type == "pracoptimal":
        pass
    elif type == "revpyramid":
        pass
    else:  # random
        pass
    return None


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
    walking_time = (0.7112/walkspeed) * row + 4*(0.4572/walkspeed)
    dict_res = {
        "board_time_cum": 0,
        "pass_start_relative": deltaT,
        "pass_end_relative": deltaT,
        "row_arrival_relative": deltaT,
        "row": row,
        "seat": seat,
        "has_luggage": has_luggage,
        "walkspeed": walkspeed,
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
    # Seat the arriving into seating matrix
    seating_matrix[row - 1][seat - 1] = arriving_passenger
    # Seating completed


def AisleManager(aisle):
    return None

# Initialization and magic numbers
aisle = np.full((35,1), {})
print(aisle)

aisle[20] = PassengerGenerator(2, 24, 3)
print(aisle)

seating_matrix = np.full((30,6), {})

enter_time = random.randrange(1,6)
print(enter_time)

walkspeed = random.uniform(0.27, 0.44)  # meter per second
print(walkspeed)

lsit = [[2,3,4],
        [3,4,5],
        [4,5,6]]

print(lsit[1][1])

t = [{}, {"e": 1}, {}]
print(bool(t[0]))
print(bool(t[1]))
print(bool(t[2]))