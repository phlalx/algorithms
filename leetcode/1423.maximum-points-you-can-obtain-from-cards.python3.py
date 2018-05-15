# Trick: this is not DP!!!
#   it's just a sliding window problem (find minimal window of size n-k)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int):
        n = len(cardPoints)
        window = sum(cardPoints[:k])
        res = window
        for i in range(k):
            print(window)
            window -= cardPoints[k - 1 - i]
            window += cardPoints[n-i-1]    
            res = max(res, window)
        return res

