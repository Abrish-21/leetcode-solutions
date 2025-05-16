class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans  = 0
        left = 0
        current_a = 0
        for right in range(len(nums)):
            # remove the leftmost element fromt the AND
            while (current_a & nums[right] )!= 0:
                current_a ^= nums[left]
                left += 1
                # now add the current element to the AND
            current_a |= nums[right]
            ans  = max(ans, right - left + 1)
        return ans


        