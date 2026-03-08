class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums[0])
        large=2**n-1
        dec=set(map(lambda x: int(x,2),nums))
        print(dec)
        print(large)
        
        for i in range(large,-1,-1):
            if i not in dec:
                b=bin(i)[2:]
                return "0"*(n-len(b))+b