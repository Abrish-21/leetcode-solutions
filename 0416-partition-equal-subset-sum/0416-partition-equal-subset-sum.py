class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0:
            return False
        memo = defaultdict(int)
        def partition(index, valid_sum):
            if valid_sum > total // 2:
                return False
            if index  == len(nums) - 1:
                return valid_sum == total // 2
            if (index, valid_sum) not in memo:
                memo[(index, valid_sum)] = (partition(index + 1,valid_sum + nums[index + 1])) or (partition(index + 1, valid_sum))
            return memo[(index, valid_sum)]    
        return partition(0,0)
            


            
            
            
            