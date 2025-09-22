class Solution:
    def fib(self, n: int) -> int:
        return round(((1 + math.sqrt(5)) ** n - (1 - math.sqrt(5))**n ) / (math.sqrt(5) * (2 ** n)))
        