class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        res=0
        for d in [-1,1]:
            dist=0
            for i in moves:
                if i=="L":
                    dist-=1
                elif i=="R":
                    dist+=1
                else:
                    dist+=(1*d)
            res=max(res,abs(dist))
        return res