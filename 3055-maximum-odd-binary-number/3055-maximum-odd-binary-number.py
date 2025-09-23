class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s_arr = [i for i in s]
        sorted_s = sorted(s_arr, reverse = True)
        for i in range(len(sorted_s)-1, -1 ,-1):
            if sorted_s[i] == '1':
                sorted_s[i], sorted_s[-1] = sorted_s[-1], sorted_s[i]
                break 

        return ''.join(sorted_s)

        