class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [''] * numRows
        i, flag = 0, False
        
        for ch in s:
            rows[i] += ch
            if i == 0 or i == numRows - 1:
                flag = not flag
            i += 1 if flag else -1
        
        return ''.join(rows)