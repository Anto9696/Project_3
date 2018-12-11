from TdP_collections.graphs.graph import Graph
import datetime


class AirService(Graph):
    class Airport(Graph.Vertex):
        __dict__ = "_min_scalo"

        def __init__(self, name, min_scalo):
            super().__init__(name)
            self._min_scalo = min_scalo

        def getMinScalo(self):
            return self._min_scalo

    class Flight(Graph.Edge):
        __dict__ = '_departure_time','_arrival_time','_seats'

        def __init__(self,u,v,dt,at,seats):
            super().__init__(u,v,at-dt)
            self._seats = seats
            self._arrival_time = at
            self._departure_time = dt

        def getArrivalTime(self):
            return self._arrival_time

        def getDepartureTime(self):
            return self._departure_time

        def getSeats(self):
            return self._seats

    def __init__(self, filename=None):
        super().__init__(True)
        if filename is not None:
            self.__init_from_file(filename)

    def __init_from_file(self,filename):
        with open(filename) as f:
            vertices = int(f.readline())
            edges = int(f.readline())
            vertex = []

            for i in range(vertices):
                name,c = f.readline().split()
                vertex.append(self.insert_vertex(name,int(c)))

            for i in range(edges):
                u,v,dt,at,s = f.readline().split()
                dt = datetime.datetime.strptime(dt,"%H:%M")
                at = datetime.datetime.strptime(at,"%H:%M")
                self.insert_edge(vertex[int(u)],vertex[int(v)],dt,at,int(s))

            f.close()

    def insert_vertex(self, name,x=None):
        """Insert and return a new Vertex with element x."""
        v = self.Airport(name,x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}  # need distinct map for incoming edges
        return v

    def insert_edge(self, u, v, dt, at, s):
        """Insert and return a new Edge from u to v with auxiliary element x.

        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        if self.get_edge(u, v) is not None:  # includes error checking
            raise ValueError('u and v are already adjacent')
        if dt > at :
            raise ValueError("Departure time is greater than arrival time")
        e = self.Flight(u, v, dt, at, s)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e


if __name__ == "__main__":

    a = AirService("test1")

    for v in a.vertices():
        print(v)

    for e in a.edges():
        print(e)