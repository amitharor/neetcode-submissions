from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        start = 0
        maxLen = 0
        fruitCount = defaultdict(int)

        for end in range(len(fruits)):
            fruitCount[fruits[end]] += 1

            while len(fruitCount) > 2:
                fruitCount[fruits[start]] -= 1

                if fruitCount[fruits[start]] == 0:
                    del fruitCount[fruits[start]]
                
                start+= 1

            maxLen = max(maxLen, end - start + 1)

        return maxLen