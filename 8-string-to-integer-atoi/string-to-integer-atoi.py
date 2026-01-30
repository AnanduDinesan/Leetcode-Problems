class Solution:
    def myAtoi(self, s: str) -> int:
        pos=True
        s=s.strip()
        
        if not s:
            return 0

        if s[0]=="-":
            pos=False
            s=s[1:]
        elif s[0]=="+":
            s=s[1:]
        s=s.lstrip("0")

        res=""
        for i in s:
            if not i.isdigit():
                break
            res+=i
        
        if not res:
            return 0
        
        if pos:
            res=int(res)
        else:
            res=int(res)*-1

        if res < -2**31:
            return -2**31
        elif res > 2**31-1:
            return 2**31-1
        else:
            return res
