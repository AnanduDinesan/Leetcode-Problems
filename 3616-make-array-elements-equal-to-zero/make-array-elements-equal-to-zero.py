class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        def is_zero_sum(ind,dir):
            cp_nums=nums[:]
            while 0<=ind<len(cp_nums):
                if cp_nums[ind]==0:
                    ind+=dir
                elif cp_nums[ind]>0:
                    cp_nums[ind]-=1
                    dir*=-1 
                    ind+=dir
            return sum(cp_nums)==0
        
        res=0
        for i in range(len(nums)):
            if nums[i]==0:
                if is_zero_sum(i,1):
                    res+=1
                if is_zero_sum(i,-1):
                    res+=1
        
        return res
