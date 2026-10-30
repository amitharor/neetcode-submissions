'''
Input(s): arr (int)
Output: bool; return True if you can reach the last index starting from index 0, else False

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 1000

Approach:
dp - greedy

Time: O(n)
Space: O(1)
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i, jump in enumerate(nums):
            if i > farthest:
                return False

            farthest = max(farthest, i + jump)
        
        return True