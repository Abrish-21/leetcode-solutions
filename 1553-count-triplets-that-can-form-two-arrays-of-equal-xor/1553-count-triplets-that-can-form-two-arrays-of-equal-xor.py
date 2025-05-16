class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        xor_sum = defaultdict(int)
        xor = 0
        for i in range(len(arr)):
            xor ^= arr[i]
            xor_sum[i] = xor
        count  = 0
       
        for i in range(0,len(arr)):
            for k in range(len(arr)):
                if i < k:
                    if (xor_sum[i - 1]  ^ xor_sum[k] == 0):
                        count += k - i
        return count

        