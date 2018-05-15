#TAGS dp

class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        N = len(s)
        memo = [ [ None ] * N for _ in range(N) ]

        def f(s, i, j):
            if memo[i][j]:
                return memo[i][j]
            if i == j:
                res = 1 if s[i] == '(' or s[i] == ')' else 0
            elif i > j:
                res = 0
            else: 
                next_states = []
                if s[i] == '(' and s[j] == ')':
                    next_states.append(f(s, i+1, j-1))
                next_states.extend( f(s, i, k) + f(s, k+1, j) for k in range(i,j))
                res = min(next_states)
            memo[i][j] = res
            return res

        return f(s, 0, len(s) - 1)
    
def main():
    s = "())"
    sol = Solution()
    res = sol.removeInvalidParentheses(s)
    print('res = ', res)

main()
        
