class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n=len(s)
        incremented = {str(n):str((n+a)%10) for n in range(10)}

        def add(s):
            res=''
            for i in range(n):
                res += s[i] if i % 2 == 0 else incremented[s[i]]
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