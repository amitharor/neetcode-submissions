'''
Input(s): arr (int)
Output: return max profit you can achieve

Constraints:
1 <= prices.length <= 5000
0 <= prices[i] <= 1000

Approach:
dp

Time: O(n)
Space: O(1)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holding = float('-inf') # best profit while owning a share
        sold = 0 # best profit if sold today
        resting = 0 # best profit with no share and free to buy

        for price in prices:
            newHolding = max(holding, resting - price) # keep holding or buy new
            newSold = holding + price # sell the share we held
            newResting = max(resting, sold) # keep resting, or finish the cooldown

            holding = newHolding
            sold = newSold
            resting = newResting

        return max(sold, resting) # end without a share