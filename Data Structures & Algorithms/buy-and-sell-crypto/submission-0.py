class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        profit = 0
        
        for price in prices:
            if price - buy > profit:
                sell = price
                profit = sell - buy
            if price < buy:
                buy = price
        return profit