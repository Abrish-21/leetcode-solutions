class Solution:
    def find132pattern(self, zx):
        bb=float('-inf')
        ss=[]
        for v in zx[::-1]:
            if v<bb:
                return True
            while ss and ss[-1]<v:
                bb=ss.pop()
            ss.append(v)
        return False
