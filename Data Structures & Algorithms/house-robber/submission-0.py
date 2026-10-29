'''
Input(s): arr (nums)
Output: return mac amount of money you can rob without alerting police

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100

Approach:
dp

Time: O(n)
Space: O(n)
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0] #only one house

        best = [0] * n
        best[0] = nums[0]
        best[1] = max(nums[0], nums[1])

        for i in range(2, n):
            skipHouse = best[i - 1]
            robHouse = best[i - 2] + nums[i]
            best[i] = max(skipHouse, robHouse)

        return best[n - 1]