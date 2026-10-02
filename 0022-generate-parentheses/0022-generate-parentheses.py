class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        def solve(open,close,curr):
            if len(curr)== 2*n:
                ans.append(curr)
                return 
            
            if open<n:
                solve(open+1,close,curr+"(")

            if close<open:
                solve(open,close+1,curr+")")

        solve(0,0,"")

        return ans 