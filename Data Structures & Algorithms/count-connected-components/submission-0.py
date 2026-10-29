'''
Input(s): undirected graph of n node. n (int) edges - nest arr(int)
Output: return num of connected components in graph


Constraints:
1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= aᵢ < n
0 <= bᵢ < n
aᵢ != bᵢ
There are no repeated edges.


Approach:


Time: O(V + E) - where V is num of vertices and E is num of edges
Space: O(V + E)
'''


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # Building graph - adjacency list of neighbors
        graph = {node: [] for node in range(n)}
        
        for a, b in edges:
            graph[a].append(b) # undirected: both directions
            graph[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited: # already part of a counted group
                return
            
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor) # marking everything connected to this node

        components = 0
        for node in range(n):
            if node not in visited: # a node no earlier search reached
                components += 1 # so it starts a new group
                dfs(node) # marking the whole group as visited

        return components