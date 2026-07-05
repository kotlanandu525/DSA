class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        for i in range(len(word)):
            nword=word[:i]+word[i+1:]
            f=Counter(nword)
            if len(set(f.values()))==1:
                return True
        return False
