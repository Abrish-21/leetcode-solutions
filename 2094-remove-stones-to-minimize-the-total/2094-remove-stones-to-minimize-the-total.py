class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total_sum  = sum(piles)
        new_piles = [-i for i in piles]
        heapify(new_piles)
        while k:
            max_num = heappop(new_piles)
            heappush(new_piles,-(ceil(abs(max_num / 2))))
            total_sum -=   abs(max_num)// 2
            k -= 1
        return total_sum
       
        
        
        
            

        