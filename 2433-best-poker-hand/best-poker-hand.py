from collections import Counter

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits))==1:
            return "Flush"
        
        ct=Counter(ranks)

        if max(ct.values())>=3:
            return "Three of a Kind"
        elif max(ct.values())>=2:
            return "Pair"
        else:
            return "High Card"
