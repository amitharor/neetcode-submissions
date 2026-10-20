'''
Input(s): arr (int) containing n+1
Output: return repeated int

Constraints:
1 <= n <= 10,000
nums.length == n + 1
1 <= nums[i] <= n

Approach:



Time: O()
Space: O()
'''


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        repeated = Counter(nums)

        for num, freq in repeated.items():
            if freq > 1:
                return num