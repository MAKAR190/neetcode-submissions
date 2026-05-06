class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []

        for string in strs:
            ans.append(f"{len(string)}#" + string)
        
        return "".join(ans)

    #5#Hello5#World
    def decode(self, s: str) -> List[str]:
        ans = []
        left = right = 0

        while right < len(s):
            curr = []

            while s[right] != "#":
                right += 1

            curr_len = int(s[left:right])
            right += 1
            left = right

            for i in range(right, right + curr_len):
                curr.append(s[i])
                right += 1
                left += 1

            ans.append("".join(curr))
        
        return ans
                