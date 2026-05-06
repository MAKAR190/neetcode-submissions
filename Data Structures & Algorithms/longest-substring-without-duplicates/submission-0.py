from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = defaultdict(int)

        ans = left = 0
        n = len(s)

        for right in range(n):
            counts[s[right]] += 1

            while counts[s[right]] > 1:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1

            
            
            ans = max(ans, right - left + 1)
        
        return ans