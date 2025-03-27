class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        window_sum = 0
        start = 0
        for i in range(len(nums)):
            window_sum += nums[i]
            # when the the criteria is met
            if window_sum >= target:
                while window_sum >= target:
                    window_sum -= nums[start]
                    start += 1
                min_length = min(min_length, i- start + 2)

            
            
        return min_length  if sum(nums) >= target else 0

