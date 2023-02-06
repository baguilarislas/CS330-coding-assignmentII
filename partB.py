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