class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(len(prices)):
            p=max(prices[i::])-prices[i]
            profit=p if p>profit else profit
        return profit