class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        for i in range(len(position)):
            stack.append((position[i],speed[i]))
        stack.sort(reverse=True)
        time_stack=[]
        for i,j in stack:
            time=(target-i)/j
            if not time_stack or time_stack[-1]<time:
                time_stack.append(time)
        return len(time_stack)