import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self.load_all_artists()
        self.dao = DAO()
        self.id_map = {}

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        return self._artists_list

    def build_graph(self):
        artisti = self.load_all_artists()


        artisti_id = []

        for artista in artisti:
            artisti_id.append(artista.id)







