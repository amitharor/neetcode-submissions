'''
Input(s): x (float), n (int)
Output: implement func that calc x raised to the power of n

Constraints:
-100.0 < x < 100.0
-2^31 <= n <= 2^31 - 1
n is an integer.
Either x is not zero or n > 0.
-10^4 <= x^n <= 10^4

Approach:
fast exponentation (repeated squaring)

Time: O(log n)
Space: O(1)
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 /x
            n = -n

        result = 1
        currentPower = x

        while n > 0:
            if n % 2 == 1:
                result *= currentPower
            currentPower *= currentPower
            n //= 2

        return result