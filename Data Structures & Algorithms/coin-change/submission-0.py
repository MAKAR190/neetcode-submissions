class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(remaining):
            if remaining < 0:
                return float("inf")
            if remaining == 0:
                return 0 
            if remaining in memo:
                return memo[remaining]

            min_coins = float("inf")
            for coin in coins:
                min_coins = min(min_coins, 1 + dp(remaining - coin))

            memo[remaining] = min_coins            
            return memo[remaining]

        memo = {}
        ans = dp(amount)
        return ans if ans != float("inf") else -1