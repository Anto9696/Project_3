from Airport import *
from Flight import *
from utils import interval_time
from typing import List,Dict


def backtrack(cost,total):
    # Backtracking function to prune the solution tree
    return cost <= total


def list_routes_rec(flights :Dict,start :Airport,b :Airport,arrival_time,T :int,solution :List,paths):
    if start == b:
        # Save the solution
        paths.append((solution[0],solution[1].copy()))
    else:
        for flight in flights[start]:
            # Try all possible solution

            # Calculate the cost
            if arrival_time + c(start) <= l(flight):
                waiting_time = l(flight) - arrival_time
            else:
                waiting_time = 24*60 - arrival_time + l(flight) # Provo a prenderlo il giorno dopo

            if waiting_time < c(start):
                # Si suppone che il tempo minimo di attesa sia inferiore a 24h
                waiting_time += 24*60

            actual_cost = waiting_time + interval_time(l(flight), a(flight))

            if backtrack(solution[0] + actual_cost, T):
                # This is a possible partial solution
                solution[0] += actual_cost
                solution[1].append(flight)
                list_routes_rec(flights,d(flight),b,a(flight),T,solution,paths)
                solution[1].pop()
                solution[0] -= actual_cost


def list_routes(flights :List[Flight],start :Airport,b :Airport,t,T :int):
    """
    :param flights: Lista di tutti i voli della compagnia
    :param start: aeroporto di partenza
    :param b: aeroporto di arrivo
    :param t: orario di partenza (espresso in minuti)
    :param T: tempo massimo per una rotta in minuti
    :return: Tutti i possibili percorsi da start a b che impiegano tempo non superiore a T minuti
    """
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