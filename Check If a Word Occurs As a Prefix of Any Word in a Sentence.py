class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = sentence.strip().split()
        for words in l :
            if words.startswith(searchWord) :
                return l.index(words) + 1
        return -1 
        
