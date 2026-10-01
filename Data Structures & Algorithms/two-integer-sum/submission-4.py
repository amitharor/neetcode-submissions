'''
input: int arr nums and int target
output: indices of i and j the sum up to target and not equal to each other (return smaller index first)

constraints: 
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
Only one valid answer exists.

edge case:

time: O(n)
space: O(1)

init var to store set

iterate through array
init var to store compliment number (target - current num)
if compliment in set;
return index of that stored num + index of current num
otherwise add index of num to set

return results
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            compliment = target - num

            if compliment in seen:
                return [seen[compliment], i]

            seen[num] = i

        return []