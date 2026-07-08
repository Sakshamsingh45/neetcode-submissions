class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        mc=0
        while i<j:
            fill=min(heights[i],heights[j])*(j-i)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
            mc=max(mc,fill)
        return mc