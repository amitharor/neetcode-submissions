'''
Input(s): arr (int)
Output: return len of longest strictly increasing subsequence

Constraints:
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000

Approach:
dp

Time: O(n^2)
Space: O(n)
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        chainLen = [1] * n # each num alone is a chain of 1

        for i in range(n):
            for j in range(i): # every index before i
                if nums[j] < nums[i]: # nums[i] can follow nums[j]
                    extendJ = chainLen[j] + 1
                    chainLen[i] = max(chainLen[i], extendJ)

        return max(chainLen)
        