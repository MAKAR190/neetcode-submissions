from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        n = len(board)

        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue

                if board[i][j] in rows[i]:
                    return False
                
                if board[i][j] in cols[j]:
                    return False

                curr_square = (i // 3, j // 3)

                if board[i][j] in squares[curr_square]:
                    return False
                
                rows[i].append(board[i][j])
                cols[j].append(board[i][j])
                squares[curr_square].append(board[i][j])
        
        return True
        