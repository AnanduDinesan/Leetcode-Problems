class Solution:
    def concatenatedBinary(self, n: int) -> int:
        b=""
        for i in range(1,n+1):
            b+=bin(i)[2:]
        return int(b,2)%(10**9+7)