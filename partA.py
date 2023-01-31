import argparse

import random



parser = argparse.ArgumentParser(description='Generate a weighted graph')

parser.add_argument('--vertices', type=int, default=random.randint(2, 10), help='Number of vertices in the graph')

parser.add_argument('--connected', action='store_true', help='Indicates if the graph should be connected')

args = parser.parse_args()



# Create a list of vertices

vertices = [str(i) for i in range(args.vertices)]