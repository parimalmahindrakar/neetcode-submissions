class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for i in nums:
            count_dict[i] = count_dict.get(i, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count_dict.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res
