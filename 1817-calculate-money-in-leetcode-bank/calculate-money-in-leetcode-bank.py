class Solution:
    def totalMoney(self, n: int) -> int:
        week=n//7
        day=n%7
        bal=0
        i=1
        while i<=week:
            bal+=(7*(2*i+6)//2)
            i+=1
        bal+=(day*(2*i+day-1)//2)
        return bal