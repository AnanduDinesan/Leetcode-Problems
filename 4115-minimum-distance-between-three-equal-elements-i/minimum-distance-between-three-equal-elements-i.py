class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        result=float('inf')
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]==nums[j]==nums[k]:
                        print(i,j,k)
                        diff=abs(i-j)+abs(j-k)+abs(k-i)
                        result=min(diff,result)
        
        if result==float('inf'):
            return -1
        else:
            return result