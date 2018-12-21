from datetime import datetime
from utils import read_from_file
from pkg_1.esercizio1 import list_routes

airports,flights=read_from_file("test1")

"""for airport in airports:
    print(airport)

for flight in flights:
    print(flight)"""

start = airports[0]
end = airports[3]
starting_time = datetime.strptime("12:00", "%H:%M").time()
total_time = datetime.strptime("23:00", "%H:%M").time()

start_time_minutes = starting_time.hour*60 + starting_time.minute
total_time_minutes = total_time.hour*60 + total_time.minute

paths = list_routes(flights,start,end,start_time_minutes,total_time_minutes)

print("\n\nPercorsi da "+str(start)+" a "+str(end)+" in "+str(total_time_minutes)+" minuti ")
print("Partenza alle "+str(starting_time))

for path in paths:
    print("--------------PATH----------- ")
    for flight in path:
        print(str(flight))
