# "neetcode", wordDict = ["neet","code"]

# Iterate while a word beginning from the current search index exists and while we can find a full word which applies; or when the current matched string equals to the original one, return True
# Otherwise break a loop and return False - done

# In the loop look for a first word which begins on the letter of current search index - done
# If the full word matches with an original string update the search index - 
# If after the whole iteration the search index wasn't updated return False

# TC(n * m) where n is the length of an original string and m is the average length of a string in a wordDict
# SC(1) 


# GREEDY APPROACH FAILED

# DP is needed as we need to explore all possible situations, in the previous approach our search index couldn't be rewinded 


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict) # for fast lookups
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]
