'''
Input(s): 2d int arr
Output: return min cost to connect all points together

Constraints:
1 <= points.length <= 1000
-1,000,000 <= xi, yi <= 1,000,000
All pairs (xi, yi) are distinct.


Approach:
Prim's -> MST

Time: O(n^2 log n)
Space: O(n^2)
'''

import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        connected = set()
        heap = [(0, 0)]
        total = 0


        while len(connected) < n:
            cost, i = heapq.heappop(heap) # cheapest link out of the group
            if i in connected:
                continue #already joined by a cheaper link

            connected.add(i)
            total += cost


            x1, y1 = points[i]
            for j in range(n):
                if j not in connected:
                    x2, y2 = points[j]
                    distance = abs(x1 - x2) + abs(y1 - y2) #manhattan distance
                    heapq.heappush(heap, (distance, j))

        return total