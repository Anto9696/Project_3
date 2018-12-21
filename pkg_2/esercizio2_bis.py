from Airport import *
from Flight import *
from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from utils import *
from typing import Dict,List
from datetime import datetime

def find_route(airports :List[Airport],flights :Dict, start :Airport,b :Airport,t):
    cost = {}
    cloud = {}
    git  = []
    queue = AdaptableHeapPriorityQueue()

    for airport in airports:
        cost[airport] = [float('inf'),queue.add(float('inf'),(airport,None,t))]

    cost[start][0] = 0
    queue.update(cost[start][1], 0, (start,None,t))

    while not queue.is_empty():
        _,(airport,flight_last,arrival_time) = queue.remove_min()
        cloud[airport] = flight_last
        for flight in flights[airport]:
            if d(flight) not in cloud and arrival_time + c(airport) <= l(flight):
                cost[d(flight)][0] = min(cost[d(flight)][0],cost[airport][0] + l(flight) - arrival_time + a(flight) - l(flight))
                queue.update(cost[d(flight)][1],cost[d(flight)][0],(d(flight),flight,a(flight)))

    my_flight = cloud[b]
    while my_flight is not None:
        path.insert(0,my_flight)
        my_flight = cloud[s(my_flight)]

    return path,cost[b][0]


if __name__=="__main__":
    airports, flights = read_from_file("test2.txt")

    flights_dict = dict()
    for flight in flights:
        if s(flight) in flights_dict:
            flights_dict[s(flight)].append(flight)
        else:
            flights_dict[s(flight)] = [flight]

    start = airports[0]
    end = airports[3]
    starting_time = datetime.strptime("12:00", "%H:%M").time()
    starting_time_minutes = starting_time.hour*60+starting_time.minute

    path,time = find_route(airports,flights_dict,start,end,starting_time_minutes)

    print("Percorso migliore da {0} a {1} con partenza alle {2}".format(start,end,starting_time))
    print("Durata "+str(time))
    for flight in path:
        print(flight)