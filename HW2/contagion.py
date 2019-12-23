
import numpy as np
import collections as coll

# ans 8 a)
def contagion_brd(G, S, q):
    choice = {}
    for v in G:
        if v in S:
            choice[v] = 'X'
        else:
            choice[v] = 'Y'
    change_made = True
    while change_made:
        change_made = False
        for v in G:
            if choice[v] == 'X':
                continue       
            if sum([choice[u]=='X' for u in G[v]])/len(G[v]) >= q:
                choice[v] = 'X'
                change_made = True
    return choice

def make_graph():
    gr = coll.defaultdict(list)  
    with open('facebook_combined.txt') as file:
        for l in file:
            a, b = l.strip().split(' ')
            gr[int(a)].append(int(b))
            gr[int(b)].append(int(a))
    return dict(gr)

# testing 8 a) with figure 4.1
def test_4_1():
    G1 = {0: [1], 1: [0,2], 2: [1,3], 3:[2]}
    S1 = [0, 1]
    # complete cascade in left figure 4.1 can occur for any q <= 0.5
    print('Output of complete cascade:  ', contagion_brd(G1,S1,0.49)) # using value of q as 0.49
    # incomplete cascade in left figure 4.1 can occur for any q > 0.5
    print('Output of incomplete cascade:  ', contagion_brd(G1,S1,0.51)) # using value of q as 0.51
    G2 = {0: [1], 1: [0,2,3], 2: [1], 3:[1, 4, 5], 4:[3], 5:[3, 6], 6: [5]}
    S2 = [0, 1, 2]
    # complete cascade in right figure 4.1 can occur for any q <= 1/3
    q = 1/3
    print('Output of complete cascade:  ', contagion_brd(G2,S2,q)) # using value of q as 1/3
    # incomplete cascade in right figure 4.1 can occur for any q > 1/3
    print('Output of incomplete cascade:  ', contagion_brd(G2,S2,0.5)) # using value of q as 0.5

# ans 8 b)
def fb_data():
    G = make_graph()
    infected = []
    yes = 0
    q = 0.1
    for i in range(100):
        S = np.random.randint(0,4039,10)
        result = contagion_brd(G,S,q)
        inf = sum(result[x]=='X' for x in result)
        infected.append(inf)
        if inf == len(result):
            yes += 1
    if yes > 0:
        print('There is (are) {} complete cascade(s)'.format(yes))
    print('On average, {} nodes are infected'.format(sum(infected)/100))

# ans 8 c)

def q8c():
    G = make_graph()
    k_s = [x for x in range(0, 251, 10)] 
    q_s = [round(x*0.05,2) for x in range(0, 11)]    
    K, Q = 0, 0
    max_num = 0
    for k in k_s:
        for q in q_s:
            complete = 0
            for i in range(10):
                S = np.random.randint(0, 4039, k)
                result = contagion_brd(G,S,q)
                if sum(result[x]=='X' for x in result) == len(result):
                    complete += 1
            if complete > max_num:
                K, Q = k, q
                max_num = complete
    print('For values k:{}, q:{}, a complete cascade is likely - has {} complete cascades by testing'.format(K, Q, max_num))