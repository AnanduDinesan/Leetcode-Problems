class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if not n:
            return False
        return True if not n&(n-1) else False