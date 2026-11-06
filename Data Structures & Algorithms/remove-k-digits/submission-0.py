'''
input: decimal string - non negative int, k (int)
output: remove k digits without changing the order of remaining digits -> output should be smallest possible resulting int as a string (string); else return 0 if all other digits are zero or no other digits remain


constraints:
1 <= k <= num.length <= 100000
num contains only decimal digits.
num has no leading zeros unless it is exactly "0".


approach:
monotonic stack - greedy


time: O()
space: O()


'''


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        if k:
            del stack[-k:]

        return ''.join(stack).lstrip('0') or '0'



