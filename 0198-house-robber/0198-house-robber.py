class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        # n = len(nums) - 1
        def robbing(n):
            if n < 0:
                return 0
            if n not in memo:
                memo[n] = max( nums[n] + robbing(n-2) , robbing(n-1))
            return memo[n]
        return robbing(len(nums)-1)
        print(nums)

        
            

        

             
        