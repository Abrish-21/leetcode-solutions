class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact_recursion(n):
            if n == 0:
                return 0
            return n // 5 + fact_recursion(n // 5)
        
        return fact_recursion(n) 
