class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result  = []
        size = len(nums)
        for  i in range(size):
            if nums[i] > 0:
                result.append(nums[( i + nums[i]) % size])
            elif nums[i] < 0:
                result.append(nums[ i -  (abs(nums[i]) % size)])
            else:
                result.append(nums[i])
        return result
            
            


        