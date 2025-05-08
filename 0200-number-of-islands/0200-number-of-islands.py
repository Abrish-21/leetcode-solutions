class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0), (-1,0), (0,1),(0,-1)]
        island = 0
        ans  = []
        # no = 0

        def dfs(row, col):
            no = 0
            if row >= rows or row < 0 or col >= cols or col < 0 or grid[row][col] == '0':
                return
            no += 1
            grid[row][col] = '0'
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                dfs(new_row, new_col)
    
               
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i,j)
                    island += 1
        print(ans)
        return island
        