'''
input: str
output: bool; true if we are able to close all parenthesis in order; else False

constraints:
1 <= s.length <= 1000


time: O()
space: O()

approach:
init var to store hash map of open/closing brackets
if len of str is odd; return False
init var to store open brackets; list

iterate through string:



'''



class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        match_bracket = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        open_bracket = []


        for bracket in s:
            if bracket not in match_bracket:
                open_bracket.append(bracket)
            elif not open_bracket or open_bracket.pop() != match_bracket[bracket]:
                return False

        return not open_bracket
        