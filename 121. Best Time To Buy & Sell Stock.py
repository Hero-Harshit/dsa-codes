class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):

            for j in range(i+1,len(prices)):

                if (prices[j] - prices[i]) > max_profit:
                    max_profit = prices[j] - prices[i]

        return max_profit            