from Airport import *
from Flight import *
from typing import List
from datetime import datetime
from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from TdP_collections.list.positional_list import PositionalList
from utils import read_from_file


def find_route(flights :List[Flight], start :Airport, b :Airport, t):

    route = PositionalList()

    # Construzione mappa di adiacenza, dato un aereoporto (chiave) ottengo la lista di tutti i voli che partono da questo)
    airports_flights = dict()
    for flight in flights:
        if s(flight) in airports_flights:
            airports_flights[s(flight)].append(flight)
        else:
            airports_flights[s(flight)] = [flight]

    cloud, flight_taken = Dijkstra(flights, airports_flights, start, b, t)

    total_time = 0       #calcolo tempo totale per andare da "a" a "b"
    for e in cloud:
        total_time += cloud[e]

    flight_tmp = flight_taken[b]   #partiamo all'indietro, da b fino ad arrivare in a
    route.add_first(flight_tmp)

    while s(flight_tmp) != start or d(flight_tmp) == b:    #la seconda condizione perchè altrimenti il volo diretto da a e b non viene considerato nel while, quindi fa questo fino a quando                                               #l'aereoporto di partenza non è start o l'aereoporto di destinazione è b
        flight_tmp = flight_taken[s(flight_tmp)]
        route.add_first(flight_tmp)

    # for e in route:
    #     print(e)
    return route




def Dijkstra(flights, airports_flights, start :Airport, b :Airport, t):

    D = {}                                 # D[v] èl'etichetta che rappresenta la distanza tra aereoporto start e un altro aereoporto
    cloud = {}                             # dizionario che mappa aereoporto in D[aereoporto], dove questa eticetta rappresenta il costo per andare da start a aereoporto nel minor tempo
    pq = AdaptableHeapPriorityQueue()      #vertice v avrà key D[v], dove per vertice si intende un aereoporto
    pqlocator = {}                         #dizionario che mappa un vertice (aereoporto) nel suo pq locator per trovarlo in O(1)
    flightTaken = {}                       #dizionario che mappa un aereoporto nel volo preso per arrivarci

    min_tree_path = {}

    airports = airports_flights.keys()    # costruisco la lista degli aereoporti

    for airport in airports:       #inizializzo il vettore delle etichette
        if airport is start:
            D[airport] = 0
        else:
            D[airport] = float('inf')
        pqlocator[airport] = pq.add(D[airport], airport)  #salva il locator per i fututi aggiornamenti


    while not pq.is_empty() or not b in cloud:       # perchè se b è in cloud ho già trovato il percorso minimo che mi porta da a a b, posso già fermarmi
        key, u = pq.remove_min()                #la key sarebbe l'etichetta, u l'aereoporto con quella etichetta
        cloud[u] = key                           #inserisce u nella soluzione
        t += key                              #al tempo di partenza aggiungo il tempo per aver preso quel volo
        del pqlocator[u]
        for flight in airports_flights[u]:    #per tutti gli archi uscenti da u, quindi per tutti i voli che partono da quell'aereoporto
            if l(flight) > t:      #se il tempo di partenza di quel volo è successivo a t
                airport = d(flight)   #prendo l'aereoporto di arrivo
                if airport not in cloud:        #se questo non è ancora nella soluzione
                    flightTime = a(flight) - l(flight)   #calcolo il tempo di volo
                    min_waiting = c(airport)             #e il tempo di attesa nell'aereoporto di arrivo
                    # ora per costo si intende costo viaggio + costo attesa aereoporto D'arrivo + tempo impiegato ad aspettare l'orario di partenza dell'aereoporto
                    # quindi, nel calcolo del costo, se il tempo impiegato ad aspettare l'orario di partenza del volo che si sta considerando di prendere è > del tempo minimo di attesa, questo contiene anche quest'ultimo
                    #altrimenti il tempo minimo di attesa nell'aereoporto è pari esattamente al tempo minimo dello scalo

                    if l(flight) - t >= min_waiting:          #se la differenza di tempo tra quando arrivo e quando devo partire è > del tempo minimo di attesa
                        costo = ( l(flight) - t ) + ( a(flight) - l(flight) )   #il costo del volo che si sta considerando di prendere è proprio pari alla somma tra questa differenza di tempo passata ad aspettare che parta e il tempo di volo
                                                                                    #nell'if c'è >= perchè se è pari al tempo minimo di atessa per lo scalo, devo sommare al tempo di volo proprio questo tempo, che sarà anche uguale a quella differenza
                    else:
                        costo = float('inf')

                    #aggiornamento etichette
                    if D[u] + costo < D[airport]:
                        D[airport] = D[u] + costo
                        pq.update(pqlocator[airport], D[airport], airport)  #aggiorna D[v] nella pq
                        flightTaken[u] = flight      #mappo anche il volo corrispondente a quel costo aggiornato




    if b not in cloud:
        return None     # non esiste un collegamento tra a e b
    # arrivato qui avrò un dizionario con chiavi i vertici messi nella soluzione e valori i costi per arrivarci da s


    # print("cloud:")
    # for e in cloud:
    #     print(e)

    print("taken flight, ",len(flightTaken))

    for flight in flightTaken:
        print(flightTaken[flight])

    # for airport in cloud:
    #     if airport is not a:
    #         for flight in flights:
    #             if d(flight) == airport:   #conssidera gli archi enranti, i voli che entrano in questo aereoporto
    #                 u = s(flight)          #se flight è uno di questi, mettilo in u
    #                 costo = c(airport) + (a(flight) - l(flight))
    #                 if D[airport] == D[u] + costo:
    #                     min_tree_path[airport] = flight

    return cloud, flightTaken



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
