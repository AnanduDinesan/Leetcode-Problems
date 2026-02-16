class Solution:
    def reverseBits(self, n: int) -> int:
        b=bin(n)[2:]
        res="0"*(32-len(b))+b
        return int(res[::-1],2)