class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)
        def dfs(i, color):
            colors[i] = color
            for nei in graph[i]:
                if colors[nei] == 0:
                    if not dfs(nei, -color):
                        return False
                elif colors[nei] == colors[i]:
                    return False
                
            return True

        for i in range(len(graph)):
            if colors[i] ==0:
                if not dfs(i, 1):
                    return False
        return True
          
                
            
     
        