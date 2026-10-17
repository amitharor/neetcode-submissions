'''
Input(s): str
Output: bool; true iff every bracket closes in the correct order

Constraints:
1 <= s.length <= 1000

Approach:
init var to store stack
init var for hash map of all brackets open/close

iterate through string
if stack is empty or the last item in string is the the matched bracket to the current bracket;
return False
if stack is not empty and last items matches the matched bracket to current bracket:
pop off the last bracket from stack
otherwise append the current bracket to stack

return true is stack is empty, otherwise False

Time: O(n)
Space: O(n)
'''


class Solution:
	def isValid(self, s):
		stack = []
		unmatched_brackets = {
"}" : "{",
"]" : "[",
")" : "("
}

		for bracket in s:
			if bracket in unmatched_brackets:
				if not stack or stack[-1] != unmatched_brackets[bracket]:
					return False
				stack.pop()
			else:
				stack.append(bracket)
		return not stack
