class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = []
        def dfs(room):
            if room not in visited:
                visited.append(room)
                if rooms[room]:
                    for key in rooms[room]:
                        dfs(key)
            return visited
        return len(dfs(0)) == len(rooms)
        