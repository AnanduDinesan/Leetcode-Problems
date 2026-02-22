class Solution:
    def binaryGap(self, n: int) -> int:
        b=bin(n)[2:]
        l=0
        r=1
        res=0
        while l<len(b) and r<len(b):
            if b[l]=='1' and b[r]=='1':
                res=max(res,r-l)
                l=r
                r+=1
                continue
            if b[l]=='0':
                l+=1
                continue
            if b[r]=='0':
                r+=1
                continue
        return res