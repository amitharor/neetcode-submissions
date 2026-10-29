'''
Input(s): n (num), list(next list (int))
Output: bool; return true if edges make valid tree; else false

Constraints:
1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= a_i, b_i < n
a_i != b_i
There are no self-loops or repeated edges.


Approach:
DFS - cycle detection

Time: O(V + E) - where V is the num of vertices and E is the num of edges in the graph
Space: O(V + E)
'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: # more edges would mean a cycle and fewer would mean something is disconnected
            return False

        # build graph (adjacency list)
        graph = {node: [] for node in range(n)}
        for a, b in edges:
            graph[a].append(b) # undirected; edges added both ways
            graph[b].append(a)

        visited = set()
    
        def dfs(node):
            if node in visited: # already reached it; don't loop forever
                return

            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor) # reach everything connected to this node
        
        dfs(0)

        return len(visited) == n