'''
Input(s): arr (int) containing n+1
Output: return repeated int

Constraints:
1 <= n <= 10,000
nums.length == n + 1
1 <= nums[i] <= n

Approach:
slow and fast pointer
once slow and fast pointer meet; break out of loop
init another slow pointer (slow2) and iterate through loop
return slow when both slow pointers intersect

Time: O(n)
Space: O(1)
'''


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow