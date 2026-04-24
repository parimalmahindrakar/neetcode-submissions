class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while (left <= right):
            if nums[left] <= nums[right]:
                return nums[left]

            middle = (left + right) // 2
            if nums[middle] < nums[middle - 1]:
                return nums[middle]
            else:
                if nums[left] > nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
