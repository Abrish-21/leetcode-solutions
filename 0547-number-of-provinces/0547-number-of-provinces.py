class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph  = defaultdict(list)
        for i in range(len(isConnected)):
            curr_level = []
            for j in range(len(isConnected[0])):
                if isConnected[i][j] != 0 and i !=j  :
                    curr_level.append(j + 1)
            graph[i+ 1] = curr_level
        print(graph)
        visited = set()
        comp = 0
        def dfs(node, visited):
            nonlocal comp
            if not node: return comp
            visited.add(node)
            if graph[node]:
                for nei in graph[node]:
                    if nei not in visited:
                        dfs(nei, visited)
        for node in graph.keys():
            if node not in visited:
                dfs(node,visited)
                comp += 1
        return comp

                
            

        