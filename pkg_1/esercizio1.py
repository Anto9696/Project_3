from Airport import *
from Flight import *
from typing import List,Dict
# from datetime import datetime
# from TdP_collections.stack.array_stack import ArrayStack
# from utils import read_from_file

def backtrack(arrival_time,departure_time,min_waiting,cost,total):
    if cost <= total and arrival_time + min_waiting <= departure_time:
        return True
    else:
        return False

def list_routes_rec(flights :Dict,start :Airport,b :Airport,arrival_time,T :int,solution :List,paths):
    if start == b:
        paths.append(solution[1].copy())
    else:
        for flight in flights[start]:
            actual_cost = (l(flight) - arrival_time + a(flight) - l(flight))
            cost = solution[0] + actual_cost  # finora + attesa + volo
            if backtrack(arrival_time, l(flight), c(start), cost, T):
                solution[0] += actual_cost
                solution[1].append(flight)
                list_routes_rec(flights,d(flight),b,a(flight),T,solution,paths)
                solution[1].remove(flight)
                solution[0] -= actual_cost


def list_routes(flights :List[Flight],start :Airport,b :Airport,t,T :int):
    solution = [0,[]]
    paths = []

    # Construction
    flights_tmp = dict()
    for flight in flights:
        if s(flight) in flights_tmp:
            flights_tmp[s(flight)].append(flight)
        else:
            flights_tmp[s(flight)] = [flight]

    list_routes_rec(flights_tmp,start,b,t,T,solution,paths)
    return paths

"""
def list_routes(flights :List[Flight],start :Airport,b :Airport,t,T :int):
    stack = ArrayStack()
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
            stack.push((i,flight,cost))
            paths[i] = []
            # print(str(i), str(flight), cost)
            i+=1

    while not stack.is_empty():
        begin, my_flight, time_elapsed = stack.pop()
        paths[begin].append(my_flight)
        # print("ITERATION "+str(time_elapsed))
        if d(my_flight) != b:
            item = paths.pop(begin)
            j = len(paths)
            for flight in flights_tmp[d(my_flight)]:
                cost = time_elapsed + (l(flight) - a(my_flight) + a(flight) - l(flight)) # finora + attesa + volo
                if backtrack(a(my_flight),l(flight),c(d(my_flight)),cost,T):
                    stack.push((j,flight,cost))
                    paths[j] = item + []
                    # print(str(j), str(flight), cost)
                    # print("DURATA VOLO - ", a(flight) - l(flight))
                    # print("DURATA ATTESA - ", l(flight) - a(my_flight))
                    j += 1
        else:
            paths = solution.copy()
    return paths"""


# if __name__ == "__main__":
    #
    # airports,flights=read_from_file("test1")
    #
    # """for airport in airports:
    #     print(airport)
    #
    # for flight in flights:
    #     print(flight)"""
    #
    # start = airports[0]
    # end = airports[3]
    # starting_time = datetime.strptime("12:00", "%H:%M").time()
    # total_time = datetime.strptime("23:00", "%H:%M").time()
    #
    # start_time_minutes = starting_time.hour*60 + starting_time.minute
    # total_time_minutes = total_time.hour*60 + total_time.minute
    #
    # paths = list_routes(flights,start,end,start_time_minutes,total_time_minutes)
    #
    # print("\n\nPercorsi da "+str(start)+" a "+str(end)+" in "+str(total_time_minutes)+" minuti ")
    # print("Partenza alle "+str(starting_time))
    #
    # for path in paths:
    #     print("--------------PATH----------- ")
    #     for flight in path:
    #         print(str(flight))
