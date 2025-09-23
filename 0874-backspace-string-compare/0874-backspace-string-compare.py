class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(arr):
            ans = []
            for c in arr:
                if c != "#":
                    ans.append(c)
                else:
                    if ans:

                        ans.pop()
            return ans
        return build(s) == build(t)


        