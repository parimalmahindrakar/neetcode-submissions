class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for right in range(1, len(prices)):
            if (prices[right] - min_price) > max_profit:
                max_profit = prices[right] - min_price
            if prices[right] < min_price:
                min_price = prices[right]
        
        return max_profit


        