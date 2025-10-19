class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n=len(s)

        def add(s):
            res=''
            for i in range(n):
                res+=str((int(s[i])+a)%10) if i%2 else s[i]
            return res

        def rotate(s):
            return s[n-b:]+s[:n-b]
        
        visited=set()

        def dfs(s):
            if s in visited:
                return
            visited.add(s)
            dfs(add(s))
            dfs(rotate(s))
            return
        
        dfs(s)
        print(visited)
        return min(visited)