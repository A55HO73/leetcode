class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        tgt = ord(target)
        max_ord = ord(letters[-1])
        if max_ord <= tgt :
            return letters[0]
        else :
            for items in letters :
                if tgt < ord(items):
                    return items
        
