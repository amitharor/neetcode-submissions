'''
Input(s): arr (int)
Output: return single num in the range that is missing from nums

Constraints:
1 <= nums.length <= 1000

Approach:
XOR every index 0..n with every val

Time: O(n)
Space: O(1)
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n

        for i, num in enumerate(nums):
            result ^= i ^ num
        
        return result
        