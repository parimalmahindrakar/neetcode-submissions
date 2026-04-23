class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for index, i in enumerate(nums):
            if (target - i) in index_map:
                return [index_map[target - i], index]
            index_map[i] = index
        