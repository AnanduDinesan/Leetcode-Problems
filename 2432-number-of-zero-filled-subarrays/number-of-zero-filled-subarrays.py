class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        conc=1
        if nums[0]==0:
            res=1
        else:
            res=0
        for i in range(1,len(nums)):
            if nums[i]==0:
                if nums[i-1]==0:
                    conc+=1
                elif nums[i-1]!=0:
                    conc=1
                res+=conc
        return res