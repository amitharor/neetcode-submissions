'''
input: array (int), k (int)
output: array of largest elements from subarray at each step

constraints:
1 <= nums.length <= 100,000
-10,000 <= nums[i] <= 10,000
1 <= k <= nums.length


time: O(n)
space: O(n)

approach:
init var for left/right pointer
init var for deque
init var for results

iterate through array
# back
remove all elements from back if they are smaller than current el

add current index to deque

# front
check if first element in window is out of range; if so, remove it

if window size is == k; add first element from deque (largest) into results array

return results
'''


from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = deque()
        left = 0

        for right in range(len(nums)):
            while window and nums[window[-1]] <= nums[right]:
                window.pop()

            window.append(right)

            if window[0] <= right - k:
                window.popleft()

            if (right - left + 1) == k:
                results.append(nums[window[0]])
                left += 1
                

        return results