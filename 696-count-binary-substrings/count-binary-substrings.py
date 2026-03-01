class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        d1={'0':0,'1':0}
        res=0
        for i in range(len(s)):
            if i>0 and s[i]!=s[i-1]:
                res+=min(d1['0'],d1['1'])
                d1[s[i]]=0
            d1[s[i]]+=1
        res+=min(d1['0'],d1['1'])
        return res