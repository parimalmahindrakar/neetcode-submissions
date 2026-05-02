class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x * x, n // 2)   # square base, halve exponent
            return x * res if n % 2 else res  # multiply extra x if odd

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res  # handle negative exponent