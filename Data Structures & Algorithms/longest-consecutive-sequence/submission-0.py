class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0

        for num in nums:
            if num - 1 not in nums:
                curr = num
                curr_len = 1

                while curr + 1 in nums:
                    curr_len += 1
                    curr += 1

                ans = max(ans, curr_len)
        
        return ans

            