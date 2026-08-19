class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s=''
        ans=[]
        def back(s,open,close):
            if len(s)==n*2:
                ans.append(s)
                return
            if open<n:
                back(s+'(',open+1,close)
            if close<open:
                back(s+')',open,close+1)

        back(s,0,0)
        return ans