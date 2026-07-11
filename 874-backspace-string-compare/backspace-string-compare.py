class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st=[]
        ts=[]
        for ch in s:
            if  ch=='#':
                if st:st.pop()
            else:
                st.append(ch)
        for ch in t:
            if ch=='#':
                if ts:ts.pop()
            else:
                ts.append(ch)
                
        return "".join(st)=="".join(ts)
        