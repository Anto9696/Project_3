from pkg_2.esercizio2 import find_route
from utils import *
from datetime import datetime

while True:
    print("Su quale file vuoi fare il test?: ")
    # select = input("Digita la tua scelta: (un numero da 1 a 6)")
    #
    # airports, flights = read_from_file("test" + select + ".txt")
    test_file = input("Digita la tua scelta: (un numero da 1 a 6)")
    airports,flights=read_from_file("../tests/test" + test_file)

    print("\nTEST "+test_file+"\n")

    flights_dict = dict()
    for flight in flights:
        if s(flight) in flights_dict:
            flights_dict[s(flight)].append(flight)
        else:
            flights_dict[s(flight)] = [flight]

    start = airports[0]
    end = airports[3]
    starting_time = datetime.strptime("11:00", "%H:%M").time()
    starting_time_minutes = starting_time.hour*60+starting_time.minute

    path,time = find_route(airports,flights_dict,start,end,starting_time_minutes)

    print("Percorso migliore da {0} a {1} con partenza alle {2}".format(start,end,starting_time))
    print("Durata "+str(time))
    for flight in path:
        print(flight)

    print("Vuoi testare un altro file?" )
    select = input("Premere S per continuare, altrimenti premere un qualsiasi altro tasto")
    if select.upper() != "S":
        break
    print("_______________________________________________________________________________________")
