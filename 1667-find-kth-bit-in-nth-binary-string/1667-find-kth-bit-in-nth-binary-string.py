class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(s):
            return s[::-1]
        def invert(t):
            t_arr = [i for i in t]
            for i in range(len(t_arr)):
                if t_arr[i]  == "0":
                    t_arr[i] = "1"
                else:
                    t_arr[i] = "0"
            return ''.join(t_arr)
        result = ""
        def find(n):
            if n == 1:
                return "0"
            nxt = find(n-1)
            return nxt + "1" + reverse(invert(nxt))
        result = find(n)
        print(result)
        return result[k-1]
        




        