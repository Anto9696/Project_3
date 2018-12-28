from Airport import *
from Flight import *
from datetime import datetime

def read_from_file(filename):
    airports = []
    flights = []

    with open(filename) as f:
        vertices = int(f.readline())
        edges = int(f.readline())
        for i in range(vertices):
            name, c = f.readline().split()
            c = datetime.strptime(c, "%H:%M").time()
            airports.append(Airport(name, c))

        for i in range(edges):
            u, v, dt, at, s = f.readline().split()
            dt = datetime.strptime(dt, "%H:%M").time()
            at = datetime.strptime(at, "%H:%M").time()
            flights.append(Flight(airports[int(u)], airports[int(v)], dt, at, int(s)))

        f.close()

    return airports, flights

def interval_time(departure_time, arrival_time):
    if arrival_time < departure_time:
        return 24*60 - departure_time + arrival_time
    else:
        return arrival_time - departure_time