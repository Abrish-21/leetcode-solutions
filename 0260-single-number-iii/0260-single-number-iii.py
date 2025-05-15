class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        num_1 = 0
        num_2 = 0
        right_most_xor = (xor_sum) & -(xor_sum)
        for num in nums:
            if (right_most_xor & num) == 0:
                num_1 ^= num
            else:
                num_2  ^= num
        return [num_1, num_2]
            

        