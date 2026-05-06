class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def valid(r, c):
            return 0 <= r < m and 0 <= c < n 

        def backtrack(r, c, i):
            if i >= len(word):
                return True
            
            if not valid(r, c) or word[i] != board[r][c] :
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            found = (
                backtrack(r + 1, c, i + 1) or
                backtrack(r - 1, c, i + 1) or
                backtrack(r, c + 1, i + 1) or
                backtrack(r, c - 1, i + 1)
            )
            board[r][c] = temp

            return found

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True
        
        return False