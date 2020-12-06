from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char = Counter(chars)
        total_lenght = 0
        for items in words:
        	item_Count = Counter(items)
        	intersection = char & item_Count #set can't be used since repeated elements won't be counted
        	intSect = sum(intersection.values())
        	if intSect == len(items):
        		total_lenght += intSect

        return total_lenght
