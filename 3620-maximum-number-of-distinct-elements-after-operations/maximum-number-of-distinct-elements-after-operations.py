class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:

        nums.sort()
        curr=float('-inf')
        res=0

        for i in nums:
            l=i-k
            h=i+k
            ch=max(l,curr+1)
            if ch<=h:
                res+=1
                curr=ch
        return res