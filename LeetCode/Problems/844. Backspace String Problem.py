class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = []
        for chr in s:
            if chr == "#":
                if len(new_s) == 0:
                    pass
                else:
                    new_s.pop()
            else:
                new_s.append(chr)    

        new_t = []
        for chr in t:
            if chr == "#":
                if len(new_t) == 0:
                    pass
                else:
                    new_t.pop()
            else:
                new_t.append(chr)        

        return new_s == new_t  