class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char={}
        for i in s:
            char[i]=char.get(i,0)+1
        for j in t:
            if j not in char:
                return False
            char[j]-=1
            if char[j]==0:
                char.pop(j)
            
        return not bool(char)