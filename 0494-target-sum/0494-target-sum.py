class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        def dp(i,running_sum):
            if (i, running_sum) in memo:
                return memo[(i, running_sum)]

            if i == len(nums) and target == running_sum:
                return 1
            if i >= len(nums):
                return 0

            positive = dp(i+1, nums[i]+ running_sum)
            
            negative = dp(i+1, running_sum - nums[i])
            memo[(i,running_sum)] = positive + negative
            return memo[(i,running_sum)]
        return dp(0,0)

        
