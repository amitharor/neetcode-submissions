'''
Input(s): arr (int), target (int)
Output: return num of different ways that we can build the expression such that total sum == target

Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
-1000 <= target <= 1000

Approach:


Time: O(n * m) -> n is len of array and m is the sum of all elements in arr
Space: O(m)
'''

from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counts = defaultdict(int) # running sum -> num of ways to reach it
        counts[0] = 1

        for num in nums:
            newCounts = defaultdict(int) # sum after choosing a sign for num
            for runningSum, ways in counts.items():
                plusSum = runningSum + num
                minusSum = runningSum - num
                
                #  add this path's ways to whatever already reached that sum
                newCounts[plusSum] += ways
                newCounts[minusSum] += ways
            
            counts = newCounts

        return counts[target]