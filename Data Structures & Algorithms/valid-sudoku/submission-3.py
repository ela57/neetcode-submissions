class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = 9, 9
        for r in range(rows):
            visited = set()
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in visited:
                    return False
                else:
                    visited.add(board[r][c])
        for c in range(cols):
            visited = set()
            for r in range(rows):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in visited:
                    return False
                else:
                    visited.add(board[r][c])

        for i in range(9):
            visited = set()
            for r in range(3):
                for c in range(3):
                    b = board[(i//3)*3 + r][(i%3)*3 + c]
                    if b == ".":
                        continue
                    elif b in visited:
                        return False
                    visited.add(b)
        return True