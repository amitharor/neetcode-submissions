'''
Input(s): list of tickets (next list of str)
Output: reconstruct itinerary in order and return it. if multiple valid paths, return lexical smallest one.

Constraints:
1 <= tickets.length <= 300
from_i != to_i

Approach:
dfs - euler path

Time: O(E log E) -> where E is the num of edges (tickets)
Space: O(E)
'''

from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        # sort in reverse so smallest dest is at the end of each list -> pop() will be O(1)
        for source, destination in sorted(tickets, reverse = True):
            graph[source].append(destination)

        route = []

        def visit(airport):
            # use up all tickets leaving this airport, smallest first
            while graph[airport]:
                nextAirport = graph[airport].pop()
                visit(nextAirport)

            route.append(airport)

        visit('JFK')
        return route[::-1] # reverse -> built from end to start