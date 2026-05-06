from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = Counter(t)
        window = {}

        have, need = 0, len(required)
        res = [-1, -1]
        resLen = float("inf")

        n = len(s)
        left = 0

        for right in range(n):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in required and window[c] == required[c]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                window[s[left]] -= 1
                if s[left] in required and window[s[left]] < required[s[left]]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""