class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:

        i1, i2 = 0, 0

        for char_t in t:
            if (i2<len(s) and s[i2] == char_t) or (i1< len(s)):
                if i2 < len(s) and s[i2] == char_t:
                    next_i2 = i2 + 1
                else:
                    next_i2 = i1 + 1

                i2 = max(i2, next_i2)

            if i1 < len(s) and s[i1] == char_t:
                i1 += 1

            if i1 == len(s) or i2 == len(s):
                return True

        return i1 == len(s) or i2 == len(s)