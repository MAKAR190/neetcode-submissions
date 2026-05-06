class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            "[": "]",
            "(": ")",
            "{": "}"
        }

        for c in s:
            if stack and matches.get(stack[-1]) == c:
                stack.pop()
            else:
                stack.append(c)
            
      
        
        return len(stack) == 0