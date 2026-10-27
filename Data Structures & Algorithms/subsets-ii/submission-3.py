'''
Input(s): array (int)
Output: return all possible subsets

Constraints:
1 <= nums.length <= 11
-20 <= nums[i] <= 20

Approach:
backtracking


Time: O(n * 2^n)
Space: O(2^n)
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                result.append(subset[::])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return result