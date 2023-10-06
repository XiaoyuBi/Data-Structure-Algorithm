import math
import heapq

def Bellman_Ford(n: int, edges: list, start_node: int) -> list:
    """
    The Bellman-Ford algorithm finds shortest paths from 
    a starting node to all nodes of the graph. 
    The algorithm can process all kinds of graphs, 
    provided that the graph does not contain a cycle with negative length.
    (It's OK if some edges have negative weight)

    The time complexity of the algorithm is O(nm), 
    because the algorithm consists of n - 1 rounds and 
    iterates through all m edges during a round.

    Params:
        n: number of nodes in the graph
        edges: List[(a, b, w)], edges that connect (a, b) with weight w
        start_node: 
    Return:
        distances: distances between start_node and the others
    """

    distances = [math.inf] * n
    distances[start_node] = 0

    # at most n-1 rounds is needed
    for _ in range(n - 1):
        changed_during_round = False
        
        for a, b, w in edges:
            if distances[a] + w < distances[b]:
                changed_during_round = True 
                distances[b] = distances[a] + w
            if distances[b] + w < distances[a]:
                changed_during_round = True 
                distances[a] = distances[b] + w
        
        # early stopping
        if not changed_during_round:
            break
    
    return distances


def Dijkstra(graph: dict[int, list], start_node: int) -> list:
    """
    Dijkstra's algorithm finds shortest paths from the starting node 
    to all nodes of the graph, like the Bellman-Ford algorithm. 
    The benefit of Dijsktra's algorithm is that it is more efficient 
    and can be used for processing large graphs. However, the algorithm 
    requires that there are no negative weight edges in the graph.

    The time complexity of the above implementation is O(n + m log m), 
    because the algorithm goes through all nodes of the graph and 
    adds for each edge at most one distance to the priority queue.

    Params:
        graph: a -> List[(b, w)] edges that connect (a, b) with weight w
        start_node:
    
    Return:
        distances: distances between start_node and the others
    """
    distances = [math.inf] * n
    distances[start_node] = 0
    
    queue = [(0, start_node)]
    visited = set()
    while queue:
        dist, a = heapq.heappop(queue)
        
        # each node only needs to be visited once
        if a in visited: 
            continue
        visited.add(a)

        # iterate current node's neighbours
        for b, w in graph[a]:
            distances[b] = min(distances[b], dist + w)
            heapq.heappush(queue, (distances[b], b))
    
    return distances


if __name__ == "__main__":

    n = 5
    edges = [
        (0, 1, 5), (0, 2, 3), (0, 3, 7),
        (1, 3, 3), (1, 4, 2), (2, 3, 1),
        (3, 4, 2)
    ]
    graph = {
        0: [(1, 5), (2, 3), (3, 7)],
        1: [(0, 5), (3, 3), (4, 2)],
        2: [(0, 3), (3, 1)],
        3: [(0, 7), (1, 3), (2, 1), (4, 2)],
        4: [(1, 2), (3, 2)]
    }
    
    print("Bellman-Ford Algorithm")
    print("Distances for start node at 0: ")
    print(Bellman_Ford(n, edges, 0))
    print("Distances for start node at 2: ")
    print(Bellman_Ford(n, edges, 2))
    print()
    print("Dijkstra's Algorithm")
    print("Distances for start node at 0: ")
    print(Dijkstra(graph, 0))
    print("Distances for start node at 2: ")
    print(Dijkstra(graph, 2))
