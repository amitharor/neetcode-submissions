'''
Input(s): arr (int)
Output: return sum of largest subarray

Constraints:
1 <= nums.length <= 100,000
-10,000 <= nums[i] <= 10,000

Approach:
greedy - kadane's algo

Time: O(n)
Space: O(n)
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        best = nums[0]

        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            best = max(best, currentSum)

        return best