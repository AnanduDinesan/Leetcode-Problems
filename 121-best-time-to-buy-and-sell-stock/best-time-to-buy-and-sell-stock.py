class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        buy=prices[0]
        for i in range(1,n):
            if prices[i] > buy:
                profit=max(prices[i]-buy,profit)
            else:
                buy=prices[i]
        return profit
        