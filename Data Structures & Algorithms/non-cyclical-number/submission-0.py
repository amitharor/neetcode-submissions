'''
Input(s): int
Output: bool: True is it is non-cylical number; else False

Constraints:
1 <= n <= 1000

Approach:
fast and slow

Time: O(log n)
Space: O(1)
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquares(n)

        while fast != 1 and slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))

        return fast == 1

    
    def sumOfSquares(self, number):
        total = 0
        while number > 0:
            lastDigit = number % 10
            total += lastDigit * lastDigit
            number //= 10
        return total