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
