class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
    
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == m-1 and j == n-1:
                return 1
            if not (0 <=i < m and 0<= j <n):
                return 0
            down = dp(i+1, j)
            right  = dp(i,j+1)
            memo[(i,j)] = right + down
            return memo[(i,j)]
        return dp(0,0)

        
       