class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i):
            if i in memo:
                return memo[i]

            if i >= len(cost):
                return 0
            memo[i] = min(dp(i+1), dp(i+2)) + cost[i]
            return memo[i]
        return min(dp(1), dp(0))
            

        