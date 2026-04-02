class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = 0
        b, s = 0, 1

        while s < len(prices):
            if prices[b] >= prices[s]:
                b = s
                s = b+1
            else: 
                profit = prices[s] - prices[b]
                print(profit)
                highest_profit = max(profit, highest_profit)
                s+=1
        return highest_profit