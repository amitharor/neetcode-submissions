'''
input: arr (int)

output: index of peak element that is greater than its neighbors

constraints: 
1 <= nums.length <= 1000.
-(2^31) <= nums[i] <= ((2^31)-1)
nums[i] != nums[i + 1] for all valid i.

approach: 
binary search

time: O(log n)
space: O(1)
'''


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) >> 1

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left