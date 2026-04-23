class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                
                box_index = (row // 3) * 3 + (col // 3)
                
                if val in rows[row]:
                    return False
                if val in cols[col]:
                    return False
                if val in boxes[box_index]:
                    return False

                rows[row].add(val)
                cols[col].add(val)
                boxes[box_index].add(val)

        return True
        