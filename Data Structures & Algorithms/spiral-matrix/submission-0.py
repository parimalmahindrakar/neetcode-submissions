class Solution:
    def spiralOrder(self, arr):
        res = []

        top, bottom = 0, len(arr) - 1
        left, right = 0, len(arr[0]) - 1

        while top <= bottom and left <= right:

            for j in range(left, right+1):
                res.append(arr[top][j])
            top += 1

            for i in range(top, bottom + 1):
                res.append(arr[i][right])
            right -= 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(arr[bottom][j])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(arr[i][left])
                left += 1

        
        return res

            