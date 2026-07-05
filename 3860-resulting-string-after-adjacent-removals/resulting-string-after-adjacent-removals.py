class Solution:
    def resultingString(self, s: str) -> str:
        
        st=[]
        for ch in s:
            if st:
                if abs(ord(st[-1])-ord(ch))==1 or abs(ord(st[-1])-ord(ch))==25:
                    st.pop()
                    continue
            st.append(ch)
        return "".join(st)