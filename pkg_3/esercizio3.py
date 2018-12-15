from Flight import *
from Airport import *
from utils import read_from_file
from typing import List


def select_flights(flights :List[Flight],B :int):

    # Construction
    flights_tmp = dict()
    for flight in flights:
        if s(flight) in flights_tmp:
            flights_tmp[s(flight)].append(flight)
        else:
            flights_tmp[s(flight)] = [flight]

    # flights_tmp dizionario che contiene
    # chiave --> aeroporto x
    # valore --> lista di voli che partono da x

if __name__ == "__main__":
    airports,flights = read_from_file("test1")



