'''
Input(s):
Output:

Constraints:


Approach:


Time: O()
Space: O()
'''

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)


        while low < high:
            mid = (low + high) // 2
            groups = 1
            currentSum = 0

            for value in nums:
                if currentSum + value > mid:
                    groups += 1
                    currentSum = value
                else:
                    currentSum += value

            if groups <= k:
                high = mid
            else:
                low = mid + 1

        return low

        