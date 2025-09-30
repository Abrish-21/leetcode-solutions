class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
    
        for r in range(m):
            for c in range(n):
                if r == 0 and c ==0:
                    dp[0][0] = grid[0][0]
                elif r == 0:
                    dp[r][c] = grid[r][c] + dp[r][c-1]
                elif c ==0:
                    dp[r][c] = grid[r][c] + dp[r-1][c]
                else:
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]
        return  dp[-1][-1]


