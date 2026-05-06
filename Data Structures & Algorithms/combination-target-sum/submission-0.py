from collections import Counter
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(curr, i):
            if sum(curr) == target:
                ans.append(curr[:])
                return
            
            if sum(curr) > target:
                return
            
            for i in range(i, n):
                curr.append(nums[i])
                backtrack(curr, i)
                curr.pop()

        backtrack([], 0)
        return ans