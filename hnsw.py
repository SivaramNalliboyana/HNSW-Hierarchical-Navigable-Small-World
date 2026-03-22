import math
import random
from node import Node

class HNSW:
    def __init__(self, M, ef_construction=200):
        self.M = M
        self.max_level = -1
        self.global_entry_point = None
        self.nodes = {}
        self.counter = 0

    def get_random_level(self):
        """Probability function which gets a random level and designed to give level 0 often times """
        multiplier = 1 / math.log(self.M)
        level = int(-math.log(random.random()) * multiplier)
        return level

    def insert(self, vector, connections):
        level = self.get_random_level()
        self.max_level = max(level, self.max_level)
        new_node = Node(self.counter, vector, level, {})

        # Set global entry point
        if self.global_entry_point is None:
            self.global_entry_point = new_node

