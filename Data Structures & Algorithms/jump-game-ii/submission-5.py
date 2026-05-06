# input:
# [2,4,1,1,1,1]
#            #   
# minimum number of jumps from nums[0] to nums[-1]
# nums[i] - the maximum number of jumps can be taken from ith position
# ans: 2 nums[0] -> nums[1] -> nums[-1]
# output: the minimum number of jumps 

# what if we choose the maximum number to jump which is in ith position range?
# it should minimize the taken number of jumps
# or if the nums[-1] already in range, return the ans + 1
# the question is, will it work on all test cases, or I am being delusional here...
# let's try

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if nums[0] == 0 or n == 1:
            return 0

        ans = i = 0
        
        while i < n - 1:
            furthest = i
            max_idx = i

            for j in range(1, nums[i] + 1):
                if i + j == n - 1:
                    return ans + 1
                
                if furthest <= i + j + nums[j]:
                    furthest = i + j + nums[j]
                    max_idx = i + j

            i = max_idx
            ans += 1

        return ans