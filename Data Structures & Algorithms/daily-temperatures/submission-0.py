'''
input: array (int)
output: array (int) where every element is num of days after the ith day before warmer temp appears

constraints:
1 <= temperatures.length <= 100,000.
1 <= temperatures[i] <= 100

approach:
init var for results (set to 0 * len of input array)
init var for stack

iterate through array
repeatedly while our stack isn't empty and the last el in stack is smaller than curr el
	pop last element off stack
	update result at the last stack's element to current val's index minus stack's last element
append index of current element onto stack

return results

time: O(n)
space: O(n)
'''

class Solution:
    def dailyTemperatures(self, temperatures):
        results = [0] * len(temperatures)
        stack = []

        for today, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                cold_day = stack.pop()
                results[cold_day] = today - cold_day
            stack.append(today)
        return results
