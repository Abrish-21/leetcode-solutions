class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        average = set()
        nums.sort()
        left = 0
        right = len(nums) -1
        while left < right:
            average.add((nums[right] + nums[left])/2)
            left  +=1 
            right-=1
        return len(average)

        