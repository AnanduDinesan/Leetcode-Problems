class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        res=[]
        n=len(digits)

        def backtrack(level,comb):
            if level==n:
                res.append(comb)
                return 
            for i in phone[digits[level]]:
                backtrack(level+1,comb+i)

        backtrack(0,"")
        return res