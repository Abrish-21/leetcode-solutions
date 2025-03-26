class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]  # Initialize with a valid sum
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest sum if needed
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                
                # Move pointers based on comparison
                if curr_sum < target:
                    left += 1  # Increase sum
                elif curr_sum > target:
                    right -= 1  # Decrease sum
                else:
                    return curr_sum  # Exact match found
                
        return closest_sum
        