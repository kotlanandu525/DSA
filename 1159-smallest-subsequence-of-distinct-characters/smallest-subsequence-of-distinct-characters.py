class Solution:
    def smallestSubsequence(self, s: str) -> str:
        st=[]
        fmap=Counter(s)
        inans=set()
        for ch in s:
            fmap[ch]-=1
            if ch in inans: continue
            while st and st[-1]>ch and fmap[st[-1]]:
                inans.remove(st.pop())
            st.append(ch)
            inans.add(ch)
        return "".join(st)
            


        