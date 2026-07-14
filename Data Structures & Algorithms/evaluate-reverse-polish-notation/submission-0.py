class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack=[]
        opset=set(['+', '-', '*', '/'])
        for i in tokens:
            if i not in opset:
                num_stack.append(int(i))
            else:
                num1=num_stack.pop()
                num2=num_stack.pop()
                if i=="+":
                    num_stack.append(num2+num1)    
                elif i=="-":
                    num_stack.append(num2-num1)
                elif i=="*":
                    num_stack.append(num2*num1)
                elif i=="/":
                    num_stack.append(int(num2/num1))
        return num_stack[-1]