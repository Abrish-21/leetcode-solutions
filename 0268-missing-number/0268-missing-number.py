class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_sum_1 = 0
        xor_sum_2 = 0
        for i, num in enumerate(nums):
            xor_sum_1 ^= num
            xor_sum_2 ^= i + 1
        return xor_sum_2 ^ xor_sum_1

        