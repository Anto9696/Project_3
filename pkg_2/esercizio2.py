from Airport import *
from Flight import *
from typing import List
from datetime import datetime
from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from TdP_collections.list.positional_list import PositionalList
from utils import read_from_file

def canBeTaken(flight, costo):
    return True



def find_route(flights :List[Flight], start :Airport,b :Airport,t):

    route = PositionalList()

    # Construzione mappa di adiacenza, dato un aereoporto (chiave) ottengo la lista di tutti i voli che partono da questo)
    airports_flights = dict()
    for flight in flights:
        if l(flight) > t:        #se l'orario di partenza dei voli è precedente a t non vengono messi nella mappa di adiacenza dell'aereoporto
            if s(flight) in airports_flights:
                airports_flights[s(flight)].append(flight)
            else:
                airports_flights[s(flight)] = [flight]

    min_tree_path = Dijkstra(airports_flights, start, b, t)

    flight_tmp = min_tree_path[b]
    route.add_first(flight_tmp)

    while s(flight_tmp) != start:
        flight_tmp = min_tree_path[s(flight_tmp)]
        route.add_first(flight_tmp)
    if(flight_tmp not in route):
        route.add_first(flight_tmp) #il volo che ha come aereoporto di partenza start

    for e in route:
        print(e)
    return route




def Dijkstra(airports_flights , start :Airport,b :Airport,t):

    D = {}                                 # D[v] è un limite superiore alla distanza tra aereoporto start e un altro aereoporto
    cloud = {}                             # dizionario che mappa aereoporto in D[aereoporto], dove questa eticetta rappresenta il costo per andare da start a aereoporto nel minor tempo
    pq = AdaptableHeapPriorityQueue()      #vertice v avrà key D[v]
    pqlocator = {}                         #dizionario che mappa un vertice nel suo pq locator per trovarlo in O(1)
    min_tree_path = {}

    airports = airports_flights.keys()
    flights : List[Flight] = []
    for list_flight in airports_flights.values():
        flights += list_flight

    for airport in airports:
        if airport is start:
            D[airport] = 0
        else:
            D[airport] = float('inf')
        pqlocator[airport] = pq.add(D[airport], airport)  #salva il locator per i fututi aggiornamenti


    while not pq.is_empty() or not b in cloud:       # perchè se b è in cloud ho già trovato il percorso minimo che mi porta da a a b
        key, u = pq.remove_min()
        cloud[u] = key   #inserisce u nella soluzione
        del pqlocator[u]
        for flight in airports_flights[u]:    #per tutti gli archi uscenti da u, quindi per tutti i voli che partono da quell'aereoporto
            airport = d(flight)   #prendo l'aereoporto di arrivo
            if airport not in cloud:
                costo = c(airport)+ (a(flight) - l(flight))  # dove per costo si intende costo viaggio + costo attesa aereoporto D'arrivo
                if(canBeTaken(flight, costo)):
                    if D[u] + costo < D[airport]:
                        D[airport] = D[u] + costo
                        pq.update(pqlocator[airport], D[airport], airport)  #aggiorna D[v] nella pq

    if b not in cloud:
        return None
    # arrivato qui avrò un dizionario con chiavi i vertici messi nella soluzione e valori i costi per arrivarci da s

    for e in cloud:
        print(e)

    for airport in cloud:
        if airport is not start:
            for flight in flights:
                if d(flight) == airport:   #conssidera gli archi enranti, i voli che entrano in questo aereoporto
                    u = s(flight)          #se flight è uno di questi, mettilo in u
                    costo = c(airport) + (a(flight) - l(flight))
                    if D[airport] == D[u] + costo:
                        min_tree_path[airport] = flight



    return min_tree_path


    # u = b
    #
    # for flight in flights:
    #     if d(flight) == u:
    #         costo = c(u) + (a(flight) - l(flight))
    #         d_u = cloud[u]
    #         if cloud[airport] == cloud[u] + costo:
    #             min_tree_path.append(flight)
    #
    # return min_tree_path.reverse()


if __name__ == "__main__":

    airports,flights=read_from_file("test2.txt")

    """for airport in airports:
        print(airport)

    for flight in flights:
        print(flight)"""

    start = airports[0]
    end = airports[3]
    starting_time = datetime.strptime("11:00", "%H:%M").time()
    total_time = datetime.strptime("23:00", "%H:%M").time()

    start_time_minutes = starting_time.hour*60 + starting_time.minute
    total_time_minutes = total_time.hour*60 + total_time.minute

    path = find_route(flights,start,end,start_time_minutes)



    print("\n\nPercorso da "+str(start)+" a "+str(end)+" in "+str(total_time_minutes)+" minuti ")
    print("Partenza alle "+str(starting_time))

    print("--------------PATH----------- ")

    if(path is not None):
        for flight in path:
         print(flight)

    else:
        print("Nessun percorso trovato")
