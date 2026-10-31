'''
Input(s): arr (int)
Output: return list of digits og the given int after incrementing by 1

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9

Approach:
add from the right and carry

Time: O(n)
Space: O(1)
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, - 1, - 1):
            if digits[i] < 9: 
                digits[i] += 1 # no carry needed 
                return digits
            digits[i] = 0 # digit is 9 -> write 0 -> carry 1 to the left

        return [1] + digits # takes into account that every digit is 9 so result is 1 followed by all zeros