from collections import deque
class Solution:
    def longestSubarray(self, qv, lm):
        a=deque()
        b=deque()
        s=0
        m=0
        for e in range(len(qv)):
            while a and a[-1]<qv[e]: a.pop()
            a.append(qv[e])
            while b and b[-1]>qv[e]: b.pop()
            b.append(qv[e])
            while a[0]-b[0]>lm:
                if a[0]==qv[s]: a.popleft()
                if b[0]==qv[s]: b.popleft()
                s+=1
            m=max(m,e-s+1)
        return m
