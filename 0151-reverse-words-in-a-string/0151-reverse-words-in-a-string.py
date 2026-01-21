class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        r_s = list(reversed(s))
        return " ".join(r_s)