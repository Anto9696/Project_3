from Airport import *
from Flight import *
from typing import List
from datetime import datetime
from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from utils import read_from_file

def backtrack(arrival_time,departure_time,min_waiting,cost,total):
    if cost <= total and arrival_time + min_waiting <= departure_time:
        return True
    else:
        return False


def find_route(flights :List[Flight],start :Airport,b :Airport,t):

    priority_queue = AdaptableHeapPriorityQueue();
    paths = {}

    # Construction
    flights_tmp = dict()
    for flight in flights:
        if s(flight) in flights_tmp:
            flights_tmp[s(flight)].append(flight)
        else:
            flights_tmp[s(flight)] = [flight]


def Dijkstra(flights :List[Flight],start :Airport,b :Airport,t,T :int):
    d = {}
    cloud = {}
    pq = AdaptableHeapPriorityQueue()
    pqlocator = {}

    for airport in airports:

