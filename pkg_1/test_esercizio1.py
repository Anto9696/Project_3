from datetime import datetime
from utils import read_from_file
from pkg_1.esercizio1 import list_routes


test_file = input("Inserire il nome del file ")
airports,flights=read_from_file(test_file)


print(" AEROPORTI ")
for i in range(len(airports)):
    print(i, " - ", airports[i])

start_index = int(input("Scegli indice aeroporto di partenza "))
end_index = int(input("Scegli indice aeroporto di arrivo "))
departure_time = input("Inserire ora hh:mm di parteza ")
max_time = input("Inserire tempo massimo per la tratta hh:mm ")

start = airports[start_index]
end = airports[end_index]
starting_time = datetime.strptime(departure_time, "%H:%M").time()
total_time = datetime.strptime(max_time, "%H:%M").time()

start_time_minutes = starting_time.hour*60 + starting_time.minute
total_time_minutes = total_time.hour*60 + total_time.minute

paths = list_routes(flights,start,end,start_time_minutes,total_time_minutes)

print("\n\nPercorsi da "+str(start)+" a "+str(end)+" in "+str(total_time_minutes)+" minuti ")
print("Partenza alle "+str(starting_time))

for path in paths:
    print("--------------PATH----------- ")
    for flight in path:
        print(str(flight))
