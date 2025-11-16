class Solution:
    def numSub(self, s: str) -> int:
        c=0
        t=0
        for i in s:
            if i=='1':
                t+=1
            else:
                t=0
            c=(c+t)%(10**9+7)
        return c
