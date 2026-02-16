class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        for i in range(n):
            if nums[i] == 0:
                res[i]=0
            else:
                ind=(i+nums[i])%n
                res[i]=nums[ind]
        return res