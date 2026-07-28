class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=0,max(piles)
        res=r
        while l<=r:
            mid=(l+r)//2
            if mid==0:
                return res
            temp=h
            for j,i in enumerate(piles):
                ceil=0
                time_pile=i/mid
                if time_pile%1>0:
                    ceil=1
                temp-=(int(time_pile)+ceil)
                if temp<(len(piles)-j-1):
                    l=mid+1
                    break
                elif temp>=0 and j==len(piles)-1:
                    res=mid
                    r=mid-1
                elif j==len(piles)-1:
                    r=mid-1
        return res