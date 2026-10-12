'''
input: array (int), target (int)
output: return indices of two nums that sum up to target; cannot be same index

constraints:
2 <= numbers.length <= 30000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000


time: (n)
space: O(1)

approach:
init left and right pointers starting at each end and traversing inwards
if the sum of elements at left and right index > target; then decrement right pointer to decrease sum
    otherwise; increment left pointer to increase sum
if sum of elements == target; return left and right pointers (in that order) + 1 (1-indexed)
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            
            if total < target:
                left += 1
            
            if total > target:
                right -= 1

            if total == target:
                return [left + 1, right + 1]
