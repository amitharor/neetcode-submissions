'''
Input(s): 2 x arr (int)
Output: return starting gas station's index such that we can travel around the circuit once clockwise, else return -1

Constraints:
1 <= gas.length == cost.length <= 100000
0 <= gas[i], cost[i] <= 1000

Approach:
dp - greedy

Time: O(n)
Space: O(1)
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1


        tank = 0 # gas left since the current start
        start = 0 # current candidates start station

        for i in range(len(gas)):
            tank += gas[i] - cost[i] 
            if tank < 0:
                start = i + 1
                tank = 0
        return start