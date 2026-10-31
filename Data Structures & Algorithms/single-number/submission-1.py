'''
Input(s): arr (int)
Output: return the int that appears only once

Constraints:
1 <= nums.length <= 10000
-10000 <= nums[i] <= 10000

Approach:
bit manipulation

Time: O(n)
Space: O(1)
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num

        return result