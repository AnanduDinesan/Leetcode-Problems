class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotation(mat):
            for i in range(len(mat)):
                for j in range(i):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            
            return mat[::-1]
        
        for _ in range(4):
            if mat==target:
                return True
            mat=rotation(mat)
        
        return False