class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = curr = left = 0
        n = len(prices)

        for right in range(n):
            curr = prices[right] - prices[left]
            while curr < 0:
                left += 1
                curr = prices[right] - prices[left]
                
            ans = max(ans, curr)

        return ans