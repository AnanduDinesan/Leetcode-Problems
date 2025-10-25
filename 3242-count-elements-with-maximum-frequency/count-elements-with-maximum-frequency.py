from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt_nums=Counter(nums)
        max_num=cnt_nums.most_common(1)[0][1]
        cnt=0
        print(cnt_nums.values())
        for v in cnt_nums.values():
            if v==max_num:
                cnt+=max_num
        return cnt