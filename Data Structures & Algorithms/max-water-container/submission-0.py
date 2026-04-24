class Solution:
    def maxArea(self, heights: List[int]) -> int:
        heights_size = len(heights)
        left = 0
        right = heights_size - 1
        max_contained_water = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            max_contained_water = max(max_contained_water, area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_contained_water

        