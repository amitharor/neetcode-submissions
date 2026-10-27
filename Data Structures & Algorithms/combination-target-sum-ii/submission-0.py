'''
Input(s): arr (int), target (int)
Output: nested arr of unique combinations summing up to target

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

Approach:
backtracking

Time: O(n * 2^n)
Space: O(n)
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        current = []

        def backtrack(index, total):
            if total == target:
                result.append(current.copy())
                return

            if index == len(candidates) or total > target:
                return

            current.append(candidates[index])
            backtrack(index + 1, total + candidates[index])
            current.pop()

            nextIndex = index + 1
            while nextIndex < len(candidates) and candidates[nextIndex] == candidates[index]:
                nextIndex += 1
            
            backtrack(nextIndex, total)
        
        backtrack(0, 0)
        return result