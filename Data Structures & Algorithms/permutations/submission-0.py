'''
Input(s): arr (int)
Output: return all possible permutations

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10

Approach: 
backtracking

Time: O(n! * n)
Space: O(n! * n)
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        used = [False] * len(nums)

        def backtrack():
            if len(current) == len(nums):
                result.append(current.copy())
                return


            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                current.append(nums[i])
                backtrack()
                current.pop()
                used[i] = False


        backtrack()
        return result