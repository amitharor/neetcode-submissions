'''
Input(s): array (int) sorted in asc ord. target (int)
Output: return index of target in input array if found; else return -1

Constraints:
1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
All the integers in nums are unique.

Approach:
init left/right pointers
iterate through array
init middle pointer

if el at middle pointer == target then return index
else if el at middle point < target; move left point to middle + 1
else move right pointer to middle -1

return -1

Time: O(log n)
Space: O(1)
'''


class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1