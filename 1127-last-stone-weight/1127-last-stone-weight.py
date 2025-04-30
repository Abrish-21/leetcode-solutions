class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = [-i for i in stones]
        heapify(new_stones)
        while len(new_stones) >= 2:
            y = abs(heappop(new_stones))
            x = abs(heappop(new_stones))
            if x != y:
                heappush(new_stones, -(abs(y) - abs(x)))
        return -(new_stones[0]) if new_stones else 0
        