class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        intervals.sort()
        l=intervals[0][0]
        r=intervals[0][1]

        res=[]
        for i in intervals[1:]:
            if i[0]<=r:
                r=max(r,i[1])
            else:
                res.append([l,r])
                l,r=i[0],i[1]
        res.append([l,r])

        return res