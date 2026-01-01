class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s_num="".join(map(str,digits))
        new_num=str(int(s_num)+1)
        res=list(map(int,new_num))
        return res