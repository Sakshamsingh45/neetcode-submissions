class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        res=[0]*n
        for i,j in enumerate(temperatures):
            while stack and stack[-1][0]<j:
                extra,index=stack.pop()
                res[index]=i-index
            stack.append((j,i))
        return res