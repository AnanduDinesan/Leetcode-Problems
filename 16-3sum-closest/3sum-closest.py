class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res=0
        diff=float('inf')
        nums.sort()

        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1

            while l<r:
                s=nums[i]+nums[l]+nums[r]
                curr=abs(target-s)

                if s<target:
                    l+=1
                elif s>target:
                    r-=1
                else:
                    l+=1
                    return s
                
                if curr<diff:
                    diff=curr
                    res=s
        return res

        