class Solution:
    def resultingString(self, s: str) -> str:
        
        st=[]
        for ch in s:
            if st and (abs(ord(st[-1])-ord(ch)) in (1,25)):
                st.pop()
            else:
                st.append(ch)
            
                
        return "".join(st)