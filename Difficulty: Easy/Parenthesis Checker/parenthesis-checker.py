class Solution:
    def isBalanced(self, s):
        res = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                res.append(ch)
            else:
                if not res:
                    return False
                top = res.pop()
                if ch == ')' and top != '(':
                    return False
                if ch == '}' and top != '{':
                    return False
                if ch == ']' and top != '[':
                    return False
                    
        return len(res) == 0
            
        
        
        