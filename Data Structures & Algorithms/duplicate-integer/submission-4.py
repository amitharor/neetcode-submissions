'''
input: nums array
output: bool - return t if any val appears more than once in arr, otherwise return f

constraints:
-> 0 <= nums.length <= 10^5
-> -10^9 <= nums[i] <= 10^9

time: O(n)
space: O(n)

create a new array set from og array
compare len of two array
if len is not same ret T, else ret F

'''


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # print(len(set(nums)))
        # print(len(nums))

        return len(set(nums)) != len(nums)
