'''
Input(s): arr (int), target (int)
Output: return the fewest num of couns that you need to make up the exact target amount. return -1 if impossible.

Constraints:
1 <= coins.length <= 10
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10000

Approach:
dp

Time: O(n * t) -> where n is the len of arr and t is the given amount
Space: O(t)
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
            
        return dp[amount] if dp[amount] != amount + 1 else -1
        