# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3519/

class Solution:
    def findMinHeightTrees(self, n, edges):
        
        ''' 
        n: number of nodes (values of n start from 0 to n-1),
        edges: list of list of each node and it's connected node
        example: edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
        '''
        # create adjacency list of neighbor for each node
        # [{3}, {3},{3},{0,1,2,4}, {3,5}, {4}] means node 3 connects to node 0,1,2,4 etc
        if n == 1: return [0]
        elif n == 2: return edges[0]

        neighbors = [set() for _ in range(n)]
        for e1, e2 in edges:
            neighbors[e1].add(e2)
            neighbors[e2].add(e1)

        # create a list of leaves (leaves are nodes with only 1 neighbor)
        leaves = []
        for node in range(len(neighbors)): # node is the index of the neighbors list
            if len(neighbors[node]) == 1: 
                leaves.append(node)
        
        # then remove those leaves, add new leaves 
        # repeat the remove leaves process until 2 or less nodes remain. Those are roots of the MHT or the centroids of the graph

        while len(leaves) > 2: 
            newleaves = []
            while leaves: 
                leaf = leaves.pop()
                # leaf = 5, neighbor = 4, remove 5 in list of neighbors of 4
                #print('leaf', leaf)
                for neighbor in neighbors[leaf]:
                    #print(neighbors[neighbor])
                    neighbors[neighbor].remove(leaf)
                    if len(neighbors[neighbor]) == 1: # construct a list of nodes that remain 
                        newleaves.append(neighbor) 

            leaves = newleaves 

        return leaves 


sol = Solution()
print(sol.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
print(sol.findMinHeightTrees(2, [[0,1]]))
print(sol.findMinHeightTrees(1, [[]]))
        