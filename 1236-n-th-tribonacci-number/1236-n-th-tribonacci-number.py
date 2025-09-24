class Solution:
    def tribonacci(self, n: int) -> int:
        memo = defaultdict(int)
        def trifib(n):
            if n  == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if n not in memo:
                memo[n] = trifib(n-3) + trifib(n-2) + trifib(n-1)
            return memo[n]
        return trifib(n)
        