'''
input: implement medianFinader class
output: initialize object, addNum, findMedian

constraints:
-100,000 <= num <= 100,000
At most 50,000 calls will be made to addNum and findMedian.
findMedian will only be called after adding at least one integer to the data structure.


approach:
heap (priority queue)

time: O(m * log n)
space: O(n)


'''

import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return(-self.small[0] + self.large[0]) / 2
        