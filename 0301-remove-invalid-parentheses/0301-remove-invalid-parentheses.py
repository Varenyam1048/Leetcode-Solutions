class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)

    
        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left:
                    left -= 1
                else:
                    right += 1

        res = []
        path = []

        
        def dfs(i, l, r, bal):
            if i == n:
                if l == 0 and r == 0 and bal == 0:
                    res.append(''.join(path))
                return

            ch = s[i]

            
            if ch != '(' and ch != ')':
                path.append(ch)
                dfs(i + 1, l, r, bal)
                path.pop()
                return

            
            j = i
            while j < n and s[j] == ch:
                j += 1
            k = j - i

    
            for rem in range(k + 1):
                keep = k - rem
                nl, nr, nbal = l, r, bal
                if ch == '(':
                    nl -= rem
                    nbal += keep
                else:
                    nr -= rem
                    nbal -= keep

                if nl < 0 or nr < 0:
                    break         
                if nbal < 0:
                    continue       

                path.extend(ch * keep)
                dfs(j, nl, nr, nbal)
                del path[len(path) - keep:]

        dfs(0, left, right, 0)
        return res