class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0), (-1,0), (0,1),(0,-1)]
        ans  = max_area = 0
        # no = 0

        def dfs(row, col):
            no = 0
            if row >= rows or row < 0 or col >= cols or col < 0 or grid[row][col] == 0:
                return 0
            size =  1
            grid[row][col] = 0
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                size += dfs(new_row, new_col)
            return size
    
               
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i,j))
        return max_area
  
        
        