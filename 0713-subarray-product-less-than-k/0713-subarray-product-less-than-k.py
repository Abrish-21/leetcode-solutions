class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:  # If k is 0 or 1, no valid subarray exists
            return 0
        
        product = 1
        count = 0
        left = 0
        
        for right in range(len(nums)):
            product *= nums[right]
            
            while product >= k and left <= right:
                product //= nums[left]
                left += 1
            
            count += (right - left + 1)  # Number of valid subarrays ending at 'right'
        
        return count
        