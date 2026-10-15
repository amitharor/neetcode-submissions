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
        left, right = 0, len(height) - 1
        l_wall, r_wall = height[left], height[right]
        results = 0
        i = 0
        while left < right:
            if l_wall < r_wall:
                left += 1
                l_wall = max(l_wall, height[left])
                results += l_wall - height[left]
            else:
                right -= 1
                r_wall = max(r_wall, height[right])
                results += r_wall - height[right]


        return results



# [6, 7, 3, 6, 4, 7]
        