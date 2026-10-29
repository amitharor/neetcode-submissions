'''
Input(s): arr (int)
Output: return min cost to reach the top of the staircase (just past the last index in array)

Constraints:
2 <= cost.length <= 100
0 <= cost[i] <= 100

Approach:
dp

Time: O(n)
Space: O(n)
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCost = [0] * (n + 1)

        for i in range(2, n + 1):
            oneBelow = minCost[i - 1] + cost[i -1] # pay for i-1, step 1
            twoBelow = minCost[i - 2] + cost[i - 2] # pay for i-2, step 2
            minCost[i] = min(oneBelow, twoBelow)

        return minCost[n] # cheapest way to the top