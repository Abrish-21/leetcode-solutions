class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # first we store the rotten ones and coun the fresh ones
        row = len(grid)
        col = len(grid[0])
        max_minute = 0

        fresh_count  = 0 #counts the fresh oranges
        queue = deque() #stores the rotten oranges
        for i in range(row):
            for  j in range(col):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i,j,0))
        if fresh_count ==0:
            return max_minute
        while queue:
            r, c, minute = queue.popleft()
            max_minute  = max(max_minute, minute)
            directions = [(1,0), (0,1), (-1,0),(0,-1)]
            for dr, dc in directions:
                new_row = dr + r 
                new_col  = dc + c
                if 0 <= new_row < row and 0 <= new_col < col and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    fresh_count -= 1
                    queue.append((new_row, new_col, minute + 1))
        if fresh_count == 0:
            return max_minute
        else:
            return -1


        