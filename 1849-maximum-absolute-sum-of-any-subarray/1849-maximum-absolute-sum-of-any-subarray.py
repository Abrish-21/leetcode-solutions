class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        global_max  = 0
        curr_max  = 0
        for num in nums:
            curr_max += num
            if curr_max < 0:
                curr_max = 0
            global_max = max(global_max, curr_max)
        global_min = 0
        curr_min = 0
        for num in nums:
            curr_min += num
            if curr_min > 0:
                curr_min = 0
            global_min = min(global_min, curr_min)
        return max(global_max, abs(global_min))
        