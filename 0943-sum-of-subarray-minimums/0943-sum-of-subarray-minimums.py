class Solution:
    def sumSubarrayMins(self, qz):
        md=10**9+7
        n=len(qz)
        lf=[0]*n
        rg=[0]*n
        st=[]
        for i in range(n):
            while st and qz[st[-1]]>qz[i]:
                st.pop()
            lf[i]=i-st[-1] if st else i+1
            st.append(i)
        st.clear()
        for i in range(n-1,-1,-1):
            while st and qz[st[-1]]>=qz[i]:
                st.pop()
            rg[i]=st[-1]-i if st else n-i
            st.append(i)
        sm=0
        for i in range(n):
            sm=(sm+qz[i]*lf[i]*rg[i])%md
        return sm
