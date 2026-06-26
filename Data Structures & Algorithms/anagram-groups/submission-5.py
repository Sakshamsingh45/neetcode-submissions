class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-ord("a")]+=1
            key=tuple(count)
            if key not in freq:
                freq[key]=[]
            freq[key].append(i)
        return list(freq.values())