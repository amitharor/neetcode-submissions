'''
Input(s): s(str)
Output: return all possible lists of palindomic substrings

Constraints:
1 <= s.length <= 20
s contains only lowercase English letters.


Approach:
backtracking

Time: O(n * 2^n)
Space: O(n^2)
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        
        def backtrack(start):
            if start == len(s):
                result.append(current.copy())
                return

            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    current.append(s[start:end + 1])
                    backtrack(end + 1)
                    current.pop()
            

        backtrack(0)
        return result