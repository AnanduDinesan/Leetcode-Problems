class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        col=0
        st=True
        for c in range(len(strs[0])):
            for r in range(1,len(strs)):
                if ord(strs[r][c])<ord(strs[r-1][c]):
                    st=False
            if not st:
                col+=1
                st=True
        return col