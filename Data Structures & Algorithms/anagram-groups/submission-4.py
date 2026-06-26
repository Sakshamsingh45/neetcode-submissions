class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for i in strs:
            j="".join(sorted(i))
            if j not in freq:
                freq[j]=[]
            freq[j].append(i)
        return list(freq.values())