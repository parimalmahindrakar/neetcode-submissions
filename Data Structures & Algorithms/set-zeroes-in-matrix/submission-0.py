class Solution:
    def setZeroes(self, arr: List[List[int]]) -> None:
        # O(1)
        rows, cols = len(arr), len(arr[0])
        rowZeros = False

        # determine which rows/cols needs to be zero
        for r in range(rows):
            for c in range(cols):
                if arr[r][c] == 0:
                    arr[0][c] = 0
                    if r > 0:
                        arr[r][0] = 0
                    else:
                        rowZeros = True
                    
        for r in range(1, rows):
            for c in range(1, cols):
                if arr[0][c] == 0 or arr[r][0] == 0:
                    arr[r][c] = 0

        if arr[0][0] == 0:
            for r in range(rows):
                arr[r][0] = 0
        
        if rowZeros:
            for c in range(cols):
                arr[0][c] = 0

        