'''
Travelling Salesman Problem
Problem Statement: given a **complete graph with weighted edge** in and adjacency matrix, what is the path that visits each node once and return to the starting point, which also has the **minimum cost** ?
'''

def tspBF(graph, s):
    '''
    graph: is given as an adjacency matrix
    s: index of the source in the adjacency matrix 
    output: the cost of the shortest path to complete the entire route
    '''
    from itertools import permutations
    from sys import maxsize
    
    # identify vertexes that are not starting point
    # create all permutations of the vertexes 
    # example V = [1,2,3] => return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    
    V = [i for i in range(len(graph[0])) if i != s]
    V = list(permutations(V))
    
    # compare the min cost of all permutations
    minPath = maxsize  # initiate minPath value with the maximum integer in python sys
    
    for l in V: # O(n-1)! there are (n-1)! lists in V after the permutations 
        # calculate path cost
        c = 0
        k = s 
        for i in l: # O(n)
            c += graph[k][i]
            # update k to the next starting point
            k = i 
            
        # add cost of going back to starting point after the iteration
        c += graph[k][s] 
        minPath = min(c, minPath)
        
    return minPath


graph = [[0, 10, 15, 20], [10, 0, 35, 25],[15, 35, 0, 30], [20, 25, 30, 0]]

print(tspBF(graph,0))
print(tspBF(graph,1))
print(tspBF(graph,2))
print(tspBF(graph,3))