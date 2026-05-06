

# dp(i, j):
#
#  if text1[i] == text2[j]:
#     return 1 + dp(s1[1])
#  
#  memo[(s1, s2)] = 
#  return memo[(s1, s2)]

from collections import defaultdict
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        def dp(i, j):
            if i == m or j == n:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1)

            memo[(i, j)] = max(dp(i + 1, j), dp(i, j + 1))
            return memo[(i, j)]    

        memo = defaultdict(int)
        return dp(0, 0)