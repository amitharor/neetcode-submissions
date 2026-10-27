'''
Input(s): nums arr (int)
Output: return all subsets of nums

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10

Approach:
backtracking

Time: O(n * 2^n)
Space: O(n)
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def backtrack(index):
            if index == len(nums):
                result.append(current.copy())
                return

            current.append(nums[index])
            backtrack(index + 1)
            current.pop()

            backtrack(index + 1)

        backtrack(0)
        return result