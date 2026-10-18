'''
Input(s): two arrays (int), target (int)
Output: num of different car fleets that arrive at destination

Constraints:
n == position.length == speed.length.
1 <= n <= 100,000
0 < target <= 1,000,000
1 <= speed[i] <= 1,000,000
0 <= position[i] < target
All the values of position are unique.

Approach:
zip the two arrays to group the speed and position. sort and reverse array to get descending ord
init var for stack

iterate through array
init var to calc time to reach target
check if current time is > the last time in the stack; if so, append to stack

return len of stack

Time: O(n log n)
Space: O(n)
'''

class Solution:
	def carFleet(self, target, position, speed):
		combined = sorted(zip(position, speed), reverse = True)
		stack = []

		for car_position, car_speed in combined:
			time = (target - car_position) / car_speed

			if not stack or time > stack[-1]:
				stack.append(time)
			
		return len(stack)
