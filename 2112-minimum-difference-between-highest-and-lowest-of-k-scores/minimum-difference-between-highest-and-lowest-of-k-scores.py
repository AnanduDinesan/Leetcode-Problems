class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        result=float('inf')
        for i in range(k-1,len(nums)):
            result=min(result,nums[i]-nums[i-k+1])
        return result