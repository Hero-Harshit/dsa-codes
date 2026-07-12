class Solution:
    def reverseString(self, s: List[str]) -> None:

        start_index = 0
        end_index = len(s)-1

        for i in range(len(s)):

            if start_index > end_index:
                break

            s[start_index], s[end_index] = s[end_index], s[start_index]
            start_index += 1
            end_index -= 1