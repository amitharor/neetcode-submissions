'''
Input(s): int array and int target
Output: array of indices of two nums that add up to targer and i != j

Constraints:
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
Only one valid answer exists.

Time: O(n)
Space: O(n)

Approach:

we can use a hash map to store all nums and it's index position we have seen
get the compliment of the target (targer num - current num) and check to see if exists in hash map
    if so; return index of that plus the index of current num
    otherwise; store the current num and index into hash map
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}


        for i, num in enumerate(nums):
            compliment = target - num

            if compliment in seen:
                return [seen[compliment], i]
            else:
                seen[num] = num