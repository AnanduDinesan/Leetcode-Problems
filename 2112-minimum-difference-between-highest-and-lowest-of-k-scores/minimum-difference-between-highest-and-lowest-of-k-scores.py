class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=float('inf')
        print(nums,end="\n\n\n")
        for i in range(len(nums)-k+1):
            res=min(res,nums[k+i-1]-nums[i])
        return res