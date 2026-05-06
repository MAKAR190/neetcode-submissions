class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        n = len(nums)

        for i in range(n):
            num = nums[i]
            complement = target - num

            if num in complements:
                return [complements.get(num), i]
            
            complements[complement] = i