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