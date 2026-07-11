class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for ch in s:
            if not st or ch in '({[':
                st.append(ch)
            else:
                if ch==')':
                    if st[-1]=='(':
                        st.pop()
                    else:
                        st.append(ch)
                if ch==']':
                    if st[-1]=='[':
                        st.pop()
                    else:
                        st.append(ch)
                if ch=='}':
                    if st[-1]=='{':
                        st.pop()
                    else:
                        st.append(ch)
        return False if len(st)>0 else True