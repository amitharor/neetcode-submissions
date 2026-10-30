'''
Input(s): string -> '(', ')' or '*'
Output: bool; return True if s is valid; else False

Constraints:
1 <= s.length <= 100

Approach:
greedy

Time: O(n)
Space: O(1)
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen = 0 # fewest '(' that could be open -> treat '*' as ')'
        maxOpen = 0 # most '(' that could be open -> treat '*' as '('

        for char in s:
            if char == '(':
                minOpen += 1
                maxOpen += 1
            elif char == ')':
                minOpen -= 1
                maxOpen -= 1
            else: # '*' -> open, close, or empty
                minOpen -= 1
                maxOpen += 1

            if maxOpen < 0:
                return False 
            if minOpen < 0:
                minOpen = 0 # cannot have negative open
            
        return minOpen == 0