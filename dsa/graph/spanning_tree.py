import heapq
import random
from typing import Iterable
from collections import defaultdict

class UnionFind:
    """
    A union-find structure maintains a collection of sets. 
    The sets are disjoint, so no element belongs to more than one set. 
    Two O(logn) time operations are supported: 
    the unite operation joins two sets, and 
    the find operation finds the representative of the set that contains a given element.
    """

    def __init__(self, candidates: Iterable[int]):

        self.link = {}
        self.size = defaultdict(int)

        for candidate in candidates:
            self.link[candidate] = candidate
            self.size[candidate] += 1
    
    # find the repersentative of element x in O(logn)
    # x must be from candidates, otherwise throw error
    def find(self, x: int) -> int:
        if x not in self.link:
            raise ValueError(f"{x} is not from valid candidates!")
        
        while self.link[x] != x:
            x = self.link[x]
        
        return x
    
    # union both sets which x and y are in
    # always merge smaller one to larger one !
    def union(self, x: int, y: int):
        # get both representatives
        x, y = self.find(x), self.find(y)

        if self.get_size(x) < self.get_size(y):
            x, y = y, x 
        
        # reset the link and size
        self.link[y] = x
        self.size[x] += self.get_size(y)
    
    # check if element x and y are in the same union set
    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    # get the size the set which x is in
    # always reach out to the representative for set size !
    def get_size(self, x: int) -> int:
        rep = self.find(x)
        return self.size[rep]


def Kruskal(edges: list) -> list:
    """
    A greedy method to construct minimum and maximum spanning trees.

    In Kruskal's algorithm, the initial spanning tree only contains 
    the nodes of the graph and does not contain any edges. 
    Then the algorithm goes through the edges ordered by their weights, 
    and always adds an edge to the tree if it does not create a cycle.

    The first phase of the algorithm sorts the edges in the list in O(mlogm) time.
    The time complexity of Kruskal's algorithm will be O(mlogn) after sorting.

    Params:
        edges: List[(a, b, w)], edges that connect (a, b) with weight w
    Return:
        edges: List[(a, b, w)], edges in minimum spanning tree that connect 
        (a, b) with weight w
    """

    edges.sort(key = lambda x: x[2])
    candidates = set()
    for a, b, _ in edges:
        candidates.add(a)
        candidates.add(b)
    
    tree = []
    myUnionFind = UnionFind(candidates)
    for a, b, w in edges:
        if not myUnionFind.same(a, b):
            myUnionFind.union(a, b)
            tree.append((a, b, w))
    
    return tree


def Prim(edges: list) -> list:
    """
    A greedy method to construct minimum and maximum spanning trees.

    Prim's algorithm is an alternative method for finding a minimum spanning tree. 
    The algorithm first adds an arbitrary node to the tree. 
    After this, the algorithm always chooses a minimum-weight edge 
    that adds a new node to the tree. 
    Finally, all nodes have been added to the tree and a minimum spanning tree found.

    The time complexity of Prim's algorithm is O(n+mlogm) that 
    equals the time complexity of Dijkstra's algorithm.

    Params:
        edges: List[(a, b, w)], edges that connect (a, b) with weight w
    Return:
        edges: List[(a, b, w)], edges in minimum spanning tree that connect 
        (a, b) with weight w
    """
    graph = defaultdict(list)
    for a, b, w in edges:
        graph[a].append((b, w))
        graph[b].append((a, w))
    
    # select a random start node
    start = random.choice(list(graph.keys()))
    print(f"Randomly choose {start} as start node")
    queue = [] # PQ for edges that connect "connected" and "not-connected"
    visited = {start}
    for b, w in graph[start]:
        heapq.heappush(queue, (w, start, b))
    
    tree = []
    while queue:
        w, a, b = heapq.heappop(queue)

        # new edges must add a new node
        # if not, skip
        if b in visited:
            continue 

        visited.add(b)
        tree.append((a, b, w))

        # get new edges that connect "connected" and "not-connected"
        for neighbor, w in graph[b]:
            heapq.heappush(queue, (w, b, neighbor))
    
    return tree

if __name__ == "__main__":
    edges = [
        (1, 2, 3), (1, 5, 5), (2, 5, 6),
        (2, 3, 5), (3, 6, 3), (5, 6, 2),
        (3, 4, 9), (4, 6, 7)
    ]

    print("Kruskal's algorithm: ")
    tree = Kruskal(edges)
    path = [(x[0], x[1]) for x in tree]
    path_sum = sum([x[2] for x in tree])
    print(f"Minimum spanning tree: {path}")
    print(f"Minimum spanning tree weight {path_sum}")

    print("Prim's algorithm: ")
    tree = Prim(edges)
    path = [(x[0], x[1]) for x in tree]
    path_sum = sum([x[2] for x in tree])
    print(f"Minimum spanning tree: {path}")
    print(f"Minimum spanning tree weight {path_sum}")
