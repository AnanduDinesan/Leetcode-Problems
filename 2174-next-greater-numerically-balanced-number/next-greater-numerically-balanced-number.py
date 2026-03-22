class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(num):
            ct=[0]*10
            for i in str(num):
                ct[int(i)]+=1
            
            for i in range(len(ct)):
                if ct[i]!=0 and ct[i]!=i:
                    return False
            return True
        
        res=n+1
        while True:
            if is_balanced(res):
                return res
            res+=1
