from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        largest=max(cnt.values())
        res=(list(cnt.values()).count(largest))*largest
        return res
