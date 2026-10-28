'''
Input(s): connected undirected graph
Output: return deep copy of graph

Constraints:
0 <= The number of nodes in the graph <= 100.
1 <= Node.val <= 100
There are no duplicate edges and no self-loops in the graph.


Approach:
DFS

Time: O(V + E)
Space: O(V)
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def clone(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy

        return clone(node) if node else None