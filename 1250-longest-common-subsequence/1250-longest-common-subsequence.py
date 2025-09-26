class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        longest = 0
        M = len(text1)
        N = len(text2)
        memo = defaultdict(int)
        def dp(i,j):
            nonlocal longest
            if (i, j) in memo:
                return memo[(i,j)]
            
            if i == M  or j == N :
                return 0
            include = 0
            exclude = 0

            if text1[i] == text2[j]:
                include = 1 + dp(i+1,j+1)
            else:
                skip_1 = dp(i+1, j)
                skip_2  = dp(i, j+1)
                exclude = max(skip_1, skip_2)
            memo[(i,j)] = max(include, exclude)
            return memo[(i,j)]
        return dp(0,0)
            
            
        