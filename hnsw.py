import math
import random
from node import Node
from langchain_ollama import OllamaEmbeddings


class HNSW:
    def __init__(self, M, ef_construction=200):
        self.M = M
        self.max_level = -1
        self.global_entry_point = None
        self.nodes = {}
        self.counter = 0
        self.model = OllamaEmbeddings(model="nomic-embed-text")

    def get_random_level(self):
        """Probability function which gets a random level and designed to give level 0 often times """
        multiplier = 1 / math.log(self.M)
        level = int(-math.log(random.random()) * multiplier)
        return level

    def get_M_neighbours(self):


    def insert(self, content):
        level = self.get_random_level()
        self.max_level = max(level, self.max_level)
        node_connections = {}
        embedding = self.model.embed_query(content)
        new_node = Node(self.counter, embedding, level, {})

        # Set global entry point
        if self.global_entry_point is None:
            self.global_entry_point = new_node
            for i in range(self.max_level + 1):
                node_connections.update({i : []})
            new_node.connections = node_connections
        else:
            # Search from the global entry point onward
            current_level = self.max_level
            local_entry_point = self.global_entry_point
            while current_level > 0:
                pass


            neighbours_of_entry_point = self.global_entry_point.connections.get(self.max_level,[])
            if current_level == level:
                # Insert node at this level, no need to go down
                pass


        # Add node to global list
        for i in range(self.max_level + 1):
            lst = self.nodes.get(i, [])
            lst.append(new_node)
            self.nodes.update({i : lst})

HNSW(4).insert("Yoo mate")



