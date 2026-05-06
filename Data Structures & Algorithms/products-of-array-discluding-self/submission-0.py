class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        def multiply(l, r):
            ans = 1
            for i in range(l, r):
                ans = ans * nums[i]
            return ans
        
        for i in range(n):
            ans.append(multiply(0, i) * multiply(i + 1, n))
        
        return ans