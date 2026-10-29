'''
Input(s): n (int)
Output: return num of distinct ways to climb to the top of staircase

Constraints:
1 <= n <= 45


Approach:
fibonacci sequence -> dp

Time: O(n)
Space: O(n)
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n # base case

        ways = [0] * (n + 1)
        ways[1] = 1 # just one step
        ways[2] = 2

        for step in range(3, n + 1):
            ways[step] = ways[step - 1] + ways[step - 2]

        return ways[n]