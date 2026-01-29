class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def back_track(open,close,pairs):
            if len(pairs)==n*2:
                res.append(pairs)
                return
            if open<n:
                back_track(open+1,close,pairs+"(")
            if close<open:
                back_track(open,close+1,pairs+")")


        back_track(0,0,"")
        return res