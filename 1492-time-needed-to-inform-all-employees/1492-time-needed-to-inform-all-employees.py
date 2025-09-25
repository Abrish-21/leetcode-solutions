class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i, m in enumerate(manager):
            if m!= -1:
                graph[m].append(i)
        def dfs(node):
            max_time  = 0
            if not graph[node]:
                return informTime[node]
            max_time = 0
            for sub in graph[node]:
                max_time  = max(max_time, dfs(sub))
            return informTime[node] + max_time
        return dfs(headID)



            