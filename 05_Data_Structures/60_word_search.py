# -------------------------------------------------
# File Name: 60_word_search.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Word Search (LeetCode 79). Find word in 2D grid using backtracking.
# -------------------------------------------------

def exist(board: list[list[str]], word: str) -> bool:
    """Return True if word exists in board."""
    if not board or not board[0] or not word:
        return False

    rows, cols = len(board), len(board[0])

    def backtrack(r: int, c: int, idx: int) -> bool:
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False

        original = board[r][c]
        board[r][c] = "#"

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if backtrack(r + dr, c + dc, idx + 1):
                board[r][c] = original
                return True

        board[r][c] = original
        return False

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False


if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    print("Word 'ABCCED':", exist([row[:] for row in board], "ABCCED"))  # True
    print("Word 'SEE':", exist([row[:] for row in board], "SEE"))  # True
    print("Word 'ABCB':", exist([row[:] for row in board], "ABCB"))  # False
