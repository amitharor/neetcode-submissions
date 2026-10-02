'''
i: int arr
o: array of product of all element of nums except self

constraints:
2 <= nums.length <= 100,000
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

edge:

time: O(n)
space: O(1)

two pointer?

init left and right pointers (start and end of array)
iterate through the loop and 

'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        results = [1] * length
        prefix, postfix = 1, 1
        left, right = 0, length - 1

        while left < length:
            results[left] *= prefix
            prefix *= nums[left]
            
            results[right] *= postfix
            postfix *= nums[right]
            
            left += 1
            right -= 1

        return results