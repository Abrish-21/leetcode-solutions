class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        original_color = image[sr][sc]
        
        if original_color == color:
            return image
        
        ROWS, COLS = len(image), len(image[0])
        
        def dfs(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS):
                return
            
            if image[r][c] != original_color:
                return
            
            image[r][c] = color
            
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        dfs(sr, sc)
        
        return image