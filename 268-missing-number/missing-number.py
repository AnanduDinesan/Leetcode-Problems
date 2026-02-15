class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s1=sum(nums)
        s2=(n*(n+1))//2
        return s2-s1