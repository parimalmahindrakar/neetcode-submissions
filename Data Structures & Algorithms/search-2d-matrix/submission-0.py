class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0,  m * n - 1
        
        while left <= right:
            middle = (left + right) // 2

            row = middle // n
            col = middle % n

            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                left = middle + 1
            else:
                right = middle - 1

        return False 
