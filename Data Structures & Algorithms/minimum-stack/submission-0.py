'''
Input(s): Creating a stack class that has push, pop, top, and getMin
Output: top and getMin output the last on stack or min in stack

Constraints:
-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.
At most 3∗10^4 calls will be made to push, pop, top, and getMin.

Approach:
have two stacks. min stack will keep track of the min num at each level
push - add to stack and add lowest num to min stack
pop - remove last el from stack and min stack
top - return last el from stack
getMin - return last el from min stack

Time: O(1)
Space: O(n)
'''


class MinStack:
	
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
	        self.min_stack.append(val)
		
    def pop(self):
	    if self.stack:
		    self.stack.pop()
		    self.min_stack.pop()
		
    def top(self):
        return self.stack[-1]		

    def getMin(self):
	    return self.min_stack[-1]
