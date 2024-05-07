import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._airports = DAO.get_all_airports()  #importo tutti gli aeroporti
        self._flights = DAO.get_all_flights()  #importo tutti i voli
        self._airports_idMap = {}  #mappa in cui a ogni id di aeroporto è associato l'oggetto
        for a in self._airports:
            self._airports_idMap[a.id] = a
        self._flights_idMap = {}  #mappa in cui a una tupla (origine, dest) è associata una lista di voli
        for f in self._flights:
            try:
                self._flights_idMap[(f.origin_airport_id, f.destination_airport_id)].append(f)
            except KeyError:
                self._flights_idMap[(f.origin_airport_id, f.destination_airport_id)] = []
                self._flights_idMap[(f.origin_airport_id, f.destination_airport_id)].append(f)
        self._airports_graph = nx.Graph()  #creo il grafo vuoto

    def build_graph(self, d_minima):
        """
        Aggiunge i nodi, poi scorre i voli e aggiunge gli archi estraendo destinazione e arrivo dalla mappa
        """
        self._airports_graph.add_nodes_from(self._airports)  #aggiungo i nodi al grafo
        for t in self._flights_idMap:  #guardo tutte le coppie
            origin = self._airports_idMap[t[0]]  #estraggo l'aeroporto di partenza
            destination = self._airports_idMap[t[1]]  #estraggo l'aeroporto di arrivo
            flights = self._flights_idMap[t]  #estraggo i voli da origin a destination
            avg = self.avg_distance(flights)    #calcolo la media
            if avg >= d_minima:
                self._airports_graph.add_edge(origin, destination, weight=avg)

    def avg_distance(self, flights):
        """
        Calcola la distanza tra i voli con stessa origine e destinazione
        """
        s = 0
        for f in flights:
            s += f.distance
        avg = s / len(flights)
        return avg
