from pkg_3.esercizio3 import select_flights
from utils import read_from_file

while True:
    # airports, flights = read_from_file("test1")
    print("Su quale file vuoi fare il test?: ")
    test_file = input("Digita la tua scelta: (un numero da 1 a 6)")
    airports,flights=read_from_file("../tests/test" + test_file)

    print("\nTEST "+test_file+"\n")

    selected, money = select_flights(flights, airports, 6000)

    print(" VOLI ")
    for flight in selected:
        print(flight)

    print(" SOLDI ")
    for airport in money.keys():
        print(airport, money[airport])


    print("Vuoi testare un altro file?" )
    select = input("Premere S per continuare, altrimenti premere un qualsiasi altro tasto")
    if select.upper() != "S":
        break
    print("_______________________________________________________________________________________")
