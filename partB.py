import argparse
import sys
from collections import defaultdict
import re




def shortest_path(graph, start, end):

    # Initialize distance dictionary

    dist = {vertex: float('infinity') for vertex in graph}
    dist[start] = 0

    # Initialize predecessor dictionary

    pred = {vertex: None for vertex in graph}

    # Initialize the unvisited set

    unvisited = set(graph)

    # Run Dijkstra's algorithm

    while unvisited:
        current = min(unvisited, key=lambda vertex: dist[vertex])
        unvisited.remove(current)

        for neighbor, weight in graph[current].items():
            if dist[neighbor] > dist[current] + weight:
                dist[neighbor] = dist[current] + weight
                pred[neighbor] = current
    
    # Build shortest path
    path = []
    vertex = end

    while vertex is not None:

        path.append(vertex)
        vertex = pred[vertex]



    # Reverse the path
    path = path[::-1]

    # Print the shortest path and its length

    if dist[end] != float('infinity'):

        print("Shortest path:", ' -> '.join(path))
        print("Length of the shortest path:", dist[end])

    else:
        print("No path from {} to {}".format(start, end))

if __name__ == "__main__":


    parser = argparse.ArgumentParser(description='Find the shortest path between two vertices')
    parser.add_argument('start', type=str, help='The start vertex')
    parser.add_argument('end', type=str, help='The end vertex')
    args = parser.parse_args()

 # Initialize the graph and the set of vertices

    graph = defaultdict(dict)
    vertices = set()
    edge_count = defaultdict(int)

    # Read the graph from standard input

    for i, line in enumerate(sys.stdin):
        edge = line.strip().split()
        if len(edge) != 3:
            print("Invalid input at line", i+1)
            sys.exit(1)

        start, end, weight = edge

# check if weight is valid

    if not re.match(r"^[0-9]+(\.[0-9]{1,4})?$",weight):
        print("Invalid weight at line", i+1)
        sys.exit(1)

    weight = float(weight)

     # check if vertex is valid

    if not re.match(r"^[A-Za-z0-9]+$", start) or not re.match(r"^[A-Za-z0-9]+$", end):

        print("Invalid vertex name at line", i+1)
        sys.exit(1)

    vertices.add(start)
    vertices.add(end)

    # Check if edge is already present in graph

    if edge_count[(start, end)] > 0:

        print("Duplicate edge at line", i+1, ", first appeared at", edge_count[(start, end)])
        sys.exit(1)

    else:
       edge_count[(start, end)] = i+1

    graph[start][end] = weight
    graph[end][start] = weight