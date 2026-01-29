from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(check):
            ct=0
            for i in check:
                if i=="(":
                    ct+=1
                elif i==")":
                    ct-=1
                if ct<0:
                    return False
            return ct==0

        res = []
        visited = set()
        queue = deque([s])
        visited.add(s)
        found = False

        while queue:
            curr=queue.popleft()

            if is_valid(curr):
                res.append(curr)
                visited.add(curr)
                found=True
            
            if found:
                continue
            
            for i in range(len(curr)):
                if curr[i] not in '()':
                    continue
                sub=curr[:i]+curr[i+1:]
                if sub not in visited:
                    visited.add(sub)
                    queue.append(sub)
        return res

