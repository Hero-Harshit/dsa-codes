class Solution:
    def isPalindrome(self, x: int) -> bool:

        x = str(x)

        a = ""

        for i in x:
            a = i + a

        if x == a:
            return True

        return False