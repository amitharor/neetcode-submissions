'''
Input(s): arr (int)
Output: return max num of coins you can receive by bursting all of the balloons.

Constraints:
n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100

Approach:
dp

Time: O(n^3)
Space: O(n^2)
'''


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1] # pad edges with 1 so neighbors always exist
        n = len(balloons)

        maxCoins = [[0] * n for _ in range(n)]


        for gap in range(2, n):
            for left in range(0, n - gap):
                right = left + gap
                best = 0

                for last in range(left + 1, right):

                    burstLast = balloons[left] * balloons[last] * balloons[right]
                    leftSide = maxCoins[left][last]
                    rightSide = maxCoins[last][right]
                    best = max(best, leftSide + burstLast + rightSide)
                
                maxCoins[left][right] = best

        return maxCoins[0][n - 1]