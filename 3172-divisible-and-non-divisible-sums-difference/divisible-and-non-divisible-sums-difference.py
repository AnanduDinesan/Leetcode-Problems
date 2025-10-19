class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1=sum(i for i in range(1,n+1) if i%m)
        num2=sum(i for i in range(1,n+1) if not i%m)
        return num1-num2