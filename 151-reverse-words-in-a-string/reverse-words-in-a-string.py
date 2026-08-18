class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        words=s.split(' ')
        print(words)
        ans=[]
        for word in words:
            if word!='':
                ans.append(word)
        print(ans)      
        return " ".join(ans[::-1])