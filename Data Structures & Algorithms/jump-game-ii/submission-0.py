'''
Input(s): arr (int)
Output: return min num of jumps to reach last position in arr

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 100

Approach:
dp - greedy

Time: O(n)
Space: O(1)
'''


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0 # keep track of jumps taken so far
        currentEnd = 0 # last index using jumps
        farthest = 0 # farthest index reachable using another jump

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == currentEnd:
                jumps += 1 
                currentEnd = farthest # next level ends here

        return jumps