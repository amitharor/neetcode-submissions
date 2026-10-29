'''
Input(s): arr of pos ints (int)
Output: bool; return True if we can partition the arr into two subsets wher sum(subset1) == sum(subset2); otherwise False

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 50

Approach:


Time: O(n * t) -> where t is the sum or array elements divided by 2
Space: O(t)
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False #odd total cannot be split in two equal halves

        target = total // 2 # one group must add up to exactly this
        reachable = {0} #sums we can make so far


        for num in nums:
            newReachable = set(reachable)
            for oldSum in reachable:
                newSum = oldSum + num

                if newSum == target:
                    return True # found group that hits half
                if newSum < target:
                    newReachable.add(newSum)
            reachable = newReachable

        return False