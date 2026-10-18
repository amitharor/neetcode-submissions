'''
input: array (str)
output: evaluated expression

constraints:
1 <= tokens.length <= 10000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-200, 200].

approach:
init stack

iterate through array
if the curr el is a num; add it to stack
if the curr el is an operator:
    pop the last two el from stack (1st pop is num2; 2nd pop is num1)
    eval the to nums with operand and add to stack

return stack (evaluated result)

time: O(n)
space: O(n)
'''


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if stack and token in '+-/*':
                num2, num1 = stack.pop(), stack.pop()

                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '/':
                    stack.append(int(num1 / num2))
                else:
                    stack.append(num1 * num2)
            else:
                stack.append(int(token))
        return stack[0]