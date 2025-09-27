import sys
from typing import List

sys.setrecursionlimit(3000)
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo = defaultdict(int)
        stone_map = {stone:i for i,stone in enumerate(stones)}
        for i in range(len(stones)):
            if stones[i] - stones[i-1] > i:
                return False
        def dp(i,k):
            if (i,k) in memo:
                return memo[(i,k)]
            if i  == len(stones)-1:
                return True
            for j in [k-1, k, k+1]:
                if j <= 0:
                    continue
                possible_p = stones[i] + j
                if possible_p in stone_map:
                    new_i = stone_map[possible_p]
                    if dp(new_i, j):
                        memo[(i,k)] = True
                        return True
            memo[(i,k)] = False
            return False
        return dp(0,0)
                