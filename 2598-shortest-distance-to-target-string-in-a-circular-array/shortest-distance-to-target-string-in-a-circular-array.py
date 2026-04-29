class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=len(words)
        result=float('inf')
        for i in range(n):
            if words[(i + startIndex) % n]==target:
                idx = (i + startIndex) % n
                dist = min(abs(idx - startIndex), n - abs(idx - startIndex))
                result = min(result, dist)
        
        if result==float('inf'):
            return -1
        else:
            return result