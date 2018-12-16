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


def find_route(flights :List[Flight], start :Airport,b :Airport,t):

    priority_queue = AdaptableHeapPriorityQueue();

    # Construzione mappa di adiacenza, dato un aereoporto (chiave) ottengo la lista di tutti i voli che partono da questo)
    airports_flights = dict()
    for flight in flights:
        if l(flight) > t:        #se l'orario di partenza dei voli è precedente a t non vengono messi nella mappa di adiacenza dell'aereoporto
            if s(flight) in airports_flights:
                airports_flights[s(flight)].append(flight)
            else:
                airports_flights[s(flight)] = [flight]

    return Dijkstra(airports_flights, start, b, t)




def Dijkstra(airports_flights , start :Airport,b :Airport,t):

    d = {}                                 # d[v] è un limite superiore alla distanza tra aereoporto start e un altro aereoporto
    cloud = {}                             # dizionario che mappa aereoporto in d[aereoporto], dove questa eticetta rappresenta il costo per andare da start a aereoporto nel minor tempo
    pq = AdaptableHeapPriorityQueue()      #vertice v avrà key d[v]
    pqlocator = {}                         #dizionario che mappa un vertice nel suo pq locator per trovarlo in O(1)
    min_tree_path = []

    airports = airports_flights.keys()
    flights : List[Flight] = airports_flights.values()

    for airport in airports:
        if airport is start:
            d[airport] = 0
        else:
            d[airport] = float('inf')
        pqlocator[airport] = pq.add(d[airport], airport)  #salva il locator per i fututi aggiornamenti

    while not pq.is_empty() or not b in cloud:       # perchè se b è in cloud ho già trovato il percorso minimo che mi porta da a a b
        key, u = pq.remove_min()
        cloud[u] = key   #inserisce u nella soluzione
        del pqlocator[u]
        for flight in flights[u]:    #per tutti gli archi uscenti da u, quindi per tutti i voli che partono da quell'aereoporto
            airport = d(flight)   #prendo l'aereoporto di arrivo
            if airport not in cloud:
                costo = c(d(airport))+ (l(flight) - a(flight))  # dove per costo si intende costo viaggio + costo attesa aereoporto d'arrivo
                if d[u] + costo < d[airport]:
                    d[airport] = d[u] + costo
                    pq.update(pqlocator[airport], d[airport], airport)  #aggiorna d[v] nella pq

    if b not in cloud:
        return None
    # arrivato qui avrò un dizionario con chiavi i vertici messi nella soluzione e valori i costi per arrivarci da s

    # for airport in cloud:
    #     if airport is not start:
    #         for flight in flights:
    #             if d(flight) == airport:   #conssidera gli archi enranti, i voli che entrano in questo aereoporto
    #                 u = s(flight)          #se flight è uno di questi, mettilo in u
    #                 costo = c(flight) + (a(flight) - l(flight))
    #                 if d[airport] == d[u] + costo:
    #                     min_tree_path[airport] = flight

    u = b
    for flight in flights:
        if d(flight) == u:
            costo = c(u) + (a(flight) - l(flight))
            d_u = cloud[u]
            if cloud[airport] == cloud[u] + costo:
                min_tree_path.append(u)

    return min_tree_path.reverse()