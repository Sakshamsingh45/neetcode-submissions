class Solution:

    def encode(self, strs: List[str]) -> str:
        st=""
        for i in strs:
            st+=str(len(i))+"#"+i
        return st
    def decode(self, s: str) -> List[str]:
        i=0
        ans=[]
        while i<len(s):
            count=""
            while s[i]!="#":
                count+=s[i]
                i+=1
            l=int(count)
            if l==0:
                ans.append("")
                i+=1
                continue
            ans.append(s[i+1:i+1+l])
            i+=l+1
        return ans
            
            