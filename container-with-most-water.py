class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        l, r = 0, len(height)-1
        while l < r:
            result = max(result,(r-l) * min(height[r],height[l]))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return result