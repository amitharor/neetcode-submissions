'''
Input(s): string of digits from 2 through 9 inclusive
Output: return all possible letter combinations that digits could represent

Constraints:
0 <= digits.length <= 4
2 <= digits[i] <= 9

Approach:
backtracking

Time: O(n * 4^n)
Space: O(n)
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        result = []
        current = []

        def backtrack(index):
            if index == len(digits):
                result.append(''.join(current))
                return

            
            for letter in phone[digits[index]]:
                current.append(letter)
                backtrack(index + 1)
                current.pop()

        if digits:
            backtrack(0)
        return result