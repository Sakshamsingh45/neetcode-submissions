class TimeMap:

    def __init__(self):
        self.data={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key]=[]
        self.data[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        val=None
        l,r=0,len(self.data[key])-1
        while l<=r:
            mid=(l+r)//2
            if self.data[key][mid][1]==timestamp:
                return self.data[key][mid][0]
            elif self.data[key][mid][1]>timestamp:
                r=mid-1
            else:
                l=mid+1
                val=self.data[key][mid][0]
        if val:
            return val
        else:
            return ""


