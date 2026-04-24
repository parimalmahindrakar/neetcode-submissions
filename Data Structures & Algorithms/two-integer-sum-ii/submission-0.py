class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_size = len(numbers)
        left = 0
        right = num_size - 1
        
        while left < right:
            summation = numbers[left] + numbers[right]
            if summation == target:
                return [left + 1, right + 1]
            elif target < summation:
                right -= 1
            else:
                left += 1
