'''
input: array (int)
output: return max profit (only 1 buy and 1 sell)

constraints:
1 <= prices.length <= 100
0 <= prices[i] <= 100
cannot go back in time
cannot sell before buying stock

time: O(n)
space: O(1)

approach:
init right/left pointer starting at beginning
init var to store results

iterate through array
increment right pointer
if right pointer is smaller than left pointer, move left pointer to right pointer
otherwise; get the max profit (right element - left element)

return results
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0

        for right in range(len(prices)):
            buy = prices[left]
            sell = prices[right]

            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                left = right


        return profit