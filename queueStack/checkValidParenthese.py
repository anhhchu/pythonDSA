class Solution: 
    def validParentheses(self,s):
        if len(s) < 2:
            return False
        stack = []
        brackets = {'(':')','[':']','{':'}'}
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif stack and char == brackets[stack[-1]]:
                stack.pop()
            else:
                return False

        return stack == []

sol = Solution()
print(sol.validParentheses('[['))
print(sol.validParentheses('}['))
print(sol.validParentheses('{[()]}'))