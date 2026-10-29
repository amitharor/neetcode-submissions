'''
Input(s): connected undirected graph (nested list(int)). 
Output: return an edfe that can be removed so that the graph is still connected in a non-cyclical graph

Constraints:
n == edges.length
3 <= n <= 1000
1 <= edges[i][0] < edges[i][1] <= edges.length
There are no repeated edges and no self-loops in the input.

Approach:


Time: O()
Space: O()
'''

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))


        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]] #shortcut to point to grandparent
                node = parent[node]

            return node
        
        for a, b in edges:
            captainA = find(a)
            captainB = find(b)

            if captainA == captainB:
                return[a,b] # already connected; this edge makes loop

            parent[captainA] = captainB #merging the two teams       