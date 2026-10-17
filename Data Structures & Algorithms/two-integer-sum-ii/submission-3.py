'''
input: sorted array [int], target [int]
output: indices of two nums that sum up to target -> 1 indexed

constraints:
2 <= numbers.length <= 30000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000

approach:
init left/right pointers
init var to store results

iterate through array
init total var to be sum of nums at left and right pointers
if total < target then increment left pointer to increase total
if total > target then decrement right pointer to decrease total
if total == target then return the indices (1 index)


time: O(n)
space: O(1)

'''


class Solution:
	def twoSum(self, numbers, target):
		left, right = 0, len(numbers) - 1

		while left < right:
			total = numbers[left] + numbers[right]
			
			if total < target:
				left += 1
			elif total > target:
				right -= 1
			else:
				return [left + 1, right + 1]
