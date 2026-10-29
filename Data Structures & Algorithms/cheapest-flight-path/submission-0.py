'''
Input(s): n (int), flights - list (int), src (int), dst (int), k(int)
Output: 

Constraints:
1 <= n <= 100
fromi != toi
1 <= pricei <= 1000
0 <= src, dst, k < n

Approach:
bellman-ford

Time: O(K * E) -> k+ 1 rounds and each round checkes every one of the E flights once
Space: O(n)
'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        prices = [INF] * n # cheapest known cost to reach each city
        prices[src] = 0 # no cost from starting city

        for _ in range(k + 1):
            newPrices = prices.copy()

            for source, destination, price, in flights:
                if prices[source] == INF:
                    continue # can't reach the flights start yet

                cost = prices[source] + price # reach source and then take this flight
                if cost < newPrices[destination]:
                    newPrices[destination] = cost # found cheaper way

            prices = newPrices

        return -1 if prices[dst] == INF else prices[dst]