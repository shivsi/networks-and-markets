import numpy as np
# Please enter here the netids of all memebers of your group (yourself included.)
authors = ['amp453','nc532','aks298','sj747']

# Which version of python are you using? python 2 or python 3? 
python_version = "Python3"

# Important: You are NOT allowed to modify the method signatures (i.e. the arguments and return types each function takes).

# Implement the methods in this class as appropriate. Feel free to add other methods
# and attributes as needed. 
# Assume that nodes are represented by indices between 0 and number_of_nodes - 1
class DirectedGraph:
    
    def __init__(self,number_of_nodes):
        self.graph = {}
        self.node_set = np.arange(number_of_nodes)
        self.n = number_of_nodes
    
    def add_edge(self, origin_node, destination_node):
        if origin_node not in self.graph:
            self.graph[origin_node] = []

        if destination_node in self.graph[origin_node]:
            return

        self.graph[origin_node].append(destination_node)

    
    def edges_from(self, origin_node):
        ''' This method shold return a list of all the nodes u such that the edge (origin_node,u) is 
        part of the graph.'''
        if origin_node not in self.graph:
            return []

        return self.graph[origin_node]
    
    def check_edge(self, origin_node, destination_node):
        ''' This method should return true is there is an edge between origin_node and destination_node
        and destination_node, and false otherwise'''
        if origin_node not in self.graph or (destination_node not in self.graph[origin_node]):
            return False

        return True
    
    def number_of_nodes(self):
        ''' This method should return the number of nodes in the graph'''
        return self.n

    def get_nodes(self):
        return list(self.node_set)

    def get_adj_list(self):
        return self.graph
    
def scaled_page_rank(graph, num_iter, eps = 1/7.0):
    ''' This method, given a directed graph, should run the epsilon-scaled page-rank
    algorithm for num-iter iterations and return a mapping (dictionary) between a node and its weight. 
    In the case of 0 iterations, all nodes should have weight 1/number_of_nodes'''    
    
    nodes = graph.get_nodes()
    ranks = {}

    for node in nodes:
        ranks[node] = 1 / float(len(nodes))
    

    for _ in range(num_iter):
        for node1 in nodes:
            rank = 0
            incoming_nodes = []
            for node2 in nodes:
                if graph.check_edge(node2,node1):
                    incoming_nodes.append(node2)

            for in_node in incoming_nodes:
                out_deg = len(graph.edges_from(in_node))
                if out_deg == 0:
                    continue
                rank += (ranks[in_node] / float(out_deg))

            rank *= (1 - eps)
            rank += (eps / len(nodes))

            ranks[node1] = rank

    return ranks



def graph_15_1_left():
    ''' This method, should construct and return a DirectedGraph encoding the left example in fig 15.1
    Use the following indexes: A:0, B:1, C:2, Z:3 '''  
    G = DirectedGraph(4)
    G.add_edge(3,3)
    G.add_edge(0,3)
    G.add_edge(0,1)
    G.add_edge(1,2)
    G.add_edge(2,0)  
    
    return G

def graph_15_1_right():
    ''' This method, should construct and return a DirectedGraph encoding the right example in fig 15.1
    Use the following indexes: A:0, B:1, C:2, Z1:3, Z2:4'''    
    
    G = DirectedGraph(5)
    G.add_edge(3,4)
    G.add_edge(4,3)
    G.add_edge(0,3)
    G.add_edge(0,4)
    G.add_edge(0,1)
    G.add_edge(1,2)
    G.add_edge(2,0)  
    
    return G

def graph_15_2():
    ''' This method, should construct and return a DirectedGraph encoding example 15.2
        Use the following indexes: A:0, B:1, C:2, A':3, B':4, C':5'''

    G = DirectedGraph(6)

    G.add_edge(0,1)
    G.add_edge(1,2)
    G.add_edge(2,0)    

    G.add_edge(3,4)
    G.add_edge(4,5)
    G.add_edge(5,3)

    return G


