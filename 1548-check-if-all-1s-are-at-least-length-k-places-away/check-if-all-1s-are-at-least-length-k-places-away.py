class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        j=k
        for i in nums:
            if i==1:
                if j<k:
                    return False
                else:
                    j=0
            else:
                j+=1
            
        return True