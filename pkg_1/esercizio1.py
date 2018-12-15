from Airport import *
from Flight import *
from typing import List,Dict
from datetime import datetime
from TdP_collections.queue.array_queue import ArrayQueue
from utils import read_from_file

def backtrack(arrival_time,departure_time,min_waiting,cost,total):
    if cost <= total and arrival_time + min_waiting <= departure_time:
        return True
    else:
        return False


"""def simply_list_routes(flights :Dict[Flight],start :Airport,b :Airport,t,T :int,solution,actual_cost,paths):
    if start == b:
        paths.append(solution)
    else:
        for flight in flights[start]:
            cost = actual_cost + (l(flight) - a(start) + a(flight) - l(flight))  # finora + attesa + volo
            if backtrack(a(start), l(flight), c(d(start)), cost, T):
                simply_list_routes(flights,d(start),b,T,solution + [flight],cost,paths)
"""


def list_routes(flights :List[Flight],start :Airport,b :Airport,t,T :int):
    queue = ArrayQueue()
    paths = {}

    # Construction
    flights_tmp = dict()
    for flight in flights:
        if s(flight) in flights_tmp:
            flights_tmp[s(flight)].append(flight)
        else:
            flights_tmp[s(flight)] = [flight]

    # Init the queue
    i = 0
    for flight in flights_tmp[start]:
        cost = (c(start)+ a(flight) - l(flight))
        if backtrack(t,l(flight),0,cost,T):
            queue.enqueue((i,flight,cost))
            paths[i] = []
            # print(str(i), str(flight), cost)
            i+=1


    while not queue.is_empty():
        begin, my_flight, time_elapsed = queue.dequeue()
        paths[begin].append(my_flight)
        # print("ITERATION "+str(time_elapsed))
        if d(my_flight) != b:
            item = paths.pop(begin)
            j = len(paths)
            for flight in flights_tmp[d(my_flight)]:
                cost = time_elapsed + (l(flight) - a(my_flight) + a(flight) - l(flight)) # finora + attesa + volo
                if backtrack(a(my_flight),l(flight),c(d(my_flight)),cost,T):
                    queue.enqueue((j,flight,cost))
                    paths[j] = item + []
                    # print(str(j), str(flight), cost)
                    # print("DURATA VOLO - ", a(flight) - l(flight))
                    # print("DURATA ATTESA - ", l(flight) - a(my_flight))
                    j += 1

    return paths


if __name__ == "__main__":

    airports,flights=read_from_file("test1")

    """for airport in airports:
        print(airport)

    for flight in flights:
        print(flight)"""

    start = airports[0]
    end = airports[3]
    starting_time = datetime.strptime("12:00", "%H:%M").time()
    total_time = datetime.strptime("12:00", "%H:%M").time()

    start_time_minutes = starting_time.hour*60 + starting_time.minute
    total_time_minutes = total_time.hour*60 + total_time.minute

    paths = list_routes(flights,start,end,start_time_minutes,total_time_minutes)

    print("\n\nPercorsi da "+str(start)+" a "+str(end)+" in "+str(total_time_minutes)+" minuti ")
    print("Partenza alle "+str(starting_time))

    for path in paths.keys():
        print("--------------PATH----------- "+str(path))
        for flight in paths[path]:
            print(str(flight))
