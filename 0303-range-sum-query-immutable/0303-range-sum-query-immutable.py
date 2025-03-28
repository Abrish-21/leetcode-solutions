class NumArray:

    def __init__(self, nums: List[int]):
        self.PrefixSum = nums
        for i in range(1, len(nums)):
            self.PrefixSum[i]  =  self.PrefixSum[i-1] + self.PrefixSum[i]
        self.PrefixSum.append(0)

    def sumRange(self, left: int, right: int) -> int:
        return self.PrefixSum[right] -  self.PrefixSum[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)