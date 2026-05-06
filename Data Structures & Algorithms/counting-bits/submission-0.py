class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n + 1):
            bits = 0
            while i:
                bits += i & 1
                i >>= 1

            ans.append(bits)

        return ans