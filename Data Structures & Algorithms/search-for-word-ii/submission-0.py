'''
Input(s): 2d grid (str), words(str)
Output: list of all words present in grid

Constraints:
1 <= board.length, board[i].length <= 12
board[i] consists only of lowercase English letter.
1 <= words.length <= 30,000
1 <= words[i].length <= 10
words[i] consists only of lowercase English letters.
All strings within words are distinct.

Approach:
trie - backtracking

Time: O(m * n * 4 * 3^(t-1) + s) -> m is the num of rows, n is num of cols, t is the max len of word in arr words and s is the sum of the len of all words
Space: O(s)
'''

class TrieNode:
    def __init__(self):
            self.children = {}
            self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        ROWS, COLS = len(board), len(board[0])
        found = []

        def dfs(row, col, node):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return

            letter = board[row][col]
            if letter not in node.children:
                return
            node = node.children[letter]

            if node.word:
                found.append(node.word)
                node.word = None

            board[row][col] = '#'
            dfs(row + 1, col, node)
            dfs(row - 1, col, node)
            dfs(row, col + 1, node)
            dfs(row, col - 1, node)
            board[row][col] = letter

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root)

        return found