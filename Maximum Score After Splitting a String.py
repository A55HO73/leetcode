class Solution:
    def maxScore(self, s: str) -> int:
        lenght = len(s)
        score = 0
        for i in range(lenght -1):
            f_score = s[0:i+1].count("0") + s[i+1:lenght].count("1")
            if (f_score > score) :
                score = f_score
            else :
                None
        return score
