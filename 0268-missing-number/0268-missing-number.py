class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_sum_1 = 0
        n = len(nums)
        for i in range(n + 1):
            xor_sum_1 ^= i
        xor_sum_2 = 0
        for num in nums:
            xor_sum_2 ^= num
        return xor_sum_2 ^ xor_sum_1
        