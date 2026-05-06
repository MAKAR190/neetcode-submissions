class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        n = len(nums)

        maxEnding = nums[0]

        for i in range(1, n):
            maxEnding = max(nums[i], nums[i] + maxEnding)

            ans = max(ans, maxEnding)
        
        return ans