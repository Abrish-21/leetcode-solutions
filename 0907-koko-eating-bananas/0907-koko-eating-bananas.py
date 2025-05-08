class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def validate(capacity):

            curr_wei = 0
            for wei in piles:
                curr_wei += ceil(wei / capacity)
                if curr_wei > h:
                    return False
            return True
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high) // 2
            if validate(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low

        