class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        
        for i in range(2):
            if s1[i] != s2[i] or s1[i+2] != s2[i+2]:
                s1[i], s1[i+2] = s1[i+2], s1[i]
        
        return "".join(s1) == s2