class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse = True)
        freq = [0] * len(nums)
        for l,r in requests:
            freq[l] +=1
            if r + 1 < len(freq):
                freq[r+1] -= 1
        for i in range(1,len(freq)):
            freq[i] += freq[i-1]

        sorted_freq = sorted(freq, reverse = True)
        
        total  = 0
        for a,b in zip(sorted_freq, nums):
            total += a * b 
        return total   % ( pow(10, 9) + 7)
        


