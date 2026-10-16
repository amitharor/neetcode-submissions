'''
input: array (int)
output: bool; True is any val appears more than once; else False

constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9


time: O()
space: O()


approach:
init set for input array to get unique chars
compare len of set with len of original array; if same len then return False as there were no dups; else True

'''


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)