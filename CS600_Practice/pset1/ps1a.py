###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    with open(filename) as f:
        cow_dict = {}
        for line in f:
            cow_name, cow_weight = line.split(',')
            cow_dict[cow_name] = int(cow_weight)
        return cow_dict
    

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_copy = cows.copy()
    trips = []
    while len(cows_copy) > 0:
        trip = []
        trip_weight = 0
        cows_copy_sorted = sorted(cows_copy.items(), key=lambda x: x[1], reverse=True)
        for cow in cows_copy_sorted:
            if trip_weight + cow[1] <= limit:
                trip.append(cow[0])
                trip_weight += cow[1]
                del cows_copy[cow[0]]
        trips.append(trip)
    return trips


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips = []
    for partition in get_partitions(cows):
        valid = True
        for trip in partition:
            trip_weight = 0
            for cow in trip:
                trip_weight += cows[cow]
            if trip_weight > limit:
                valid = False
                break
        if valid:
            trips.append(partition)
    trips_sorted = sorted(trips, key=lambda x: len(x))
    return trips_sorted[0]
        
# Problem 4
def compare_cow_transport_algorithms(file_name="ps1_cow_data.txt", limit=10):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows(file_name)
    start = time.time()
    print(greedy_cow_transport(cows, limit))
    end = time.time()
    print(end - start)
    start = time.time()
    print(brute_force_cow_transport(cows, limit))
    end = time.time()
    print(end - start)
    
if __name__ == "__main__":
    compare_cow_transport_algorithms(limit=15)

