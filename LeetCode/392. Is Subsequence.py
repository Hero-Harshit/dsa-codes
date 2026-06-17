class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        idx = 0

        for ch in t:

            if idx < len(s) and ch == s[idx]:
                idx += 1

        return idx == len(s)