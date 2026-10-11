'''
Input(s): 9 x 9 sudoku board
Output: each row needs 1 through 9; each col needs 1 through 9, each 3 x 3 needs 1 through 9 (no duplicates)

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

Time: O(n^2)
Space: O(1)

Approach:

init vars for rows, cols, and 3x3 grid
iterate through rows
iterate through cols (nested within rows)

init vars to get the current num, row, col and sq

skip "."
check if num is in row, col, sq, if so; return False as it means the num has been seen
if not; add num to row, col, sq

return True
'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(length):
            for c in range(length):
                num = board[r][c]
                row = rows[r]
                col = cols[c]
                sq = square[( r // 3, c // 3)]

                if num == '.':
                    continue
                
                if (num in row or
                    num in col or
                    num in sq
                ):
                    return False

                row.add(num)
                col.add(num)
                sq.add(num)

        return True

