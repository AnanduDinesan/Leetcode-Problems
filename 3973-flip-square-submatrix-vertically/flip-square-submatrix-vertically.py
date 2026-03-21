class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        t=0
        for i in range(x,x+k//2):
            for j in range(y,y+k):
                grid[i][j],grid[x+k-1-t][j]=grid[x+k-1-t][j],grid[i][j]
            t+=1
        return grid