'''
Input(s): 2d arr(int), arr (int)
Output: return arr where output[j] is the result of query[j]

Constraints:
1 <= intervals.length <= 100000
1 <= queries.length <= 100000
1 <= left_i <= right_i <= 10000000
1 <= queries[j] <= 10000000

Approach:
sort intervals and queries -> min heap of size and end


Time: O(n log n)
Space: O(n)
'''

import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort() # by start
        heap = []
        answerFor = {}
        i = 0


        for query in sorted(queries): # smallest query first
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                heapq.heappush(heap, (right - left + 1, right))
                i += 1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            answerFor[query] = heap[0][0] if heap else -1

        return [answerFor[query] for query in queries]