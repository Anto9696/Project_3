
class Flight:
    __dict__ = '_dep_airport','_arr_airport','_dep_time','_arr_time','_seats'

    def __init__(self,dep_airport,arr_airport,dep_time,arr_time,seats):
        self._dep_airport = dep_airport
        self._arr_airport = arr_airport
        self._dep_time = dep_time
        self._arr_time = arr_time
        self._seats = seats

    def __str__(self):
        return str(self._dep_airport)+" "+str(self._arr_airport)+" "+str(self._dep_time)+" "+str(self._arr_time)+" "+str(self._seats)

def s(f :Flight):
    return f._dep_airport

def d(f :Flight):
    return f._arr_airport

def l(f :Flight):
    return f._dep_time.hour * 60 + f._dep_time.minute

def a(f :Flight):
    return f._arr_time.hour * 60 +f._arr_time.minute

def p(f :Flight):
    return f._seats