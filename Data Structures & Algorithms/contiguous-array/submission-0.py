class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = {0: -1}
        balance = best = 0

        for i, x in enumerate(nums):
            balance += 1 if x else -1

            if balance in first:
                best = max(best, i - first[balance])
            else:
                first[balance] = i
        
        return best