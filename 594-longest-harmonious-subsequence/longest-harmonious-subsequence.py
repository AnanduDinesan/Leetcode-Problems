class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        l,r=0,1
        while r<len(nums) and l<len(nums):
            if nums[r]-nums[l]<1:
                r+=1
            elif nums[r]-nums[l]>1:
                l+=1
            else:
                result=max(result,r-l+1)
                r+=1
        return result