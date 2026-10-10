'''
input: int array

output: bool; true if any val appears more than once; otherwise false

constraints: 
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

time: O()

space: O()

we can use a set to get all unique values in the input array.
compare the len of the set vs the input array. If the size is not the same (contains duplicate) then return True; otherwise False
'''


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)