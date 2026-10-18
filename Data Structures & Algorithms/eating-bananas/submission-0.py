'''
input: arr (int), target (int)
output: min num koko can eat per hour within target limit

constraints:
1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109


approach:
init min/max pointers (max will be largest pile)

search for smallest speed that finishes all piles within the target
init middle pointer between the min and max pointers
init var to keep track of total time
iterate through input arr
repetitively add time for each element + mid time - 1 // mid time as long as its less that target time



update time to 

time: O(n log m)
space: O(1)
'''



class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        result = right

        while left <= right:
            mid = (left + right) // 2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / mid)

            if totalTime <= h:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1

        return result