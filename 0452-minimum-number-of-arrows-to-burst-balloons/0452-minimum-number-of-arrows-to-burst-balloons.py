class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrow = 1
        points.sort(key = lambda x: x[1])
        min_val = points[0][0]
        max_val = points[0][1]
        for l,r in points:
            if l > max_val:
                arrow += 1
                max_val = r
        return arrow
                 

        