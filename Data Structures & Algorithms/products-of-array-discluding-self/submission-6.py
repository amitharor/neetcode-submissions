'''
Input(s): array int
Output: array of ints where each element is the product of all other elements except self

Constraints:
2 <= nums.length <= 100,000
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Time: O(n)
Space: O(n)

Approach:
init var to store left/right pointers
init var to store prefix/postfix
init var to store results

iterate through array
prefix will multiply every element before it
postfix will multiply every element after it


return result

'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        prefix = postfix = 1
        results = [1] * len(nums)

        while left < len(nums):
            # PREFIX
            results[left] *= prefix
            prefix *= nums[left]
            left += 1

            # POSTFIX
            results[right] *= postfix
            postfix *= nums[right]
            right -= 1

        return results