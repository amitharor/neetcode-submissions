'''
Input(s): array (str)
Output: evaluated num

Constraints:
1 <= tokens.length <= 10000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-200, 200].

Approach:
init var for stack

iterate through array
if current el is a num then push onto stack
if current el is an operator, pop the last two from stack (first pop is num2, second pop is num1)
eval expression and push the evaluated num back onto stack

return the evaluated num from stack

Time: O(n)
Space: O(n)
'''


class Solution:
    def evalRPN(self, tokens):
        stack = []
        ops = "+-/*"

        for token in tokens:
            if token in ops:
                num2, num1 = stack.pop(), stack.pop()
        
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
                    
            else:
                stack.append(int(token))
            
        return stack[0]
