class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = left = 0
        n = len(heights)
        right = n - 1

        while left < right:
            h_l, h_r = heights[left], heights[right]
            curr_h = min(h_l, h_r)
            curr_w = right - left
            ans = max(ans, curr_h * curr_w)

            if h_l >= h_r:
                right -= 1
            else:
                left += 1
        
        return ans
