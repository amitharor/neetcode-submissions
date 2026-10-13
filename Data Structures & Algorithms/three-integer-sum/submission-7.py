'''
Input(s): array (int)
Output: list of all triplets that sum to 0; distinct indices

Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5


Time: O(n^2)
Space: O(n)

Approach:
sort array
init results variable

iterate through sorted array
increment initial pointer if same num as prev element

init left and right pointers to i + 1 and end of sorted array
iterate left and right pointers
init var to store total of elements at i, left, and right

if < 0; then increment left pointer
if > 0; decrement right pointer
otherwise append the three nums to results

    increment left
    decrement right
    keep moving left pointer if element is same as prev element

return results
'''


class Solution:
    def threeSum (self, nums):
        nums.sort()
        results = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return results
        