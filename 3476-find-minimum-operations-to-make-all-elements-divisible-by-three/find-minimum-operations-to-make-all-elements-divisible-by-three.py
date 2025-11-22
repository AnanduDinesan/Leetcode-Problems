class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            r=i%3
            res+=(r if r<2 else 3-r)
        return res