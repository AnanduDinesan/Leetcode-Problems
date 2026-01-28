class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                sub_str=s[i:j+1]
                if sub_str==sub_str[::-1] and len(sub_str)>len(res):
                    res=sub_str
        return res