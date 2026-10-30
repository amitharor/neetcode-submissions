'''
Input(s): arr (int), amount (int)
Output: return num of dist combination that sum up to amount, return 0 if impossible

Constraints:
1 <= coins.length <= 100
1 <= coins[i] <= 5000
0 <= amount <= 5000

Approach:
dp

Time: O(n * a) -> n is the num of coins and a is the given amount
Space: O(a)
'''


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0] * (amount + 1)
        ways[0] = 1 # one way to make 0; use no coins

        for coin in coins: # counting combinations
            for currentAmount in range(coin, amount + 1):
                # every way to make current amount - coin, plus one of this coin
                ways[currentAmount] += ways[currentAmount - coin]

        return ways[amount] 