'''
Input(s): arra (int)
Output: max amt of water that the container can hold (int)

Constraints:

Time: O(n)
Space: O(1)

Approach:
init var to store results
init left/right pointers

iterate through the input array
init var to store width between left and right pointers
init var to store height which will be the minimum of the two elements
store capacity into results variable which will be width x height
move the smaller of the two pointers (left or right) and keep calculating and only store the capacity if greater than currently stored val in results

return results
'''

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        results = 0
        left, right = 0, len(heights) - 1


        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            results = max(results, width * height)

            # print(f'w:{width} h:{height} r:{results}')

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1


        return results