class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        long = 0
        ans = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            long = max(long, freq[s[r]])
            while (r - l + 1) - long > k:
                freq[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans
