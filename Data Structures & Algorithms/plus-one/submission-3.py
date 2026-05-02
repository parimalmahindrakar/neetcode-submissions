class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        new_arr = []
        # for i in range(len(digits) - 1, -1, -1):

        for i in digits[::-1]:
            summation = i + carry
            reminder = summation % 10
            ques = summation // 10
            carry = ques
            new_arr.append(reminder)

        if carry:
            new_arr.append(carry)
        return new_arr[::-1]

            





        