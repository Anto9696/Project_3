from pkg_3.esercizio3 import select_flights
from utils import read_from_file

airports, flights = read_from_file("test1")

selected, money = select_flights(flights, airports, 6000)

print(" VOLI ")
for flight in selected:
    print(flight)

print(" SOLDI ")
for airport in money.keys():
    print(airport, money[airport])
