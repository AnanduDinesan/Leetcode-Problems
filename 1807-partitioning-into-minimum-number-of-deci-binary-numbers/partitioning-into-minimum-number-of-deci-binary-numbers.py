class Solution:
    def minPartitions(self, n: str) -> int:
        num=list(map(int,n))
        num.sort()

        res=0
        diff=0
        for i in num:
            diff=i-res
            res+=diff
        
        return res