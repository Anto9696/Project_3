
class Airport:
    __dict__ = '_name','_min'

    def __init__(self,name,min):
        self._name=name
        self._min=min

    def __str__(self):
        return self._name + " " + str(self._min)

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, other):
        if isinstance(other,Airport):
            return other._name == self._name
        return False
def c(a: Airport):
    return a._min.hour*60+a._min.minute
