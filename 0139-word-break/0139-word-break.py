class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = defaultdict(bool)
        def dp(idx):
            if  idx in memo:
                return  memo[idx]
            if idx >= len(s):
                return True 
            temp = False
            
            for i in range(len(s)):
                if s[idx:i+1] in  wordDict:
                    
                    temp  = temp or dp(i + 1)
            memo[idx] = temp
            return memo[idx]
        return dp(0)


        