'''
Input(s): rectangular island heights where heights[r][c] represents the height above sea level
Output: find all cells where water can flow from that cell to BOTH the Pacific and Atlantic oceans

Constraints:
1 <= heights.length, heights[r].length <= 100
0 <= heights[r][c] <= 1000


Approach:
DFS


Time: O(n * m)
Space: O(n * m)
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(row, col, reached, prevHeight):
            if ((row, col) in reached or
                row < 0 or
                col < 0 or
                row >= ROWS or
                col >= COLS or
                heights[row][col] < prevHeight
                ):
                return # visited, off grid, or downhill

            reached.add((row, col))
            height = heights[row][col]
            dfs(row + 1, col, reached, height) #keep climbing
            dfs(row - 1, col, reached, height)
            dfs(row, col + 1, reached, height)
            dfs(row, col - 1, reached, height)


        for col in range(COLS):
            dfs(0, col, pacific, heights[0][col]) #top edge
            dfs(ROWS - 1, col, atlantic, heights[ROWS - 1][col]) #bottom edge
        for row in range(ROWS):
            dfs(row, 0, pacific, heights[row][0]) #left edge
            dfs(row, COLS - 1, atlantic, heights[row][COLS - 1]) #right edge

        return [[row, col] for row, col in pacific & atlantic]

