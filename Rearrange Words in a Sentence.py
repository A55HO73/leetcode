class Solution:
    def arrangeWords(self, text: str) -> str:
        l = text.lower().split()
        ln = len(l)
        if ln == 0 :
            return 0
        else :
            l.sort(key=len)
            return " ".join(l).capitalize()
        
