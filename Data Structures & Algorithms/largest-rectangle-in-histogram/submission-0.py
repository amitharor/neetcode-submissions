'''
input: arr (int)
output: area of largest rectangle that can be formed among the bars

constraints:
1 <= heights.length <= 100,000.
0 <= heights[i] <= 10,000


approach:
init stack
init  var to track max area

iterate through array


time: O(n)
space: O(n)

'''


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea









        