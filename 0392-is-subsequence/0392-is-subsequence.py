class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        if not s:
            return True

        while j < len(t):
            if i < len(s) and s[i] == t[j]:
                i += 1
            if i == len(s):
                return True
            
            j += 1

        return i == len(s)