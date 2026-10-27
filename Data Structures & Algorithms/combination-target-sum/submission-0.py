'''
Input(s): arr (int), targt (int)
Output: return list of all unique combinations of nums where the chose nums sum to target

Constraints:
All elements of nums are distinct.
1 <= nums.length <= 20
2 <= nums[i] <= 30
2 <= target <= 30

Approach:


Time: O(2^(t/m))
Space: O(t/m)
'''

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []


        def backtrack(index, total):
            if total == target:
                result.append(current.copy())
                return
            if index == len(nums) or total > target:
                return

            
            current.append(nums[index])
            backtrack(index, total + nums[index])
            current.pop()

            backtrack(index + 1, total)

        backtrack(0, 0)
        return result
        