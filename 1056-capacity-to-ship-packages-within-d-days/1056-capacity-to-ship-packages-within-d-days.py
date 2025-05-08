class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validate(capacity):
            day =  1
            curr_wei = 0
            for wei in weights:
                curr_wei += wei
                if curr_wei > capacity:
                    curr_wei = wei
                    day += 1
                if day > days:
                    return False
            return True

        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            if validate(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
                    



        
            
            


                
            

                    



            
        