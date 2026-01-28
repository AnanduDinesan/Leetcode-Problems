class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        l,r=0,0
        start=0
        end=0
        def left_right(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return r,l+1

        for i in range(len(s)):
            r1,l1=left_right(i,i)
            if end-start<r1-l1:
                start=l1
                end=r1
            r2,l2=left_right(i,i+1)
            if end-start<r2-l2:
                start=l2
                end=r2
        return s[start:end]