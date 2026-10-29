'''
Input(s): n directed nodes (int), time (nest list of list(int)), k(int)
Output: return min time it takes for all of the n nodes to recieve signal. Return -1 if impossible

Constraints:
1 <= k <= n <= 100
1 <= times.length <= 1000

Approach:
Dijkstra's 

Time: O(E logV) -> where V is the num of vertices and E is the num of edges
Space: O(V + E)
'''

import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {node: [] for node in range(1, n + 1)} # building our graph: list of (neighbor, travel time)
        for source, target, travel in times:
            graph[source].append((target, travel))

        
        heap = [(0, k)] # (time to reach node, node) -> starting at k
        reached = {} # node -> fastest time id gets the signal

        while heap:
            time, node = heapq.heappop(heap)
            if node in reached:
                continue
            reached[node] = time # first pop is the fastest time

            for neighbor, travel in graph[node]:
                if neighbor not in reached:
                    heapq.heappush(heap, (time + travel, neighbor))

        if len(reached) < n:
            return -1 # some node didn't receive signal
        return max(reached.values()) # last node to recieve signal