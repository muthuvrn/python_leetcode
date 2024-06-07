class Solution:
    def longestPalindrome(self, s: str) -> str:
        _l, _r = 0, 0
        maxLens = 0
        for i in range(len(s)):
            l, r = i-1, i
            while r < len(s) and s[r] == s[i]:
                r += 1
            while l >= 0 and r < len(s) and s[l] == s[r] :
                l -= 1
                r += 1
            if r-l-1 > maxLens:
                maxLens = r-l-1
                _l, _r = l, r
            if r-l-1 == len(s):
                break
        return s[_l+1:_r]