def extra_graph_1():
    ''' This method, should construct and return a DirectedGraph of your choice with at least 10 nodes
        0:A,B:1,C:2,D:3,E:4,F:5,G:6,H:7,I:8,J:9
    '''    
    G = DirectedGraph(10)

    G.add_edge(0,1)
    G.add_edge(1,2)
    G.add_edge(2,3)    
    G.add_edge(3,1)
    G.add_edge(1,4)
    G.add_edge(4,5)
    G.add_edge(5,1)
    G.add_edge(6,5)
    G.add_edge(7,8)
    G.add_edge(8,1)
    G.add_edge(9,8)

    return G

# This dictionary should contain the expected weights for each node when running the scaled page rank on the extra_graph_1 output
# with epsilon = 0.07 and num_iter = 20.
extra_graph_1_weights = {1 : 0, 2: 0, 3 : 0, 4: 0, 5 : 0, 6: 0, 7 : 0, 8: 0, 9 : 0}

def extra_graph_2():
    ''' This method, should construct and return a DirectedGraph of your choice with at least 10 nodes'''    
    
    G = DirectedGraph(10)

    G.add_edge(1,0)
    G.add_edge(1,1)
    G.add_edge(2,3)    
    G.add_edge(3,1)
    G.add_edge(1,4)
    G.add_edge(0,5)
    G.add_edge(5,1)
    G.add_edge(6,5)
    G.add_edge(7,1)
    G.add_edge(0,0)
    G.add_edge(9,0)

    return G

# This dictionary should contain the expected weights for each node when running the scaled page rank on the extra_graph_2 output
# with epsilon = 0.07 and num_iter = 20.
extra_graph_2_weights = {1 : 0, 2: 0, 3 : 0, 4: 0, 5 : 0, 6: 0, 7 : 0, 8: 0, 9 : 0}


def facebook_graph(filename = "facebook_combined.txt"):
    ''' This method should return a DIRECTED version of the facebook graph as an instance of the DirectedGraph class.
    In particular, if u and v are friends, there should be an edge between u and v and an edge between v and u.'''    
    fp = open(filename, 'r')
    G = DirectedGraph(4039)
    for line in fp:
        line = line.split(' ')
        line[0] = int(line[0])
        line[1] = int(line[1].rstrip())

        G.add_edge(line[0],line[1])
        G.add_edge(line[1],line[0])

    return G



# The code necessary for your measurements for question 8b should go in this function.
# Please COMMENT THE LAST LINE OUT WHEN YOU SUBMIT (as it will be graded by hand and we do not want it to interfere
# with the automatic grader).
def question8b():

    G1 = graph_15_1_left()
    G2 = graph_15_1_right()
    G3 = graph_15_2()
    G4 = extra_graph_1()
    G5 = extra_graph_2()

    print('graph_15_1_left PR:', scaled_page_rank(G1,100))
    print('graph_15_1_right PR:', scaled_page_rank(G2,100))
    print('graph_15_2 PR:', scaled_page_rank(G3,100))
    print('extra_graph_1 PR:', scaled_page_rank(G4,100))
    print('extra_graph_2 PR:', scaled_page_rank(G5,100))


def question9():
    G_fb = facebook_graph()
    weights = scaled_page_rank(G_fb,10)

    with open('q9.txt','w+') as fp:
        fp.write(str(weights))


question8b()
question9()

# G6 = DirectedGraph(8)
# G6.add_edge(0,1)
# G6.add_edge(1,0)
# G6.add_edge(0,2)
# G6.add_edge(2,0)
# G6.add_edge(0,3)
# G6.add_edge(3,0)
# G6.add_edge(3,7)
# G6.add_edge(7,3)
# G6.add_edge(7,4)
# G6.add_edge(4,7)
# G6.add_edge(4,5)
# G6.add_edge(5,4)
# G6.add_edge(4,6)
# G6.add_edge(6,4)

# print(scaled_page_rank(G6,20))