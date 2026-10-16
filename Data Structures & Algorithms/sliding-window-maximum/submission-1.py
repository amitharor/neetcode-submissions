'''
input: array (int), k (int)
output: array of max el at each window

constraints:
1 <= nums.length <= 100,000
-10,000 <= nums[i] <= 10,000
1 <= k <= nums.length


time: O(n)
space: O(1)

approach:
init left/right pointers
int var to store results
init var for deque to store indices from big to small

iterate through array

recursively remove the last elements from deque if smaller than current value
add element to deque
if the first element is out of window, popleft
if window is the size of k; append the first num from deque (largest) to results

return results

'''

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        line = deque()

        for i, num in enumerate(nums):
            # back rule: smaller vals leave
            while line and nums[line[-1]] <= num:
                line.pop()

            line.append(i)

            # front rule: front el left the window
            if line[0] <= i - k:
                line.popleft()

            if i >= k - 1:
                results.append(nums[line[0]])

        return results