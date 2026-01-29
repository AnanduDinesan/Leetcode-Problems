from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        c_sct=dict(Counter(secret))
        a=0
        b=0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                a+=1
                c_sct[secret[i]]-=1
                if c_sct[secret[i]]==0:
                    c_sct.pop(secret[i])
        
        for i in range(len(secret)):
            if secret[i]!=guess[i] and guess[i] in c_sct:
                b+=1
                c_sct[guess[i]]-=1
                if c_sct[guess[i]]==0:
                    c_sct.pop(guess[i])
        
        return str(a)+"A"+str(b)+"B"
