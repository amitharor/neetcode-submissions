'''
Input(s): arr (int), groupSize (int)
Output: bool; return Trus if possible to rearrange cards in increasing order by 1; else False

Constraints:
1 <= hand.length <= 10000
0 <= hand[i] <= 1000
1 <= groupSize <= hand.length

Approach:
hash map

Time: O(n)
Space: O(n)
'''


from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        for num in hand:
            start = num

            while count[start - 1]:
                start -= 1
            
            while start <= num:
                while count[start]:
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False
                        count[i] -= 1

                start += 1

        return True