class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        lr=len(mat)
        lc=len(mat[0])
        r=[0]*lr
        c=[0]*lc

        for i in range(lr):
            for j in range(lc):
                if mat[i][j] == 1:
                    r[i]+=1
                    c[j]+=1
        
        res=0
        for i in range(lr):
            for j in range(lc):
                if mat[i][j]==1 and r[i]==1 and c[j]==1:
                    res+=1

        return res
