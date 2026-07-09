class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open=set(["{","(","["])
        close=set(["}","]",")"])
        for i in s:
            if i in open:
                stack.append(i)
            elif stack:
                if i=="}" and stack[-1]=="{":
                    stack.pop()
                elif i==")" and stack[-1]=="(":
                    stack.pop()
                elif i=="]" and stack[-1]=="[":
                    stack.pop()
                else:
                    return False
            else:
                return False
        return not bool(stack)