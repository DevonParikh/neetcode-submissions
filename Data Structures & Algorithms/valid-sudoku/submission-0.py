class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        arr = [[set() for _ in range(3)] for _ in range(3)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in arr[i//3][j//3] and board[i][j] not in rows[i] and board[i][j] not in cols[j]:
                        arr[i//3][j//3].add(board[i][j])
                        rows[i].add(board[i][j])
                        cols[j].add(board[i][j])
                    else:
                        return False
        return True