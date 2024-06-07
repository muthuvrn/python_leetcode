class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 0
        max_len = 0
        m = {}
        for r, c in enumerate(s):
            m[c] = m.get(c, 0) + 1
            if m[c] == 1:
                if r - l + 1 > max_len:
                    max_len = max(max_len, r - l + 1)
                    res = [l, r]
            else:
                while m[c] > 1:
                    m[s[l]] -= 1
                    l += 1
        return max_len