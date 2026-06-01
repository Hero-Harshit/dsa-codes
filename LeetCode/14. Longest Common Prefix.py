class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()

        i = 0

        while (
            len(strs[0]) > i
            and len(strs[-1]) > i
            and strs[0][i] == strs[-1][i]
        ):
            i += 1

        return strs[0][:i]