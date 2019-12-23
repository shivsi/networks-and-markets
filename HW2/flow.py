from random import random
import matplotlib.pyplot as plt

def max_flow(G, cap, s, t):
    flow = {}
    for e in cap:
        flow[tuple(reversed(e))] = 0
    path = dfs(G, s, t, cap)
    while path:
        path = exists(path)
        residual_capacity = min(cap[(u, v)] for u, v in path)
        for u, v in path:
            cap[(u, v)] -= residual_capacity
            flow[(v, u)] += residual_capacity
        path = dfs(G, s, t, cap)
    return sum(flow[(u,s)] for u in G[s]), flow

def dfs(G, s, t, cap):
    stack = [[s]]
    while stack:
        p = stack.pop()
        node = p[-1]
        for u in G[node]:
            if cap[(node, u)] > 0:
                if u == t:
                    return p + [u]
                stack.append(p+[u])
    return None
    
def exists(path):
    ret = []
    for i in range(len(path)-1):
        ret.append((path[i], path[i+1]))
    return ret

# 9 a) 
def test_6_1():
    G = {0:[1, 2], 1:[2, 3], 2:[3], 3:[]}
    s, t = 0, 3
    cap = {(0,1):1, (0,2):3, (1,2):2, (1,3):1, (2,3):1}
    print('Expected:', 2)
    print('Actual  :', max_flow(G, cap, s, t)[0])
    
def test_6_3():
    G = {}
    for i in range(12):
        G[i] = []
    G[1].append(7)
    G[2].append(6)
    G[2].append(7)
    G[3].append(6)
    G[4].append(8)
    G[4].append(10)
    G[5].append(8)
    G[5].append(9)
    for i in range(1, 6):
        G[0].append(i)
    for i in range(6, 11):
        G[i].append(11)
    s, t, = 0, 11
    cap = {}
    for u in G:
        for v in G[u]:
            cap[(u,v)] = 1
    print('Expected:', 4)
    print('Actual:  ', max_flow(G, cap, s, t)[0])

# 9 c)
def construct_graph(p, n, m):
    s = 0
    t = m + n + 1
    cap = {}
    G = {}
    for i in range(m+n+2):
        G[i] = []
    for i in range(1, n+1):
        G[s].append(i)
        cap[(s, i)] = 1
        for j in range(n+1, n+m+1):
            if random() < p:
                G[i].append(j)
                cap[(i,j)] = m+n+2 
    for i in range(n+1, n+m+1):
        G[i].append(t)
        cap[(i, t)] = 1   
    return G, cap, s, t
  
def max_matching(p, n, m):
    G, cap, s, t = construct_graph(p, n, m)
    flow = max_flow(G, cap, s, t)[1]
    ans = []
    for i in range(1, n+1):
        for j in range(n+1, n+m+1):
            try:
                if flow[(j, i)] > 0:
                    ans.append((i, j))
            except:
                continue
    return ans

def testing1():
    n = m = 5
    print('Result: ', max_matching(1, n, m))

def testing2():
    n = 10
    m = 15
    print('Result: ', max_matching(1, n, m))
    
# 9 d)
def ans():
    n = 100
    m = 100
    p_s = [round(x*0.001,2) for x in range(0, 1000)]
    prob = []
    for p in p_s:
        count = 0
        num_trial = 800
        for i in range(num_trial):
            connections = max_matching(p, n, m)
            count = count + 1 if len(connections) == m else count
        prob.append(count/num_trial)
    plt.plot(p_s, prob)
    plt.xlabel('Prob p')
    plt.ylabel('Prob of all riders being matched')
    plt.show()