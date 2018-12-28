from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from utils import *
from typing import Dict, List

"""
def find_route(airports: List[Airport], flights: Dict, start: Airport, b: Airport, t):
    ""
    :param airports: Lista di tutti gli aeroporti
    :param flights: dict di tutti i voli
    :param start: aeroporto di partenza
    :param b: aeroporto di destinazione
    :param t: orario di partenza
    :returns: la rotta che permette di arrivare da start a b nel minor tempo possibile, partendo ad un orario non precedente a t
    ""
    cost = {}
    cloud = {}
    path = []
    queue = AdaptableHeapPriorityQueue()

    for airport in airports:
        cost[airport] = [float('inf'), queue.add(float('inf'), (airport, None, t))]

    cost[start][0] = 0
    queue.update(cost[start][1], 0, (start, None, t))

    while not queue.is_empty() and b not in cloud:
        _, (airport, flight_last, arrival_time) = queue.remove_min()
        cloud[airport] = flight_last
        for flight in flights[airport]:
            if d(flight) not in cloud and arrival_time + c(airport) <= l(flight):
                new_cost = cost[airport][0] + l(flight) - arrival_time + a(flight) - l(flight)
                if new_cost < cost[d(flight)][0]:
                    cost[d(flight)][0] = new_cost
                    queue.update(cost[d(flight)][1], cost[d(flight)][0], (d(flight), flight, a(flight)))

    my_flight = cloud[b]
    while my_flight is not None:
        path.insert(0, my_flight)
        my_flight = cloud[s(my_flight)]

    return path, cost[b][0]
"""

def find_route(airports: List[Airport], flights: Dict, start: Airport, b: Airport, t):
    """
    :param airports: Lista di tutti gli aeroporti
    :param flights: dict di tutti i voli
    :param start: aeroporto di partenza
    :param b: aeroporto di destinazione
    :param t: orario di partenza
    :returns: la rotta che permette di arrivare da start a b nel minor tempo possibile, partendo ad un orario non precedente a t
    """
    cost = {}
    cloud = {}
    path = []
    queue = AdaptableHeapPriorityQueue()

    for airport in airports:
        cost[airport] = [float('inf'), queue.add(float('inf'), (airport, None, t))]

    cost[start][0] = 0
    queue.update(cost[start][1], 0, (start, None, t))

    while not queue.is_empty() and b not in cloud:
        _, (airport, flight_last, arrival_time) = queue.remove_min()
        cloud[airport] = flight_last
        for flight in flights[airport]:

            if arrival_time + c(airport) <= l(flight):
                waiting_time = l(flight) - arrival_time
            else:
                waiting_time = 24*60 - arrival_time + l(flight) # Posso prenderlo il giorno dopo

            if d(flight) not in cloud and waiting_time >= c(airport):
                new_cost = cost[airport][0] + waiting_time + interval_time(l(flight),a(flight))
                if new_cost < cost[d(flight)][0]:
                    cost[d(flight)][0] = new_cost
                    queue.update(cost[d(flight)][1], cost[d(flight)][0], (d(flight), flight, a(flight)))

    my_flight = cloud[b]
    while my_flight is not None:
        path.insert(0, my_flight)
        my_flight = cloud[s(my_flight)]

    return path, cost[b][0]