'''
Input(s): 2d arr (list of points), k (int)
Output: k closest points to the origin (0, 0)

Constraints:
1 <= k <= points.length <= 1000
-100 <= points[i][0], points[i][1] <= 100

Approach:
min heap

Time: O(n + k log n)
Space: O(n)
'''

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            heap.append((distance, x, y))
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            distance, x, y = heapq.heappop(heap)
            result.append([x, y])


        return result