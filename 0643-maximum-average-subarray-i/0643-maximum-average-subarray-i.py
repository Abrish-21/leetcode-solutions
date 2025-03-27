class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        window_sum =  sum(nums[:k])
        max_sum = float(window_sum) / k
        
        for i in range(k,len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i-k]
            max_sum = max(max_sum, float(window_sum) / k)
        
        return max_sum


                