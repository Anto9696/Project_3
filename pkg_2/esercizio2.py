from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from utils import *
from typing import Dict, List

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
    queue_locator = {}

    for airport in airports:
        if airport is start:
            cost[airport] = 0
        else:
            cost[airport] = float('inf')
        queue_locator[airport] = queue.add(cost[airport], (airport, None, t))

    while not queue.is_empty() and b not in cloud:
        key,(airport, flight_last, arrival_time) = queue.remove_min()
        cloud[airport] = flight_last
        del queue_locator[airport]

        for flight in flights[airport]:

            if arrival_time + c(airport) <= l(flight):
                waiting_time = l(flight) - arrival_time
            else:
                waiting_time = 24*60 - arrival_time + l(flight) # Provo a prenderlo il giorno dopo

            if waiting_time < c(airport):
                # Si suppone che c(airport) sia inferiore a 24h
                waiting_time += 24*60

            if d(flight) not in cloud:
                new_cost = cost[airport] + waiting_time + interval_time(l(flight),a(flight))
                if new_cost < cost[d(flight)]:
                    cost[d(flight)] = new_cost
                    queue.update(queue_locator[d(flight)], cost[d(flight)], (d(flight), flight, a(flight)))

    my_flight = cloud[b]
    while my_flight is not None:
        path.insert(0, my_flight)
        my_flight = cloud[s(my_flight)]

    return path, cost[b]