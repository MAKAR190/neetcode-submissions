# [3,4,5,6,1,2]

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        pivot = 0

        def b_s(l, r):
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return mid

                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
                
            return -1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l
        l, r = 0, n - 1

        if nums[pivot] == target:
            return pivot
        
        elif target > nums[r]:
            return b_s(l, pivot - 1)
        else:
            return b_s(pivot, r)