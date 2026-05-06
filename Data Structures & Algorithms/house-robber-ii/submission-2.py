class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]

        dp_first = [0] * (n + 1)
        dp_second = [0] * (n + 2)

        for i in range(n - 2, -1, -1):
            dp_first[i] = max(nums[i] + dp_first[i + 2], dp_first[i + 1])

        for i in range(n - 1, 0, -1):
            dp_second[i] = max(nums[i] + dp_second[i + 2], dp_second[i + 1])


        return max(dp_first[0], dp_second[1])