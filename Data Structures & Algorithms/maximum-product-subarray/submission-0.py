'''
Input(s): arr (int)
Output: find subarray that has the largest product, return product

Constraints:
1 <= nums.length <= 20,000
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

Approach:
kadane's strategy

Time: O(n)
Space: O(1)
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0] # biggest prod ending here
        currMin = nums[0] # smallest (most negative) 
        best = nums[0] # biggest prod seen
        

        for num in nums[1:]:
            startFresh = num
            extMax = num * currMax
            extMin = num * currMin #negative times negative can win
 
            newMax = max(startFresh, extMax, extMin)
            newMin = min(startFresh, extMax, extMin)
            currMax = newMax
            currMin = newMin

            best = max(best, currMax)

        return best