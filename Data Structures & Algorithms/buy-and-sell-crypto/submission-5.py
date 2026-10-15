'''
input: array (int)
output: return max profit (only 1 buy and 1 sell)

constraints:
1 <= prices.length <= 100
0 <= prices[i] <= 100
cannot go back in time
cannot sell before buying stock

time: O(n)
space: O(k)

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
        results = 0

        for right, num in enumerate(prices):
            buy = prices[left]
            sell = prices[right]

            while sell < buy:
                left += 1
                buy = prices[left]

            results = max(results, sell - buy)

        return results