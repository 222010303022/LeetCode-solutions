class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res , sol = [], []
        def backtrack(openB,closedB):
            if openB == closedB == n :
                res.append(''.join(sol))
                return
            if openB < n :
                sol.append('(')
                backtrack(openB+1,closedB)
                sol.pop()
            if openB > closedB :
                sol.append(')')
                backtrack(openB,closedB+1)
                sol.pop()
        backtrack(0,0)
        return res

        
