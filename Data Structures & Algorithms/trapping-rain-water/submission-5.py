'''
input: array of positive nums (int)
output: total amount of trapped water

constraints:
1 <= height.length <= 20,000
0 <= height[i] <= 100,000

time: O(n)
space: O(1)


approach:
init left/right pointers starting at opposite sides
init vars to get the height of left/right walls (store max height)
init var to store results


iterate through array
if left wall smaller than right wall; increment left wall and update left wall heigt if greater than previously stored val


otherwise, decrement right wall and update right wall height if > prev stored val
update results total with height (min of left/right wall) - current index iff > 0

return results

'''


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_wall, right_wall = height[l], height[r]
        results = 0

        while l < r:
            if left_wall < right_wall:
                l += 1
                left_wall = max(left_wall, height[l])
                results += left_wall - height[l]

            else:
                r -= 1
                right_wall = max(right_wall, height[r])
                results += right_wall - height[r]

        return results
        