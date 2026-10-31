'''
Input(s): two strings
Output: return product of num1 and num2 as a string

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.

Approach:
long multiplication


Time: O(m * n)
Space: O(m + n)
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        len1 = len(num1)
        len2 = len(num2)
        productOfDigits = [0] * (len1 + len2)

        for i in range(len1 - 1, -1, -1):
            digit1 = ord(num1[i]) - ord('0')
            for j in range(len2 -1, -1, -1):
                digit2 = ord(num2[j]) - ord('0')

                onesPosition = i + j + 1
                carryPosition = i + j
                total = digit1 * digit2 + productOfDigits[onesPosition]
                productOfDigits[onesPosition] = total % 10
                productOfDigits[carryPosition] += total // 10

        start = 0
        while start < len(productOfDigits) - 1 and productOfDigits[start] == 0:
            start += 1

        result = ''
        for digit in productOfDigits[start:]:
            result += chr(digit + ord('0'))
        
        return result