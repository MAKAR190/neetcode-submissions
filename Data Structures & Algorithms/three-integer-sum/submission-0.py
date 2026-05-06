class Solution:
    # [-4, -1, -1, 0, 1, 2]
    # [[-4, ]]
    # threesome = 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []

        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                threesome = nums[i] + nums[left] + nums[right]

                if threesome == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                else:    
                    if threesome > 0:
                        right -= 1

                    if threesome < 0:
                        left += 1

        return ans