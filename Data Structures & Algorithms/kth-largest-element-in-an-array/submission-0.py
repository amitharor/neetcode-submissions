'''
Input(s): arr(int), k(int)
Output: return kth largest element

Constraints:
1 <= k <= nums.length <= 10000
-1000 <= nums[i] <= 1000

Approach:
min-heap

Time: O(n log k)
Space: O(n)
'''

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap) #drop the smallest; not top q
        
        return heap[0]