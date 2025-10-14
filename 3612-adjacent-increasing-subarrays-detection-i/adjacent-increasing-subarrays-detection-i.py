class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        cnt=k-1
        if not cnt:
            return True
        for i in range(1,len(nums) - k):
            if nums[i]<=nums[i-1] or nums[i+k]<=nums[i+k-1]:
                cnt=k-1
            else:
                cnt-=1
            if not cnt:
                return True
    
        return False
        




















    