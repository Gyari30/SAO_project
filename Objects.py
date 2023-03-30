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
    
    
# !!!!!!!!!!!!!!!!!!!!!!!!!!! FROM HERE THE CODE DEVIATES FROM DAVID'S LATEST PUBLISH ON 30/03   !!!!!!!!!!!!!!!!!!!!!!!!!!! 
    
    
def PassengerGenerator(ID, row, seat):
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
        "board_time_cum": None,
        "time_entrance": None,
        "time_seated": None,
        "row": row,
        "seat": seat,
        "has_luggage": has_luggage,
        "walkspeed": {'aisle_begin' : size_aisle_begin/walkspeed,
                      'aisle_seats' : size_aisle_seats/walkspeed},
        "aisle_pos": None,
        "seated": False,
        "ID": ID,
        "timespent": {
            "entrance": enter_time,
            "walking": walking_time,
            "waiting": 0,
            "luggage_stash": luggage_stash,
            "seating_time": 0,
            "standup": 0,
            
        }
    }
    return dict_res


def New_arrival(passengers, aisle, current_time):
    # If the first position in the aisle is vacant, give that position to the first passenger 
    # in the passengers that had not yet been assigned a spot in the aisle.
    if bool(aisle[0]):
        print('Aisle is fully occupied, no new passenger can enter. THIS SHOULD NOT OCCUR')
    for i in range(len(passengers)):
        if passengers[i]['aisle_pos']==None:
            while aisle[0] == 0:
                passengers[i]['aisle_pos'] = 0
                passengers[i]['Time_entrance'] = current_time
                aisle[0] = 1
                # Make a new entry for the passenger in the event list
                pass_event = Passenger_event(passengers[i]['ID'], passengers[i]['walkspeed']['aisle_begin'])
                events.append(pass_event)

def Passenger_event(ID, timer):
    return{'ID': ID, 'timer' : timer,}




# Magic numbers

# Number of seat rows on the plane
nrows = 30
# Seats per row
nseats = 6
# Total length of the aisle
l_aisle = 35

# The space occupied on the aisle is larger next to the seats than on the first part.
size_aisle_seats = 0.7112
size_aisle_begin = 0.4572





# Initialization

# Initializing passengers       (should make a function out of this)
# Big change: save the passengers as a separate list that is created a priori. 
# This process defines the boarding strategies, here a super stupid one is taken for coding simplicity.
passengers = []
ID=0
for i in range(nrows):
    for q in range(nseats):
        ID+=1
        passengers.append(PassengerGenerator(ID, i+1, q+1))
        


# Initializing the aisle
# The aisle is a binary vector, where '1' designates occupancy and '0' vacancy.
aisle = np.zeros(l_aisle)



# Initializing global time
current_time = 0



# Initializing the event list. At first the only active event is that of the next arrival.
# As passengers enter the plane, they too get their separate event.
events = [{'ID': 'Arrival', 'timer' : random.expovariate(0.5)}]



#########################################################
# Identifying the next event 

min_timer = min(events, key = lambda x: x['timer'])['timer']    # Find the time to the next event

# Retrieve the event list index of the next event (by matching the smallest timer)
action_index = next((index for (index, d) in enumerate(events) if d["timer"] == min_timer), None) 

current_time = current_time + min_timer # Update current time

for i in range(len(events)):          # Update the other event timers.
    events[i]['timer'] = events[i]['timer'] - min_timer
    
    
    
# Executing next event

# First we define what happens if the event is a new arrival
if events[action_index]['ID'] == 'Arrival':
    # In case the first spot on the aisle is occupied, the arrival is delayed.
    if bool(aisle[0]):
        events[action_index]['timer'] = 1   # Setting the delay arbitrarily to 1 second, NEED TO DISCUSS AND UPDATE.
    else:
        events[action_index]['timer'] = random.expovariate(0.5) # Otherwise draw from an exp. distribution with mean 2 ALSO NEED TO DISCUSS.
        New_arrival(passengers, aisle, current_time)    # And let the new passenger arrive.
    # If all passengers are in the plane, remove the arrival event from the event list.        
    if all(d['aisle_pos'] is not None for d in passengers):
        del events[action_index]
    
else: # If we are not dealing with a new arrival, we must be dealing with a passenger.

    # Designate the passenger that is going to move.
    pass_index = next((index for (index, d) in enumerate(passengers) if d["ID"] == events[action_index]['ID']), None)
    
    # First we check if the passenger has been seated. If so, we remove the passenger from the event list
    if passengers[pass_index]['seated'] == True:
        del events[action_index]
        print(f"Passenger {passengers[pass_index]['ID']} has been seated!")
    else:    
    
        aisle_position = passengers[pass_index]['aisle_pos']    # Retrieve his position on the aisle.
        
        # If the next space on the aisle is occupied, the passenger needs to wait.
        # The way it is coded here, the waiting time is basically the movement resetting. I think this is the right way to go.
        if bool(aisle[aisle_position + 1]):
            # Taking into account smaller tiles at the beginning of the aisle.
            if aisle_position < l_aisle - nrows:    
                # Schedule next movement.
                events[action_index]['timer'] = passengers[pass_index]['walkspeed']['aisle_begin']
                # Update waiting time.
                passengers[pass_index]['timespent']['waiting'] = passengers[pass_index]['timespent']['waiting'] + passengers[pass_index]['walkspeed']['aisle_begin']
            # Now for the larger aisle tiles at the seats.
            else:           
                events[action_index]['timer'] = passengers[pass_index]['walkspeed']['aisle_seats']
                passengers[pass_index]['timespent']['waiting'] = passengers[pass_index]['timespent']['waiting'] + passengers[pass_index]['walkspeed']['aisle_seats']
        
        # If the next space on the aisle is vacant, the passenger moves.
        else:
            aisle[aisle_position] = 0
            aisle[aisle_position + 1] = 1
            passengers[pass_index]['aisle_pos'] = aisle_position + 1
            
            # If he has not arrived at his row number yet, we simply schedule his next movement.
            if not passengers[pass_index]['aisle_pos'] == passengers[pass_index]['row']:
                # Again accounting for different tile sizes. Some duplicate code cannot be avoided here.
                if aisle_position < l_aisle - nrows:    
                    events[action_index]['timer'] = passengers[pass_index]['walkspeed']['aisle_begin']
                else: 
                    events[action_index]['timer'] = passengers[pass_index]['walkspeed']['aisle_seats']
            
            # Now for something very important: if the passenger arrives at the row of his seat he needs to sit!!!!!! FCKKKK
            else:
                # !!!!!!!!!!!!!!!!!!!       READ LINE BELOW     !!!!!!!!!!!!!!!!!!!
                # The SeatingManager function needs to be updated such that it returns the time it takes for the passenger to get seated.
                # This means that the SeatingManager also needs to incorporate luggage delay.
                # events[action_index]['timer'] = SeatingManager(passengers[pass_index], seating_matrix)
                passengers[pass_index]['seated'] == True





