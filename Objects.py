import numpy as np
import numpy.random as rnd
import random

def PassengerGenerator(deltaT, row, seat):
    # Simulated parameters
    enter_time = random.uniform(1, 5) # time spent by lining up and entering the airplane
    has_luggage = rnd.choice((1, 0), p=[0.8, 0.2]) # logical if person has a luggage (1-yes, 0-no)
    if has_luggage==1:
        luggage_stash = random.uniform(6, 30) # seconds spent with luggage stash
    else:
        luggage_stash = 0
    walkspeed = random.uniform(0.27, 0.44) # meter per second

    # Calculated attributes and containing these attributes
    walking_time = (0.7112/walkspeed) * row + 4*(0.4572/walkspeed)
    dict_res = {
        "board_time_cum": 0,
        "pass_start_relative": deltaT,
        "pass_end_relative": deltaT,
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
            "seating_time": 0
        }
    }
    return dict_res




enter_time = random.randrange(1,6)
print(enter_time)

walkspeed = random.uniform(0.27, 0.44) # meter per second
print(walkspeed)

