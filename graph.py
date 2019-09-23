# include any code you need for your assignment in this file or in auxiliary
# files that can be imported here.
import random as rnd 
import networkx as nx
from itertools import combinations as cmb
import heapq
from matplotlib import pyplot as plt

# given number of nodes n and probability p, output a random graph 
# as specified in homework
def create_graph(n,p):
	nodes = range(n)
	g = nx.Graph()
	g.add_nodes_from(nodes)
	for u,v in cmb(g,2):
		if rnd.random() < p:
			g.add_edge(u,v)
	return g

# given a graph G and nodes i,j, output the length of the shortest
# path between i and j in G.
def shortest_path(G,i,j):
	seen = set()
	seen.add(i)
	smallest = {}
	smallest[i] = 0
	unvisited = []
	heapq.heappush(unvisited, (0,i))
	while unvisited:
		chk = heapq.heappop(unvisited)
		if j == chk[1]:
			return chk[0]
		nbrs = G.neighbors(chk[1])
		for x in nbrs:
			if x in seen:
				continue
			else:
				seen.add(x)
				heapq.heappush(unvisited, (chk[0]+1,x))
				smallest[x] = chk[0]+1
	return "infinity"

# averaging across 1000 randomly selected nodes
def avg_shortest_path(mygraph):
	distances = []
	while len(distances) != 1000:
		start, end = rnd.sample(range(1000), 2)
		dist = shortest_path(mygraph,start,end)
		if dist == "infinity":
			continue
		distances.append(dist)
# 		print("("+str(start)+","+str(end)+","+str(dist)+")")
	return (sum(distances)/len(distances))

# Check if graph is connected
def conn(G):
	if len(G.nodes)-1 > len(G.edges) or len(G.nodes)==0:
		return False
	seen = set()
	num = list(G.nodes)
	seen.add(num[0])
	unvisited = set()
	unvisited.add(num[0])
	while unvisited:
		chk = unvisited.pop()
		nbrs = G.neighbors(chk)
		for x in nbrs:
			if x in seen:
				continue
			else:
				seen.add(x)
				unvisited.add(x)
	for x in G.nodes:
		if x not in seen:
			return False
	return True

# Question 8 c,d - need conn graph
def gen_conn_graph(n,p):
	G = create_graph(n, p)
	while not conn(G):
		G = create_graph(n, p)
	return G

# Question 8 d
def ans8d():
	avg_sp = []
	ps = [0.01, 0.02, 0.03, 0.04, 0.05, 0.1, 0.15, 0.2 ,0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
	for p in ps:
		G = gen_conn_graph(1000,p)
		avg_sp.append(avg_shortest_path(G))
	plt.plot(ps,avg_sp)
	plt.show()

def main():
	# gr = create_graph(5,0.5)
	# print("Nodes:")
	# print(gr.nodes)
	# print("Edges:")
	# print(gr.edges)
	# print(conn(gr))
	# for i in range(10):
	# 	gr = create_graph(1000,0.5)
	# 	print(avg_shortest_path(gr))
	


if __name__ == "__main__":
    main()