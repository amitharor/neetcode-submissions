'''
input: string
output: bool; true is palindome; otherwise false

constraints:
1 <= s.length <= 1000
s is made up of only printable ASCII characters.


time: O(n)
space: O(1)

approach:
init var to store left/right pointers (starting at each end of string)
as long as the current element at left/right pointers is a non-alpha num char, move inwards
compare element at left/right index; if different; return false

return True
'''



class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].casefold() != s[right].casefold():
                return False

            left += 1
            right -= 1
        
        return True