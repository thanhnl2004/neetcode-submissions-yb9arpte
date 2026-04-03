class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low, sell high    
        # L = Buy, R = Sell    
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                cur_profit = prices[r] - prices[l]
                max_profit = max(max_profit, cur_profit)
            else:
                l = r
            r += 1 # regardless of condition
                

        return max_profit
            
         