class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i, signal):
            if (i, signal) in memo:
                return memo[(i, signal)]
            
            if i >= len(prices):
                return 0
            if signal == 1:
                include = prices[i] + dp(i+2, -1 * signal) 
            else:
                include = -prices[i] + dp(i+1, -1 *signal)
            exclude = dp(i+1, signal)
            memo[(i, signal)] =  max(include, exclude)
            return memo[(i, signal)]
        return dp(0, -1)
        