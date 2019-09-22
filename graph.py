# include any code you need for your assignment in this file or in auxiliary
# files that can be imported here.
import random
import networkx as nx
from itertools import combinations

# given number of nodes n and probability p, output a random graph 
# as specified in homework
def create_graph(n,p):
	nodes = range(n)
	g = nx.Graph()
	g.add_nodes_from(nodes)
	for u,v in combinations(g,2):
		if random.random() < p:
			g.add_edge(u,v)
	return g

# given a graph G and nodes i,j, output the length of the shortest
# path between i and j in G.
def shortest_path(G,i,j):
    return -1




def main():
	gr = create_graph(10,0.5)
	print(gr.nodes)
	print(gr.edges)
	


if __name__ == "__main__":
    main()