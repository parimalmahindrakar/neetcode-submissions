class Solution:
    def myPow(self, x: float, n: int) -> float:
        num = 1
        if n > 0:
            for _ in range(n):
                num *= x
        else:
            for _ in range(abs(n)):
                num = num / x

        return num