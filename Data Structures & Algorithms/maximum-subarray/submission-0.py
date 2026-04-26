class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        overall_max = nums[0]

        for num in nums[1:]:
            current_max = max(num, current_max + num)
            overall_max = max(current_max, overall_max)
        
        return overall_max
        