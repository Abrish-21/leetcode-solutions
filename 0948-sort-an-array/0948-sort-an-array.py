class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        min_val = min(nums)
        max_val = max(nums)
        
        range_of_numbers = max_val - min_val + 1
        
        count = [0] * range_of_numbers
        
        for num in nums:
            count[num - min_val] += 1
        
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        output = [0] * len(nums)
        for num in reversed(nums):
            output[count[num - min_val] - 1] = num
            count[num - min_val] -= 1
        
        return output
