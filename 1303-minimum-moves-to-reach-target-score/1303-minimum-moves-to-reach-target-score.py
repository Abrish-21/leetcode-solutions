class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        curr = target
        while maxDoubles > 0 and curr > 1: 
            if curr%2 !=0:
                curr -= 1
                moves += 1
            else:
                curr = curr // 2
                moves += 1
                maxDoubles -= 1
        return moves + curr - 1
        

        