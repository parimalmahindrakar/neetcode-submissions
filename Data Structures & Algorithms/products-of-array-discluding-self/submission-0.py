class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_size = len(nums)
        prefix_list = [1] * nums_size
        suffix_list = [1] * nums_size

        res = []

        for i in range(1, len(nums)):
            prefix_list[i] = prefix_list[i - 1] * nums[i - 1]

        for i in range(nums_size - 2, -1, -1):
            suffix_list[i] = suffix_list[i + 1] * nums[i + 1]

        res = [prefix_list[i] * suffix_list[i] for i in range(nums_size)]
        return res


        