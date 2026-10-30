'''
Input(s): 2d arr (int), target arr (int)
Output: bool; true if possible to ontain target as an element of triplets; else False

Constraints:
1 <= triplets.length <= 1000
1 <= ai, bi, ci, x, y, z <= 100

Approach:
dp - greedy

Time: O(n)
Space: O(1)
'''

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        matchedPositions = set() # which of positions 0, 1, 2, hit the target

        for triplet in triplets:
            #  any value lower than target cannot be lowered
            if (triplet[0] > target[0] or
                triplet[1] > target[1] or
                triplet[2] > target[2]):
                continue

            #  this triplet is safe to merge
            for position in range(3):
                if triplet[position] == target[position]:
                    matchedPositions.add(position)

        return len(matchedPositions) == 3
