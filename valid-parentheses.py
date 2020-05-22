class Solution:
    def isValid(self, s: str) -> bool:
        tmp = []
        for i in s:
            if i == '(':
                tmp.append(i)
            elif i == ')':
                if tmp and tmp[-1] == '(':
                    tmp.pop()
                else:
                    return False
            elif i == '[':
                tmp.append(i)
            elif i == ']':
                if tmp and tmp[-1] == '[':
                    tmp.pop()
                else:
                    return False
            elif i == '{':
                tmp.append(i)
            elif i == '}':
                if tmp and tmp[-1] == '{':
                    tmp.pop()
                else:
                    return False
        if tmp:
            return False
        return True