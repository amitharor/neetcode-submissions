'''
i: arr int nums + int target
o: return indices of i and j == target. i != j. return smaller index first

constraints: 
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
Only one valid answer exists.

edge:

time: 
space:

init var to store hash map of seen nums

iterate through array
init var to store compliment num (target - curr num)
check if compliment num exists in hashmap:
    if so, return of num in hash map and index of curr num
add curr num and index to hash map
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