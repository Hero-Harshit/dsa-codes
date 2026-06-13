class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        cleaned_str = ""
        for ch in s:

            if ch.isalnum():
                cleaned_str += ch

        rev_str = ""
        for ch in cleaned_str:
            rev_str = ch + rev_str


        if rev_str == cleaned_str:
            return True
        return False       