'''
Input(s): two words (string), list of words (string)
Output: return min num of words within the transformation seq needed to obtain end word, otherwise return 0

Constraints:
1 <= beginWord.length <= 10
1 <= wordList.length <= 100


Approach:
bfs

Time: O(m^2 * n) -> where n is the num of words and m is the len of the word
Space: O(m^2 * n)
'''

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList) # O(1) -> check if word is real
        if endWord not in wordSet:
            return 0    # target cannot be reached


        queue = deque([(beginWord, 1)]) # (current word, words in the chain so far)
        visited = {beginWord} # never revisit a word


        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length # bfs -> first arrival is the shortest


            #build all words that are one letter different
            for i in range(len(word)):
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = word[:i] + letter + word[i + 1:] # keep everything except for position 'i'

                    if nextWord in wordSet and nextWord not in visited:
                        visited.add(nextWord) # mark it now so it's queued once
                        queue.append((nextWord, length + 1))


        return 0