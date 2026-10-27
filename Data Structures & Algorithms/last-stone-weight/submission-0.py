'''
Input(s): arr(int)
Output: weight of last remaining stone or return 0 if none remain

Constraints:
1 <= stones.length <= 20
1 <= stones[i] <= 100


Approach:
max heap

Time: O(n log n)
Space: O(n)
'''

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones] #negate for max heap
        heapq.heapify(heap) #turn list into heap


        while len(heap) > 1:
            heaviest = -heapq.heappop(heap) #flip sign back
            second = -heapq.heappop(heap)
            print(heaviest, second)

            if heaviest != second:
                heapq.heappush(heap, -(heaviest - second))

        return -heap[0] if heap else 0
        