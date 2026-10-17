'''
input: array (int), target(int)
output: indices of two nums that sum up to target (1-indexed)

constraints:
2 <= numbers.length <= 30000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000


time: O(n)
space: O(1)

approach:
init left/right pointer starting at both ends
init var to store results



iterate through array
init var to keep track of current total

if total > target then decrement right pointer
if total < target then increment left pointer
if total == target then return the index of both values


return results
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:

            total = numbers[left] + numbers[right]

            if total > target:
                right -= 1
            
            if total < target:
                left += 1

            if total == target:
                return [left +1, right + 1]
            
            