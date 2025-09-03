class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs=''
        for i in s:
            if i.isalnum():
                cs+=i.lower()
        print(cs)
        
        l,r=0,len(cs)-1

        while r>l:
            if cs[l]!=cs[r]:
                return False
            l+=1
            r-=1

        return True