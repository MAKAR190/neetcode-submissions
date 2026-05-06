from collections import defaultdict
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def valid(r, c):
            return 0 <= r < m and 0 <= c < n

        def dp(r, c):
            if r == 0 and c == 0:
                return 1
            
            if not valid(r, c):
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            memo[(r, c)] += dp(r, c - 1) + dp(r - 1, c)
            return memo[(r, c)]
        
        memo = defaultdict(int)
        return dp(m - 1, n - 1)