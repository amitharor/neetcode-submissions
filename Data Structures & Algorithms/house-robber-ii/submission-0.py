'''
Input(s): arr (int)
Output: return max amt of money you can rob without alerting police

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 200

Approach:
dp - bottom up

Time: O(n)
Space: O(n)
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        skipFirst = self.robLine(nums[1:])
        skipLast = self.robLine(nums[:-1])
        return max(skipFirst, skipLast)


    def robLine(self, houses):
        bestTwoBack = 0
        bestOneBack = 0

        for money in houses:
            robIt = money + bestTwoBack
            skipIt = bestOneBack
            bestToday = max(robIt, skipIt)
            bestTwoBack = bestOneBack
            bestOneBack = bestToday
        
        return bestOneBack