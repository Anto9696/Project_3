from datetime import datetime
from utils import read_from_file
from pkg_1.esercizio1 import list_routes

while True:
    print("Su quale file vuoi fare il test?: ")
    test_file = input("Digita la tua scelta: (un numero da 1 a 6)")
    airports, flights = read_from_file("../tests/test" + test_file)

    print("\nTEST "+test_file+"\n")

    print(" AEROPORTI ")
    for i in range(len(airports)):
        print(i, " - ", airports[i])

    start_index = 0  # int(input("Scegli indice aeroporto di partenza "))
    end_index = 3  # int(input("Scegli indice aeroporto di arrivo "))
    departure_time = "16:00"  # input("Inserire ora hh:mm di parteza ")
    max_time = "23:00"  # input("Inserire tempo massimo per la tratta hh:mm ")

    start = airports[start_index]
    end = airports[end_index]
    starting_time = datetime.strptime(departure_time, "%H:%M").time()
    total_time = datetime.strptime(max_time, "%H:%M").time()

    start_time_minutes = starting_time.hour * 60 + starting_time.minute
    total_time_minutes = 50 * 60  # total_time.hour*60 + total_time.minute

    paths = list_routes(flights, start, end, start_time_minutes, total_time_minutes)

    print("\n\nPercorsi da " + str(start) + " a " + str(end) + " in " + str(total_time_minutes) + " minuti ")
    print("Partenza alle " + str(starting_time))

    for path in paths:
        print("--------------PATH----------- ", path[0])
        for flight in path[1]:
            print(str(flight))


    print("Vuoi testare un altro file?" )
    select = input("Premere S per continuare, altrimenti premere un qualsiasi altro tasto")
    if select.upper() != "S":
        break
    print("_______________________________________________________________________________________")
