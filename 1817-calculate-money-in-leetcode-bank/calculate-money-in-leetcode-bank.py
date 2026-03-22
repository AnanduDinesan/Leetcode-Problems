class Solution:
    def totalMoney(self, n: int) -> int:
        if n==0:
            return 0
        
        mon=1
        res=1
        inc=1
        for i in range(1,n):
            inc+=1
            if i%7==0:
                mon+=1
                inc=mon
            res+=inc
        
        return res
            
            